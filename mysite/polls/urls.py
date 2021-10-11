from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view.index, name='index'),
    # ex: /polls/question/5/
    path('question/<int:question_id>/', question_view.detail, name='detail'),
    # ex: /polls/question/5/results/
    path('question/<int:question_id>/results/', question_view.results, name='results'),
    # ex: /polls/question/5/vote/
    path('question/<int:question_id>/vote/', question_view.vote, name='vote'),
]