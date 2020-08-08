from rest_framework.pagination import (
    #LimitOffsetPagination,
    PageNumberPagination
)


"""class BlogPostLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10"""

class BlogPostPagination(PageNumberPagination):
    page_size = 7
