from django.urls import path

from . import views

app_name = 'wxapp'
'''
urlpatterns = [
    # ex: /wxapp/
    path('', views.index, name='index'),
    # ex: /wxapp/5/
    path('<int:pk>/', views.detail, name='detail'),
    # ex: /wxapp/5/results/
    path('<int:pk>/results/', views.results, name='results'),
    # ex: /wxapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
'''
'''使用django通用模板'''
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('service',views.service,name='service'),
]