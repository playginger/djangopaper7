from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import HabitViewSet, register, habits_list, public_habits_list, create_habit, edit_habit, \
    delete_habit

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('register/', register, name='register'),
    path('habits/', habits_list, name='habits_list'),
    path('public_habits/', public_habits_list, name='public_habits_list'),
    path('habits/create/', create_habit, name='create_habit'),
    path('habits/edit/<int:habit_id>/', edit_habit, name='edit_habit'),
    path('habits/delete/<int:habit_id>/', delete_habit, name='delete_habit'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
