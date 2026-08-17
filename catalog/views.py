from django.http import Http404
from django.views.generic import ListView, RedirectView

from .models import Product


class CatalogView(ListView):
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "products"

    def dispatch(self, request, *args, **kwargs):
        section = self.kwargs.get("section", "")
        valid = ["nuevo"] + list(Product.Section.values)
        if section not in valid:
            raise Http404("Sección no encontrada")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        section = self.kwargs["section"]
        queryset = Product.objects.filter(active=True)
        if section == "nuevo":
            return queryset.order_by("-created_at")
        return queryset.filter(section=section)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_section"] = self.kwargs["section"]
        context["sections"] = [("nuevo", "Nuevo")] + list(Product.Section.choices)
        return context


class HomeRedirectView(RedirectView):
    url = "/nuevo/"
    permanent = False