from django.contrib import admin
from .models import FirstMaster, SecondMaster, ThirdMaster

# Register your models here.


class FirstMasterAdmin(admin.ModelAdmin):
    list_display = ("register_date", "surname", "name", "patronymic", "auto_mark")


class SecondMasterAdmin(admin.ModelAdmin):
    list_display = ("register_date", "surname", "name", "patronymic", "auto_mark")


class ThirdMasterAdmin(admin.ModelAdmin):
    list_display = ("register_date", "surname", "name", "patronymic", "auto_mark")


admin.site.register(FirstMaster, FirstMasterAdmin)
admin.site.register(SecondMaster, SecondMasterAdmin)
admin.site.register(ThirdMaster, ThirdMasterAdmin)