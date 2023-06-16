from .models import User, Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_2']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_2 = attrs.get('password_2')
        if password_2 != password:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        try:
            author = Author.objects.create(
                user=user
            )
        except Exception as error:
            user.delete()
            raise error
        else:
            author.username = user.username
            author.email = user.email
        return author


class UserSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['email', 'username', 'password', 'password_2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_2 = attrs.get('password_2')
        if password_2 != password:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        return user
