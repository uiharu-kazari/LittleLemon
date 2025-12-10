from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    path("", views.index, name="home"),
    path("api/", include(router.urls)),
    path("api/register/", views.UserRegisterView.as_view(), name="register"),
    path("api/login/", views.UserLoginView.as_view(), name="login"),
]
