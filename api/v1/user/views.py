from rest_framework import serializers, generics, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models import UserProfile
from api.permissions import *
from api.serializer import *
from api.v1.core.serializers import CompanyDepartmentsSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    #department = UUIDRelatedField()

    class Meta:
        model = UserProfile
        fields = ('user_id', 'phone', 'home_phone', 'work_phone', 'department', 'id')


class UserProfileNestedSerializer(serializers.ModelSerializer):
    department = CompanyDepartmentsSerializer(many=False)

    class Meta:
        model = UserProfile
        serializer_class = UserProfileSerializer
        fields = ('user_id', 'phone', 'home_phone', 'work_phone', 'department', 'id')


class UserProfileNestedList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileNestedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserProfileNestedDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                              generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileNestedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'is_superuser', 'user_profile')
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class UserNestedSerializer(serializers.ModelSerializer):
    user_profile = UserProfileNestedSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'is_superuser', 'user_profile')
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserNestedSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=False)
    #password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',
                  'user_profile')
        #write_only_fields = ('password',)

    # def restore_object(self, attrs, instance=None):
    #     # call set_password on user object. Without this
    #     # the password will be stored in plain text.
    #     user = super(UserDetailSerializer, self).restore_object(attrs, instance)
    #     try:
    #         user.set_password(attrs['password'])
    #     except KeyError:
    #         pass
    #     return user


class UserList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserNestedList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserNestedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                 generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GetUserByToken(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk is None:
            return Response(UserSerializer(request.user).data)
        return super(GetUserByToken, self).retrieve(request, pk)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)