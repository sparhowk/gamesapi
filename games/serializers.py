from rest_framework import serializers
from games.models import GameCategory
from games.models import Game
from games.models import Player
from games.models import PlayerScore
import gmes.view


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail')
    
    
    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games')


class GameSerializer(serializers.ModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(),
                                                 slug_field='name' )
    
    
    class Meta:
        model = Game
        fields = ('url',
                  'game_category'
                  'name',
                  'release_date',
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
