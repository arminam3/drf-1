from django.urls import reverse_lazy
from django.contrib.auth.models import User

from rest_framework.generics import (
                                    ListCreateAPIView, 
                                    RetrieveUpdateAPIView, 
                                    RetrieveAPIView,\
                                    RetrieveUpdateDestroyAPIView
                                    )
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView

from blog.models import Article
from api.serializers import ArticleSerializer, UserSerializer
from .permissions import (
                        IsSuperUser,
                        IsSuperUserOrStaffReadOnly,
                        IsAuthorOrReadOnly,
                        IsStaffOrReadOnly,
                        IsSuperuserOrStaffReadOnly
                        )


class ArticleListApi(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (BasicAuthentication,)

class ArticleDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Article
    serializer_class = ArticleSerializer
    # lookup_field = "slug"
    permission_classes = [IsAuthorOrReadOnly]

class UserListApi(ListCreateAPIView):
    def get_queryset(self):
        self.request.auth                       # type: ignore
        return User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)

class UserDetailApi(RetrieveUpdateAPIView):
    queryset = User
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)        


class RevokeTokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        self.request.auth.delete()
        return Response({"msg": "Token deleted"}, status=201)