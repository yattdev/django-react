from django.contrib import admin
from weblog import models as m

# Register your models here.

admin.site.register(m.Categorie)
admin.site.register(m.Author)
admin.site.register(m.Post)
