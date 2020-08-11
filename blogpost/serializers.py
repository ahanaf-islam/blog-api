from rest_framework import serializers

from .models import BlogPost
from comments.serializers import CommentSerializer
from comments.models import Comment
from accounts.serializers import UserAccountsSerializer

#This serializer for list of blog
class BlogPostListSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField('get_username_from_author')
    detail_url = serializers.HyperlinkedIdentityField(view_name='detailAPI')

    class Meta:
        model = BlogPost
        fields = ['title', 'detail_url', 'author', 'content', 'date_posted']

    def get_username_from_author(self, blog_post):
        author = blog_post.author.username
        return author


#This serializer for Blog's detail view
class BlogPostDetailSerializer(serializers.ModelSerializer):
    author = UserAccountsSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'author',
            'title',
            'slug',
            'content',
            'blog_image',
            'comments',
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments
