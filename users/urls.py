from django.urls import include, path
from rest_framework import routers
from .apps import UsersConfig
from .views import HabitViewSet

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'habits', HabitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('habit/', HabitViewSet.as_view(), name='habit'),
]
