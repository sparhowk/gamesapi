from rest_framework import serializers
from games.models import Game


class GameSerializers(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    relase_date = serializers.DataTimeField()
    game_category = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        return Game.object.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.relase_date = validated_data('relase_date', instance.relase_date)
