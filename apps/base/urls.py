from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^error/$',
        view=views.ErrorView.as_view(),
        name='error'
    ),
]
