from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import UserRegisterSerializer, UserListSerializer
from .models import User


class UserRegisterView(APIView):
    """
    Register a new user.
    Accessible without authentication.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    """
    View to list all users.
    Only accessible by admin users.
    """
    permission_classes = [IsAdminUser]
    serializer_class = UserListSerializer
    queryset = User.objects.all()
