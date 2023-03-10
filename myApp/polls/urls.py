from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/hasil/', views.HasilView.as_view(), name='hasil'),
    path('<int:pertanyaan_id>/suara/', views.suara, name='suara'),
    
]
