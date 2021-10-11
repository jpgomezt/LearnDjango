from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view.index, name='home.index'),
    path('question/', question_view.index, name='question.index'),
    # ex: /polls/question/5/
    path('question/<int:question_id>/', question_view.detail, name='question.detail'),
    # ex: /polls/question/5/results/
    path('question/<int:question_id>/results/', question_view.results, name='question.results'),
    # ex: /polls/question/5/vote/
    path('question/<int:question_id>/vote/', question_view.vote, name='question.vote'),
]