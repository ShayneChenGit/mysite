from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'polls'
# urlpatterns = [
#     path('index/', views.index, name='index'),
#     url(r'^time/$', views.current_datetime),
#     url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
#     path('<int:question_id>/', views.details, name = 'detail'),
#     path('<int:question_id>/results/', views.results, name = 'results'),
#     path('<int:question_id>/vote/', views.vote, name = 'vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]