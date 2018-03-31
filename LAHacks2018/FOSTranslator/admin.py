from django.contrib import admin
from .models import Idiom

class IdiomAdmin(admin.ModelAdmin):
    list_display = ('idiom',
                    'definition',)

    list_filter = ['idiom',]

    search_fields = ['idiom', 'definition',]





admin.site.register(Idiom, IdiomAdmin)
