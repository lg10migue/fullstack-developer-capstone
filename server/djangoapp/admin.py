from django.contrib import admin

from .models import CarMake, CarModel

# Register your models here.

admin.site.register(CarMake)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    raw_id_fields = ("car_make",)
