from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, RetrieveUpdateAPIView, \
    CreateAPIView

from src.accounts.models import Profile
from src.accounts.serializers import ProfileSerializer


# Create your views here.
class CreateProfile(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_context(self):
        print(self.request.user.id)
        return {'user': self.request.user.id}


class ProfileRUDView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()

    def get_object(self):
        return Profile.objects.get(user=self.request.user.id)

    def get_serializer_class(self):
        return ProfileSerializer
