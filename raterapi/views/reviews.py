from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers, permissions
from raterapi.models import Review
from .users import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ['id', 'comment', 'game', 'user', 'is_owner']
        read_only_fields = ['user']

    def get_is_owner(self, obj):
        # Check if the user is the owner of the review
        return self.context['request'].user == obj.user


class ReviewViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        # Get all reviews
        reviews = Review.objects.all()
        # Serialize the objects, and pass request to determine owner
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})

        # Return the serialized data with 200 status code
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        comment = request.data.get('comment')
        game_id = request.data.get('gameId')

        review = Review.objects.create(
            user=request.user,
            comment=comment,
            game_id=game_id,
        )
        review.save()

        try:
            # Serialize the objects, and pass request as context
            serializer = ReviewSerializer(review, context={'request': request})
            # Return the serialized data with 201 status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
