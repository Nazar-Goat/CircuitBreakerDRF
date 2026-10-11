from django.urls import path

from api.views import ServiceView

urlpatterns = [
    path(
        "service/",
        ServiceView.as_view(),
        name="service-create",
    ),
]