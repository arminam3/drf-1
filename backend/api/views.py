from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

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
from rest_framework.viewsets import ModelViewSet

from blog.models import Article
from api.serializers import ArticleSerializer, UserSerializer
from .permissions import (
                        IsSuperUser,
                        IsSuperUserOrStaffReadOnly,
                        IsAuthorOrReadOnly,
                        IsStaffOrReadOnly,
                        IsSuperuserOrStaffReadOnly
                        )

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsSuperUserOrStaffReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


