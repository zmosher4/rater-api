from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import GameImage, Game
import uuid
import base64
from django.core.files.base import ContentFile


class GameImageSerializer(serializers.ModelSerializer):
    action_pic_url = serializers.SerializerMethodField()

    class Meta:
        model = GameImage
        fields = ['id', 'game', 'action_pic', 'action_pic_url']

    def get_action_pic_url(self, obj):
        request = self.context.get('request')
        if obj.action_pic and request:
            return request.build_absolute_uri(obj.action_pic.url)
        return None


class GameImageViewSet(viewsets.ModelViewSet):
    queryset = GameImage.objects.all()
    serializer_class = GameImageSerializer

    def create(self, request):
        game_picture = GameImage()

        # Fetch the game instance using game_id
        try:
            game = Game.objects.get(id=request.data["game_id"])
        except Game.DoesNotExist:
            return Response(
                {"error": "Game not found."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Set the game field of GameImage
        game_picture.game = game

        # Handle the image data
        format, imgstr = request.data["game_image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(
            base64.b64decode(imgstr),
            name=f'{request.data["game_id"]}-{uuid.uuid4()}.{ext}',
        )

        game_picture.action_pic = data

        try:
            game_picture.save()
            serializer = GameImageSerializer(game_picture, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response({"error": str(ex)}, status=status.HTTP_400_BAD_REQUEST)
