from django.urls import path
from posts.views import PostsListApiView, PostApiView, LikeApiView,\
    LikeStatsApiView


urlpatterns = [
    path(r'api/post', PostsListApiView.as_view()),
    path(r'api/post/<pk>', PostApiView.as_view()),
    path(r'api/post/<post_id>/like', LikeApiView.as_view()),
    path(r'api/like/stats', LikeStatsApiView.as_view()),
]
