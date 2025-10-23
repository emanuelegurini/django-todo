from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

"""
In Django la view ha lo stesso ruolo del controller nel pattern MVC (in pattern usiamo MTV).
Quindi la view e una funzione che riceve le richieste e restituisce le risposte. 

https://www.programmareinpython.it/blog/che-cosa-rende-django-speciale-miglior-web-framewo/
"""


@api_view(["GET"])
def users_list(request):
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def add_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
