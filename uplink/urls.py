from django.urls import path
from . import views

app_name = "uplink"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("account", views.account, name="account"),
    path("logout", views.logout_view, name="logout"),
    path("user/<str:name>", views.profile, name="profile")
]