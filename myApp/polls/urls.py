from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pertanyaan_id>/', views.detail, name='detail'),
    path('<int:pertanyaan_id>/hasil/', views.hasil, name='hasil'),
    path('<int:pertanyaan_id>/suara/', views.suara, name='suara'),
    
]
