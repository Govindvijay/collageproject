from . import views
from django.urls import path
app_name='collageapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_details, name='form_details'),
    path('message/', views.message, name='message'),
    path('index1/', views.index1, name='index1'),

]
