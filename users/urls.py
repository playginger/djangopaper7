from django.urls import include, path
from rest_framework import routers
from .apps import UsersConfig
from .views import HabitViewSet, register, login, habits_list, public_habits_list, create_habit, edit_habit, \
    delete_habit

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('habits/', habits_list, name='habits_list'),
    path('public_habits/', public_habits_list, name='public_habits_list'),
    path('habits/create/', create_habit, name='create_habit'),
    path('habits/edit/<int:habit_id>/', edit_habit, name='edit_habit'),
    path('habits/delete/<int:habit_id>/', delete_habit, name='delete_habit'),
]
