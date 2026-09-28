from django.contrib.auth.views import redirect_to_login


def login_not_required(view_func):
    """Mark a view as reachable without logging in (e.g. the login page)."""
    view_func.login_required = False
    return view_func


class LoginRequiredMiddleware:
    """Send anonymous users to the login page (settings.LOGIN_URL) for every
    view that isn't marked with @login_not_required.

    Same idea as Django 5.1's LoginRequiredMiddleware (and the same view
    attribute), kept here so it also works on older Django versions.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated or not getattr(view_func, 'login_required', True):
            return None
        if request.path_info.startswith('/admin/'):
            return None  # the admin has its own login page
        return redirect_to_login(request.get_full_path())
