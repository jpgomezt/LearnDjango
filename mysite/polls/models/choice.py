from django.core.exceptions import ValidationError
from django.db import models


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:        
        db_table = 'choice'

    def __str__(self):
        return self.choice_text