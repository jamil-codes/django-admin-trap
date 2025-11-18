from django.urls import path, re_path
from . import views

app_name = "admin_trap"

urlpatterns = [
    # Login page - the main trap
    path("login/", views.AdminTrapView.as_view(), name="login"),
    # Catch-all pattern for any admin URL - redirects to login trap
    re_path(r"^.*$", views.AdminTrapView.as_view(), name="index"),
]
