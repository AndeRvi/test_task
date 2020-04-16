from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='alpha v0.1',
      description="Looking forward to the future",
      contact=openapi.Contact(email="v.sripnik@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
