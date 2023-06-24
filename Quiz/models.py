
from django.db import models

from myauth.models import User,Basemodel

'''

'''

class Topic(Basemodel):
    name =  models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Question(Basemodel):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE )
    question = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question

class Option(Basemodel):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class QuestionSet(Basemodel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option,on_delete=models.CASCADE)
    is_true = models.BooleanField(default= False)

    def __str__(self) -> str:
        return self.question.question
    
class Test(Basemodel):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    total_question = models.PositiveSmallIntegerField(default=10)
    score = models.PositiveSmallIntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    def __str__(self) -> str:
        return self.user.username