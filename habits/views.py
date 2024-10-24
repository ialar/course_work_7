from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    # permission_classes = (IsAuthenticated,)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
