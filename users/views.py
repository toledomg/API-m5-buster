from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User
from utils import ResponseMethods
from .serializers import UserSerializer
from .permissions import IsUserOwnerOrAdmin


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return ResponseMethods.response_success(201, serializer.data)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwnerOrAdmin]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)

        serializer = UserSerializer(user)

        return ResponseMethods.response_success(200, serializer.data)

    def patch(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)

        serializer = UserSerializer(user, req.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return ResponseMethods.response_success(200, serializer.data)
