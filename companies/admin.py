from django.contrib import admin

from .models import Company, Employee, Opening

# Register your models here.


class EmployeeTabularInline(admin.StackedInline):
    model = Employee
    extra = 1
    max_num = 1


class OpeningTabularInline(admin.StackedInline):
    model = Opening
    extra = 1
    max_num = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        EmployeeTabularInline,
        OpeningTabularInline,
    ]

    class Meta:
        model = Company

admin.site.register(Company, CompanyAdmin)
# admin.site.register(Employee)
# admin.site.register(Opening)

