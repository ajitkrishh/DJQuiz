
from django.contrib import admin
from .models import Topic, Question, Option, QuestionSet, Test
from django.db import models



admin.site.register(Option)
class OptionInline(admin.StackedInline):
    model = Option
    extra = 1

class QuestionSetInline(admin.StackedInline):
    model = QuestionSet
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ QuestionSetInline]


# class TestAdmin(admin.ModelAdmin):
#     filter_horizontal = ('question',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name' , 'question_count']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(question_count=models.Count('question'))
        return queryset

    def question_count(self, obj):
        return obj.question_count

    question_count.admin_order_field = 'question_count'
    question_count.short_description = 'Question Count'
  
admin.site.register(Topic,TopicAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Test)
