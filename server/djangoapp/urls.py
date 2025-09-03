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
    # Path for get cars view.
    path(route="get_cars", view=views.get_cars, name="getcars"),
    # Path for get dealers.
    path(route="get_dealers/", view=views.get_dealerships, name="get_dealers"),
    path(
        route="get_dealers/<str:state>",
        view=views.get_dealerships,
        name="get_dealers_by_state",
    ),
    path(
        route="dealer/<int:dealer_id>",
        view=views.get_dealer_details,
        name="dealer_details",
    ),
    # Path for dealer reviews view.
    path(
        route="reviews/dealer/<int:dealer_id>",
        view=views.get_dealer_reviews,
        name="dealer_reviews",
    ),
    # Path for add a review view.
    path(route="add_review", view=views.add_review, name="add_review"),
    # Path for get inventory view.
    path(
        route="get_inventory/<int:dealer_id>",
        view=views.get_inventory,
        name="get_inventory",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
