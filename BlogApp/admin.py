from django.contrib import admin
from .models import Tag, Blog, Contact

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Contact)