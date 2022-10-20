from django.db import models

#Tabla abstracta
class ModelDefault(models.Model):
    status = models.BooleanField(null=False,default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


#tabla de cliente y mesa
class Client(ModelDefault):
    name_client =  models.CharField(max_length=30)
    status = models.BooleanField(null=False,default=True)

    def __str__(self) -> str:
        return self.name_client

    class Meta:
        db_table = 'client'
        ordering = ['id']
        verbose_name = "Client"
        verbose_name_plural = "Customers"
    

class TableFood(ModelDefault):
    name_table_flood = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name_table_flood

    class Meta:
        db_table = 'table_food'
        ordering = ['id']
        verbose_name = "TableFlood"
        verbose_name_plural = "TableFloods"
    

#tablas de producto       
class Category(ModelDefault):
    name_category = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name_category
    
    class Meta:
        db_table = 'category'
        ordering = ['id']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(ModelDefault):
    name_product = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    client = models.ManyToManyField(Client,through='FoodMenu',blank=True)

    def __str__(self) -> str:
        return self.name_product

    class Meta:
        db_table = 'product'
        ordering = ['id']
        verbose_name = "Product"
        verbose_name_plural = "Products"

#tabla de menus
class FoodMenu(ModelDefault):
    description_food_menu = models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    tablefood = models.ForeignKey(TableFood,on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.description_food_menu

    class Meta:
        db_table = 'food_menu'
        ordering = ['id']
        verbose_name = "FoodMenu"
        verbose_name_plural = "FoodMenus"