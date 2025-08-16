from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "djangoapp"
urlpatterns = [
    # Path for registration.
    path(route="register", view=views.registration, name="register"),
    # Path for login.
    path(route="login", view=views.login_user, name="login"),
    # Path for logout.
    path(route="logout", view=views.logout_request, name="logout"),
    # Path for dealer reviews view.
    # Path for add a review view.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
