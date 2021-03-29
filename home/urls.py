from django.urls import path
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='home/home.html'), name='home')
]