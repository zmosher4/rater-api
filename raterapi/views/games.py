from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Game
from .categories import CategorySerializer


class GameSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True)

    def get_is_owner(self, obj):
        # Check if the authenticated user is the owner
        return self.context['request'].user == obj.user

    class Meta:
        model = Game
        fields = [
            'id',
            'title',
            'designer',
            'number_of_players',
            'game_length_hrs',
            'age_rec',
            'is_owner',
            'year_released',
            'categories',
        ]


class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            title = request.data.get('title')
            designer = request.data.get('designer')
            year_released = request.data.get('year_released')
            number_of_players = request.data.get('number_of_players')
            game_length_hrs = request.data.get('game_length_hrs')
            age_rec = request.data.get('age_rec')

            game = Game.objects.create(
                user=request.user,
                title=title,
                designer=designer,
                year_released=year_released,
                number_of_players=number_of_players,
                game_length_hrs=game_length_hrs,
                age_rec=age_rec,
            )

            category_ids = request.data.get('categories', [])
            game.categories.set(category_ids)

            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# Title
# Designer
# Year released
# Number of players
# Estimated time to play
# Age recommendation
# Categories
