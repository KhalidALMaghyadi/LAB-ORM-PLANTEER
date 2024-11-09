from django.urls import path
from . import views

app_name="plant"
# راح ارجعلها 
urlpatterns = [

    path('plants/new/', views.new_add_view, name='new_add_view'),
    path('plants/all/', views.all_plant_view, name='all_plant_view'),
    path('plants/<plant_id>/detail/', views.detail_plant_view , name='detail_plant_view'),
    path('plants/<plant_id>/update/', views.update_plant_view, name='update_plant_view'),
    path('plants/<plant_id>/delete/', views.delete_plant_view, name='delete_plant_view'),
    path('plants/search/' , views.search_plant_view, name="search_plant_view"),

]