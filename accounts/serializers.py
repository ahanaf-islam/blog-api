from rest_framework import serializers

from . import models


class UserAccountsSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    confirm_password = serializers.CharField(
        style={'input_type':'password'},
        write_only=True
    )


    class Meta:
        model = models.UserAccounts
        fields = ('id','email','username','password', 'confirm_password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserAccounts.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()

        return user

