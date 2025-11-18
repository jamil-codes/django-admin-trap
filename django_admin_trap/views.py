import time
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views import generic

from .forms import AdminTrapForm


class AdminTrapView(generic.FormView):
    """
    The ultimate admin trap view - mimics admin login perfectly!
    """

    template_name = "admin_trap/login.html"
    form_class = AdminTrapForm
    start_time = None

    def dispatch(self, request, *args, **kwargs):
        self.start_time = time.time()

        # Ensure consistent URL ending
        if not request.path.endswith("/"):
            return redirect(f"{request.path}/", permanent=True)

        # Handle redirects to explicit login view
        login_url = reverse("admin_trap:login")
        if request.path != login_url:
            return redirect_to_login(request.get_full_path(), login_url)

        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add admin site context for perfect disguise
        admin_site_context = AdminSite().each_context(self.request)

        # Get the username for authenticated users
        username = None
        if self.request.user.is_authenticated:
            username = self.request.user.get_username()

        context.update(
            {
                **admin_site_context,
                "app_path": self.request.get_full_path(),
                REDIRECT_FIELD_NAME: reverse("admin_trap:index"),
                "title": _("Log in"),
                "site_title": admin_site_context.get(
                    "site_title", _("Django administration")
                ),
                "site_header": admin_site_context.get(
                    "site_header", _("Django administration")
                ),
                # Add user information for the template
                "user": self.request.user,
                "username": username,
            }
        )

        return context

    def form_valid(self, form):
        # Always treat as invalid to maintain the trap
        return self.form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
