from django.urls import path
from . import views

app_name = 'idea'

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('new/', views.idea_new, name='idea_new'),
    path('edit/<int:pk>/', views.idea_edit, name='idea_edit'),
    path('delete/<int:pk>/', views.idea_delete, name='idea_delete'),
]
