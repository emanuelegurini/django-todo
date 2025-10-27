from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(["GET"])
@permission_classes([AllowAny])
def task_list(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
