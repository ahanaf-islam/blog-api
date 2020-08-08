from rest_framework import serializers

from .models import BlogPost

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

    author = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'blog_image', 'content', 'date_posted']
        extra_kwargs = {
            'author': {'read_only': True},
            'date_posted': {'read_only': True}
            }

    def get_username_from_author(self, blog_post):
        author = blog_post.author.username
        return author

