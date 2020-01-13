from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import CreditProductsView, FilterProductView, CreditProductView


router = SimpleRouter()
router.register('products', CreditProductsView, basename='CreditProducts')
router.register('filter', FilterProductView, basename='FilterProduct')
router.register('product', CreditProductView, basename='CreditProduct')

urlpatterns = router.urls
