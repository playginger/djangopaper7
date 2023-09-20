from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .tasks import send_notification
from .models import Habit
from .serializers import HabitSerializer, UserSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class HabitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    # Здесь реализуем логику входа
    # Возвращаем токен доступа при успешном входе в систему
    ...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def habits_list(request):
    page = request.GET.get('page', 1)
    habits = Habit.objects.filter(user=request.user)
    serializer = HabitSerializer(habits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def public_habits_list(request):
    habits = Habit.objects.filter(is_public=True)
    serializer = HabitSerializer(habits, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_habit(request):
    serializer = HabitSerializer(data=request.data)
    if serializer.is_valid():
        habit = serializer.save(user=request.user)
        send_notification.delay(habit.id)  # Вызов функции send_notification с использованием delay()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_habit(request, habit_id):
    try:
        habit = Habit.objects.get(id=habit_id, user=request.user)
    except Habit.DoesNotExist:
        return Response({'error': 'Habit does not exist'}, status=404)
    serializer = HabitSerializer(habit, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_habit(request, habit_id):
    try:
        habit = Habit.objects.get(id=habit_id, user=request.user)
    except Habit.DoesNotExist:
        return Response({'error': 'Habit does not exist'}, status=404)
    habit.delete()
    return Response(status=204)
