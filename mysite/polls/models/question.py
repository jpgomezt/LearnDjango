import datetime

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:        
        db_table = 'question'

    def __str__(self):
        return self.question_text

    def get_question_text(self):
        return self.question_text

    def get_pub_date(self):
        return self.pub_date

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now