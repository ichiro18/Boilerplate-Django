from django.urls import re_path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

schema_view = get_swagger_view(title="API")

urlpatterns = [
    re_path(r'^$', schema_view),
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls'), name="rest_framework")
]
