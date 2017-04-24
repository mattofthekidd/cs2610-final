from django.conf.urls import url

from . import views

app_name = 'final'
urlpatterns = [
    #ex: /final/
    url(r'^$', views.ItemView.as_view(), name='final'),
    # #ex: /final/item/
    # url(r'^item/$', views.ItemView.as_view(), name='item'),
    # #ex: /polls/5/results/
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # #ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]