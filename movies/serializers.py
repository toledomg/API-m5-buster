from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices, default=RatingMovie.DEFAULT
    )

    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field="email",
        source="user",
    )

    def create(self, validate_data: dict) -> Movie:
        return Movie.objects.create(**validate_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field="title",
        source="movie"
    )

    # movies_title = serializers.SerializerMethodField()

    # def get_movies_title(self, obj: Movie):
    #     movies_title = [movie.title for movie in obj.movie.all()]
    #     if movies_title:
    #         return movies_title

    #     return "Título não encontrado."

    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    buyed_by = serializers.SlugRelatedField(
        read_only=True,
        slug_field="email",
        source="user",
    )

    def create(self, validate_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validate_data)
