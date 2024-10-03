from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers, permissions
from .users import UserSerializer
from raterapi.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ['id', 'rating', 'game', 'user', 'is_owner']
        read_only_fields = ['user']

    def get_is_owner(self, obj):
        # Check if the user is the owner of the review
        return self.context['request'].user == obj.user


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request):
        rating = request.data.get('rating')
        game_id = request.data.get('gameId')

        rating = Rating.objects.create(
            user=request.user, rating=rating, game_id=game_id
        )
        rating.save()

        try:
            # Serialize the objects, and pass request as context
            serializer = RatingSerializer(rating, context={'request': request})
            # Return the serialized data with 201 status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
