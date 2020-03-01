import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    published_date = models.DateTimeField()

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.published_date >= (now - datetime.timedelta(days=1))

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
