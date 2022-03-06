from django.urls import path, include
from second.views import home_view, delete_Descriptions

urlpatterns = [
    path('', home_view.as_view(), name="home" ),
    path('delete/<int:pk>', delete_Descriptions.as_view(), name="delete_view"),
]
