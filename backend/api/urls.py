from django.urls import path

from api.views import (
                        ArticleListApi, 
                        ArticleDetailApi, 
                        UserListApi,
                        UserDetailApi,
                        RevokeTokenView
                        )

app_name = "api"

urlpatterns = [
    path("", ArticleListApi.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailApi.as_view(), name="article_detail"),
    path("users/", UserListApi.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailApi.as_view(), name="user_detail"),
    path("revoke/", RevokeTokenView.as_view(), name="revoke_token"),
    ]