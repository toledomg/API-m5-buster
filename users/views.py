from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from users.models import User
from .utils import ResponseMethods
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return ResponseMethods.response_success(201, serializer.data)
        # return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    pass
