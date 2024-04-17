from django.urls import path
from keiba_app import views

app_name = 'keiba_app'
urlpatterns = [
    path('race/create/', views.create_race, name='create_race'),
    path('race/', views.read_race, name='read_race'),
]