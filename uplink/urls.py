from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

app_name = "uplink"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("account", views.account, name="account"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("user/<str:name>", views.profile, name="profile")
]

handler404 = views.error_404_view
handler500 = views.error_500_view