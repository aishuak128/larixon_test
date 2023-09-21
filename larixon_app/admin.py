from django.contrib import admin
from larixon_app.models import Category, City, Advert

admin.site.register(Category)
admin.site.register(City)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'visited')
    list_filter = ('city', 'category')

