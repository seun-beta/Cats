from django.urls import path
from . import views 

app_name = 'cats'

urlpatterns = [
    path('', views.MainList.as_view(), name='main'),
    path('cat_list', views.CatList.as_view(), name='cat_list'),
    path('breed_list', views.BreedList.as_view(), name='breed_list'),
    path('create_cat', views.CreateCat.as_view(), name='create_cat'),
    path('update_cat/<int:pk>', views.UpdateCat.as_view(), name='update_cat'),
    path('delete_cat/<int:pk>', views.DeleteCat.as_view(), name='delete_cat'),
    path('create_breed', views.CreateBreed.as_view(), name='create_breed'),
    path('update_breed/<int:pk>', views.UpdateBreed.as_view(), name='update_breed'),
    path('delete_breed/<int:pk>', views.DeleteBreed.as_view(), name='delete_breed'),

]
