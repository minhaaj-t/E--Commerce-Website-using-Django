from django.urls import path

from ecommerceapp import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allcategories,name='allcategories'),
    path('<slug:c_slug>/', views.allcategories, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.productdetail, name='productcategorydetail'),

]