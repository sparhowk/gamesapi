from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id',
                  'name',
                  'release_date',
                  'game_category',
                  'played'
                  )

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.relase_date = validated_data('release_date', instance.release_date)
        instance.game_category = validated_data('game_category', instance.game_category)
        instance.played = validated_data('played', instance.played)
        instance.save()
