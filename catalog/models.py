from django.db import models

from cloudinary.models import CloudinaryField


class Product(models.Model):
    class Section(models.TextChoices):
        HOMBRE = "hombre", "Hombre"
        MUJER = "mujer", "Mujer"
        ACCESORIOS = "accesorios", "Accesorios"

    name = models.CharField("Nombre", max_length=200)
    section = models.CharField(
        "Sección", max_length=20, choices=Section.choices
    )
    price = models.DecimalField(
        "Precio", max_digits=10, decimal_places=2
    )
    image = CloudinaryField("Imagen", folder="product_images", null=True, blank=True)
    active = models.BooleanField("Visible", default=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["section", "created_at"]

    @property
    def image_large_url(self):
        if not self.image:
            return ""
        return self.image.build_url(width=1400, crop="limit")

    def __str__(self):
        return self.name