from django.urls import path

from .views import TopicListView,TestView,FetchQuestion,ResultListView

from .views import TopicApiView,ResultApiView


urlpatterns = [
    path('',TopicListView.as_view() , name = 'topiclist'),
    path('t',TestView.as_view() , name = 'test'),
    path('result',ResultListView.as_view() , name = 'result'),


    # ajax urls
    path('q',FetchQuestion.as_view() , name = 'question'),

    # rest
    path('api',TopicApiView.as_view() , name = 'atopiclist'),
    path('api/r',ResultApiView.as_view() , name = 'aresult'),
    

]
