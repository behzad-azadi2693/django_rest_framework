from comments.models import Comment
from rest_framework.serializers import (
                    HyperlinkedIdentityField, SerializerMethodField, ModelSerializer
        )


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'parent', 'content']
