from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user"]
        extra_kwargs = {"id": {"read_only": True}}
        # linha de cima = linha de baixo (mais prático), principalmente quando tem mais de um campo
        # read_only_fields = ["id"]
