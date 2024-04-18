from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters

from . import models
from . import serializers


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class FileListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.FileSerializer
    queryset =models.File.objects.all()


class FileUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.FileSerializer
    queryset =models.File.objects.all()


class FileGroupView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['group']


class FileShareView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            file = models.File.objects.get(pk=pk)
            if file.author != request.user:
                return Response({'error': 'You are not the owner of this file'}, status=status.HTTP_403_FORBIDDEN)
            sharing_users = request.data.get('sharing', [])
            file.sharing.set(sharing_users)
            file.save()
            return Response({'message': 'File shared successfully'})
        except models.File.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
