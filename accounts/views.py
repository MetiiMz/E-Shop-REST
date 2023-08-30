from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response({'message': 'You have successfully registered'})
        return Response(srz_data.errors)
