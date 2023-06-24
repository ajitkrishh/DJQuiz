import json
from typing import List

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
'''
'''
from .models import (
    Topic , Question,Option,QuestionSet,Test
)


class TopicListView(LoginRequiredMixin,View):
    def get(self,request):

        key =request.user.id
        request.session[f'{key}-start'] = False
        request.session[f'{key}-score'] = None
        request.session[key] = None
        request.session[f'{key}-test'] = None

        qs = Topic.objects.values('id','name')
        context = {'topics' : qs}

        return render(request , 'DJQuiz/show_topic.html', context)
    
    def post(self,request):
        try:
            topicid_ = request.POST.get('topic' , None)
            if not topicid_:
                messages.error(request,'select any one topic !!!')
                return redirect('topiclist')
            
            questions = Question.objects.filter(topic_id = topicid_).values_list('id' , flat=True).order_by('?')[:10]
            if len(questions) == 0:
                messages.error(request,'No questions  !!!')
                return redirect('topiclist')
            
            new_test = Test.objects.create(
                user = request.user,
                total_question = len(questions),
                topic_id = topicid_
            )
            key = request.user.id
            request.session[f'{key}-start'] = True
            request.session[f'{key}-score'] = 0
            request.session[key] = list(questions) 
            request.session[f'{key}-test'] = new_test.id

            return redirect('test')
        
        except Exception as e:
            print(e)
            messages.error(request,'something went wrong')
            return redirect('topiclist')


class FetchQuestion(LoginRequiredMixin,View):
    def get(self,request):
        key = request.user.id
        if not request.session[f'{key}-start'] :
            return redirect('topiclist')
         
        questions = request.session[key]
        if len(questions) < 1:
            # here all questions are attemmpted, update the test result ....
            test_id = request.session[f'{key}-test']
            test = Test.objects.get(id = test_id)
            test.score = request.session[f'{key}-score']
            test.save()
            request.session[f'{key}-start'] = False
            request.session[f'{key}-topic'] = None
            return redirect('result')
        
        question = questions.pop()
        
        request.session[key] = questions
        question = QuestionSet.objects.filter(question_id = question)\
                    .select_related('question','option')\
                    .values_list('question_id','question__question','option_id', 'option__name')
        # extracting options
        options = [ row[2:] for row in question]
        # extracting question
        question = tuple(question[0][:2])

        context = {'question' : question , 'options' : options,"code":201 }
        # print(context)
        return JsonResponse(context)
    
    def post(self,request):
        key = request.user.id
        qid = request.POST.get('question' , None)
        option = request.POST.getlist('option[]' , None)

        if not qid:
            print('qid not found    ')
            messages.error(request,'something went wrong')
            return redirect('topiclist')
        
        opt = QuestionSet.objects.filter(question_id = qid , is_true = True).values_list('option_id' , flat=True) 
        
        if set(option) == set(opt):
            score = request.session[f'{key}-score']
            request.session[f'{key}-score'] = score + 1
        return JsonResponse({'message': 'ok'})


class TestView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request , 'DJQuiz/show_question.html')
        
class ResultListView(ListView):
    model = Test
    template_name = "DJQuiz/result.html"

    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(user_id = self.request.user.id).select_related('topic').order_by('-updated_at')
        return qs
