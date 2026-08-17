from django.urls import path

from .views import CatalogView, HomeRedirectView

urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home"),
    path("<str:section>/", CatalogView.as_view(), name="catalog"),
]