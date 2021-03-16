from rest_framework import generics
from .models import Message
from .serializers import InitializeMessageSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class StartMessaging(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = InitializeMessageSerializer
    permission_classes = [IsAuthenticated]


# class MessageActivities(generics.RetrieveUpdateAPIView):
#     pass