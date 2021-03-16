from comments.models import Comment
from rest_framework.serializers import (
                    HyperlinkedIdentityField, SerializerMethodField, ModelSerializer
        )


class CommentSerializers(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'parent', 'content', 'reply_count']

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentChildSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'timestamp']


class CommentDetailSerializers(ModelSerializer):
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'content', 'replies']

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializers(obj.children(), many=True).data
        return None
