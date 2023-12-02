from django.urls import path, include
from . import views


app_name='shopapp'
urlpatterns = [

    path('',views.allProduct,name='allProduct'),
    path('<slug:c_slug>/',views.allProduct,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proDetail'),

]