from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class FoodItem(models.Model):

    name = models.CharField(_("Name"), max_length=255, null=False, blank=False)
    slug = models.SlugField(_("Slug"), unique=True, null=False, blank=False)

    calories_per_100g = models.PositiveIntegerField(_("Calories/100g"), default=0)
    protein_per_100g = models.PositiveIntegerField(_("Protein/100g"), default=0)
    carb_per_100g = models.PositiveIntegerField(_("Carb/100g"), default=0)
    fats_per_100g = models.PositiveIntegerField(_("Fats/100g"), default=0)

    class Meta:
        verbose_name = _("Food Item")
        verbose_name_plural = _("Food Items")

    def __str__(self):
        return f"{self.name}, {self.slug} - prt: {self.protein_per_100g}, \
fts: {self.fats_per_100g}, crb: {self.carb_per_100g}, clr: {self.calories_per_100g}"

    def get_absolute_url(self):
        return reverse("FoodItem_detail", kwargs={"slug": self.slug})
