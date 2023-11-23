from django.contrib import admin

from main.models import TestCategory, LabTest, Doctor


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time',)
    list_filter = ('name', 'price', 'time',)
    search_fields = ()
    list_per_page = 100
    list_editable = ['price']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('specialization', 'visit', 'price',)
    list_filter = ('specialization',)