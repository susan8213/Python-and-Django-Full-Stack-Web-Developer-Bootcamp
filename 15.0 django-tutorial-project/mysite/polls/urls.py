from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # views.index
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # views.detail
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # views.results
    path('<int:pk>/vote/', views.vote, name='vote'),
]