'''Polls URLs'''
from django.urls import path
from .views import home_view, question_view

app_name = 'polls'
urlpatterns = [
    path('', home_view.index, name='home.index'),
    path('question/', question_view.IndexView.as_view(), name='question_index'),
    path('question/<int:pk>/', question_view.DetailView.as_view(), name='question_detail'),
    path('question/<int:pk>/results/', question_view.ResultsView.as_view(), name='question_results'),
    path('question/<int:question_id>/vote/', question_view.vote, name='question_vote'),
    #path('question/', question_view.index, name='question_index'),
    #path('question/<int:question_id>/', question_view.detail, name='question_detail'),
    #path('question/<int:question_id>/results/', question_view.results, name='question_results'),
    #path('question/<int:question_id>/vote/', question_view.vote, name='question_vote'),
]
