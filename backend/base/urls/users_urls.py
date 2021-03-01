from django.urls import path

from base.views.user_views import MyTokenObtainPairView, get_user_profile, get_users, register_user

urlpatterns = [
    path("users/login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/register/", register_user, name="user_register"),
    path("users/profile/", get_user_profile, name="users_profile"),
    path("users/", get_users, name="users"),
]
