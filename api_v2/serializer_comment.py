from comments.models import Comment
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['user', 'content']

    def get_user(self, obj):
        return obj.user.username