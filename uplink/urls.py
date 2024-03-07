from django.urls import path
from . import views

app_name = "uplink"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("account", views.account, name="account"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("account/edit-profile", views.edit_profile, name="edit_profile"),
    path("account/manage-links", views.manage_links, name="manage_links"),
    path("user/<str:name>", views.profile, name="profile")
]