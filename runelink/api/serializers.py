from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from .fields import *


class SkillLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillLevels
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    skills = SkillLevelsSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "rsn",
            "date_joined",
            "skills",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(
            **validated_data
        )  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class GroupFinderSerializer(serializers.ModelSerializer):
    user = ForeignKeyField(queryset=CustomUser.objects.all(), serializer=CustomUserSerializer)

    class Meta:
        model = GroupFinder
        fields = ('id', 'body', 'activity', 'players_needed', 'time_posted', 'user')


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ParentSerializer(serializers.ModelSerializer):
    child = ForeignKeyField(queryset=Child.objects.all(), serializer=ChildSerializer)

    class Meta:
        model = Parent
        fields = "__all__"
