from django.db import models
from django.urls import reverse

# Create your models here.

# Note that parens are optional if not inheriting from another class


class Accessory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accs_detail', kwargs={'pk': self.id})


class Deck(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    printing_company = models.CharField(max_length=100)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return(f"{self.name}")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'deck_id': self.id})


class Extra(models.Model):
    name = models.CharField(max_length=50)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
