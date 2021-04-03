from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from .serializer_user import UserDetailSerializer
from rest_framework.serializers import (
                    HyperlinkedIdentityField, SerializerMethodField, ModelSerializer,
                    ValidationError,
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

class CommentListSerializers(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:comment-detail'
    )
    reply_count = SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'reply_count', 'timestamp', 'url']

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class CommentChildSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'timestamp']


class CommentDetailSerializers(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    replies = SerializerMethodField()
    content_object_url = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['pk', 'content', 'replies', 'content_object_url', 'user']
        read_only_fields =['replies']

    def get_content_object_url(self, obj):
        return obj.get_api_url()

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializers(obj.children(), many=True).data
        return None

"""19 20 21
def create_comment_serializer(type='post', slug=None, parent_id=None):
    class CommentCreateSerializer(ModelSerializer):
        class Meta:
            model = Comment 
            fields = ['id','parent','content','timestamp']

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.slug = slug
            self.parentobj = None
            if self.parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count()==1:
                    self.parent_obj = parent_qs.first()
            return super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model=model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError("this is not a valid ")
            SomeModel = model_qs.first().model_class()
            obj_qs = SomeModel.objects.filter(slug=self.slug)
            if not obj_qs.exists() or obj_qs.count() != 1:
                raise ValidationError("this is not a slug for this content type")
            return data
"""