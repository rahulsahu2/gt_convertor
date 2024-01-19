from django.urls import path
from .views import upload_receipt_file, success_page, downloadfile

urlpatterns = [
    path("upload/", upload_receipt_file, name="convert"),
     path('success/', success_page, name='success_page'),
     path('upload/receipts/converted_csv/<str:filename>/', downloadfile, name='success_page'),
]