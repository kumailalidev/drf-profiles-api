from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# Creating a router
router = DefaultRouter()

# Registering a HelloViewSet with router
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")

# Registering a UserProfileViewSet with router
# NOTE: basename is not required because it is automatically configured by DRF
#       UserProfileViewSet has a queryset model UserProfile, basename is same
#       as queryset model name.
router.register("profile", views.UserProfileViewSet)

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginAPIView.as_view()),
    path("", include(router.urls)),
]
