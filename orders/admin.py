from django.contrib import admin
from .models import Client,TableFood,Category,Product,FoodMenu

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name_product','price']

class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ['id','description_food_menu','product','client','tablefood','count']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name_category']

class TableFoodAdmin(admin.ModelAdmin):
    list_display = ['id','name_table_flood']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','name_client','status']


admin.site.register(Product,ProductAdmin)
admin.site.register(FoodMenu,FoodMenuAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(TableFood,TableFoodAdmin)
admin.site.register(Client,ClientAdmin)