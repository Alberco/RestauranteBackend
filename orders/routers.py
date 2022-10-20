from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'users',views.ClientModelViewSet,basename='client')
router.register(r'table_food',views.TableFoodModelViewSet,basename='table_food')
router.register(r'category',views.CategoryModelViewSet,basename='category')
router.register(r'product',views.ProductModelViewSet,basename='product')
router.register(r'food_menu',views.FoodMenuModelViewSet,basename='food_menu')

urlpatterns = router.urls
