from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from .serializers import SignupSerializer



class SignupView(APIView):

    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "User created"
            })

        return Response(serializer.errors)



# TEMPORARY DEBUG VIEW
class DebugUserView(APIView):

    def get(self, request):

        users = User.objects.values(
            "username",
            "is_active"
        )

        return Response(
            list(users)
        )