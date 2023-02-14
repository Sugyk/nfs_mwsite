from django.contrib import admin
from .models import  Car, Brand, Profile, CarInfo, CarNote, CarImage
from django.conf import settings
from django.contrib.auth.models import User


class UserInline(admin.TabularInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserInline
    ]


admin.site.register(Car)
admin.site.register(Brand)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(CarInfo)
admin.site.register(CarNote)
admin.site.register(CarImage)

