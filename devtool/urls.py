from django.urls import path
from . import views

app_name = 'devtool'

urlpatterns = [
    path('', view=views.devtool_list, name='devtool_list'),
    path('<int:pk>/', view=views.devtool_detail, name='devtool_detail'),
    path('new/', views.devtool_new, name='devtool_new'),
    path('edit/<int:pk>/', views.devtool_edit, name='devtool_edit'),
    path('delete/<int:pk>/', views.devtool_delete, name='devtool_delete'),
]
