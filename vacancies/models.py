from django.db import models


# Create your models here.
class Vacancy(models.Model):
    STATUS = [
        ("drafts", "Черновик"),
        ("open", "Открыта"),
        ("close", "Закрыта"),
    ]
    slug = models.SlugField(50)
    text = models.CharField(max_length=2000)
    status = models.CharField(max_length=6, choices=STATUS, default="drafts")
    created = models.DateTimeField(auto_now_add=True)
