from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnBlog(BasePermission):
    """Allow users to update their own status"""
    message = 'You must be the owner of the object'

    def has_object_permission(self,request,view,obj):
        """Check the user is trying to update their own status"""
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author.id == request.user.id
