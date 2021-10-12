from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    """ Model for Author """
    name = models.CharField(verbose_name="Nom de l'auteur",
                            blank=False,
                            max_length=100)

    def __str__(self):
        return self.name


class Categorie(models.Model):
    """ Model for Category """
    name = models.CharField(
        verbose_name='Categorie',
        max_length=30,
        serialize=True,
        blank=False,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    """ Model for Post """
    title = models.CharField(
        verbose_name='titre',
        max_length=60,
        serialize=True,
    )
    subtitle = models.CharField(
        verbose_name='sous-titre',
        max_length=150,
        serialize=True,
    )
    content = models.TextField(verbose_name='content', blank=False)
    creat_at = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    categories = models.ManyToManyField(Categorie, verbose_name='categories')
    author = models.ManyToManyField(
        Author,
        verbose_name='auteur',
        related_name='related_name',
    )

    def get_categories(self):
        return self.categories.all()

    def get_authors(self):
        return self.author.all()

    def __str__(self):
        return self.title


