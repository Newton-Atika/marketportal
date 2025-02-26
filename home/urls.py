from .views import help,search,detail,home,shopping_list_view,add_to_shopping_list,update_shopping_list,download_shopping_list_as_pdf,delete_from_shopping_list,download_shopping_list_after_payment,shopping_list_detail
from django.urls import path

app_name='home'

urlpatterns = [
    path('', home, name='home'),
    path('help',help,name='help'),
    path('product/<int:pk>/',detail,name='detail'),
    path('search/',search,name='search'),
    path('shopping-list/<uuid:unique_id>/', shopping_list_detail, name='shopping_list_detail'),
    path('update-shopping-list/<int:item_id>/', update_shopping_list, name='update_shopping_list'),
    path('delete-from-shopping-list/<int:item_id>/', delete_from_shopping_list, name='delete_from_shopping_list'),
    path('add-to-shopping-list/<int:product_id>/', add_to_shopping_list, name='add_to_shopping_list'),
    path('shopping-list/', shopping_list_view, name='shopping_list'),
    path('download-shopping-list-after-payment/', download_shopping_list_after_payment, name='download_shopping_list_after_payment'),
    path('shopping-list/download/pdf/', download_shopping_list_as_pdf, name='download_shopping_list_as_pdf'),
]
