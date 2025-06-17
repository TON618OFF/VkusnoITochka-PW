from .views import *
from rest_framework import routers
urlpatterns = [

]

router = routers.SimpleRouter()
router.register('dish', DishViewSet, basename='dish')
router.register('orderitem', OrderItemViewSet, basename='orderitem')
router.register('order', OrderViewSet, basename='order')
router.register('category', CategoryViewSet, basename='category')
router.register('promotion', PromotionViewSet, basename='promotion')
router.register('contact', ContactViewSet, basename='contact')
router.register('userprofile', UserProfileViewSet, basename='userprofile')
router.register('delivery', DeliveryViewSet, basename='delivery')
urlpatterns += router.urls