from rest_framework import serializers
from viewer.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']
        read_only_fields = ['id']


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'rating', 'released']
        read_only_fields = ['id']
        depth = 1


class MovieRetreiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'rating', 'released', 'description', 'created']
        read_only_fields = ['id','created']
        depth = 1
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=128)
    # genre = serializers.CharField(max_length=128)
    # rating = serializers.IntegerField(max_value=10)
    # released = serializers.DateField()
    # description = serializers.CharField(required=False, allow_blank=True)
    # created = serializers.DateTimeField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.genre = validated_data.get('genre', instance.genre)
    #     instance.rating = validated_data.get('rating', instance.rating)
    #     instance.released = validated_data.get('released', instance.released)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance