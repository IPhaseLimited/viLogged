from rest_framework import serializers, generics, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.models import UserProfile, CompanyDepartments
from api.permissions import *
from api.serializer import *
from api.v1.core.serializers import CompanyDepartmentsSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    department = UUIDRelatedField()

    class Meta:
        model = UserProfile
        fields = ('user_id', 'phone', 'home_phone', 'work_phone', 'department', 'id', 'gender', 'image')
        filter_fields = ('phone', 'home_phone', 'work_phone', 'gender')


class UserProfileNestedSerializer(serializers.ModelSerializer):
    department = CompanyDepartmentsSerializer(many=False)

    class Meta:
        model = UserProfile
        serializer_class = UserProfileSerializer
        fields = ('user_id', 'phone', 'home_phone', 'work_phone', 'department', 'id', 'gender', 'image')
        filter_fields = ('phone', 'home_phone', 'work_phone', 'gender')


class UserProfileNestedList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileList(generics.ListAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'is_superuser', 'user_profile')
        filter_fields = ('username', 'email',)
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
        filter_fields = ('username', 'email',)
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
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('username', 'email', 'user_profile__phone', 'user_profile__work_phone', 'user_profile__home_phone')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserNestedList(generics.ListAPIView, mixins.CreateModelMixin):
    model = User
    serializer_class = UserNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('username', 'email', 'user_profile__phone', 'user_profile__work_phone', 'user_profile__home_phone')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserProfileImportSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user_id', 'phone', 'home_phone', 'work_phone', 'department', 'id', 'gender', 'image')
        filter_fields = ('phone', 'home_phone', 'work_phone', 'gender')


class UserImportSerializer(serializers.ModelSerializer):
    user_profile = UserProfileImportSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'is_superuser', 'user_profile')
        filter_fields = ('username', 'email',)
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserImportSerializer, self).restore_object(attrs, instance)

        user.set_password(attrs['password'])
        return user


class UserImport(generics.ListAPIView, mixins.CreateModelMixin):
    model = User
    serializer_class = UserImportSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                 generics.GenericAPIView, mixins.CreateModelMixin):
    model = User
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):

        try:
            return self.update(request, *args, **kwargs)
        except:
            user_profile = request.DATA.get('user_profile')
            try:
                department = user_profile['department']
            except KeyError:
                department = None

            user_id = User.objects.get(id=request.DATA.get('id'))
            department = CompanyDepartments.objects.get(uuid=department)
            new_profile = UserProfile(
                phone=user_profile['phone'],
                work_phone=user_profile['work_phone'],
                home_phone=user_profile['home_phone'],
                gender=user_profile['gender'],
                department=department,
                user_id=user_id
            ).save()
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetUserByToken(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk is None:
            return Response(UserSerializer(request.user).data)
        return super(GetUserByToken, self).retrieve(request, pk)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)