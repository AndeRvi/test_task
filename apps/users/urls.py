from django.conf.urls import url
from django.urls import path
from users.views import CreateUserView, PostsListApiView


urlpatterns = [
    url(r'^api/signup', CreateUserView.as_view()),
    path(r'api/user/<pk>', PostsListApiView.as_view()),
]