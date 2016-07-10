from django.contrib import admin

# Register your models here.
from .models import Company, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display=('product','company','description','price','stock')

class CompanyAdmin(admin.ModelAdmin):
    display=('company')

admin.site.register(Product,ProductAdmin)
admin.site.register(Company,CompanyAdmin)
