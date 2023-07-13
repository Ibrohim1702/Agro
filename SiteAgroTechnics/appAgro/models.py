from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, blank=True, max_length=256)
    is_menu = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)

        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


d = [
    ("Tashkent", "Farg'ona"),
    ("Namangan", "Andijon"),
    ("Marg'ilon", "Sirdaryo"),
    ("Qashqadaryo", "Jizzah"),
    ("Samarqand", "Buxoro"),
    ("Qoraqalpoqiston", "Navoiy"),

]


class Product(models.Model):

    price = models.IntegerField()
    vil = models.CharField(max_length=128, choices=d)
    date = models.DateField(auto_now_add=True)
    compain = models.CharField(max_length=64)
    short_description = models.CharField(max_length=256)
    quvvati = models.CharField(max_length=25)
    silindr = models.IntegerField()
    karobka = models.CharField(max_length=5)
    tezlik = models.CharField(max_length=25)
    gildirak = models.CharField(max_length=6)
    yoqilgi = models.IntegerField()
    uzunlik = models.IntegerField()
    kenglik = models.IntegerField()
    tepalik = models.IntegerField()
    akumlyator = models.CharField(max_length=6)
    telefon = models.CharField(max_length=15)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.compain


class ProdImg(models.Model):
    img = models.ImageField()
    prod = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)



