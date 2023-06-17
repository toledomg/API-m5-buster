from django.shortcuts import render
from rest_framework.views import APIView, Request, Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsUserEmployeeOrReadOnly
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from utils import *


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserEmployeeOrReadOnly]

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, req, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)

        return Response(serializer.data, 201)
        # return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserEmployeeOrReadOnly]

    def get(self, req: Request, movies_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movies_id)
        serializer = MovieSerializer(movie)

        return ResponseMethods.response_success(200, serializer.data)

    def delete(self, req: Request, movies_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movies_id)

        movie.delete()

        return ResponseMethods.response_success(204)

    
class MovieOrder(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movies_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movies_id)

        serializer = MovieOrderSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user, movie=movie)

        return ResponseMethods.response_success(201, serializer.data)
