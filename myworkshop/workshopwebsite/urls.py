from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("add_client/", views.add_client, name="add_client"),
    path("add_car/", views.add_car, name="add_car"),
    path("check_button/", views.check_button, name="check_button"),
    path("check_your_order/", views.check_your_order, name="check_your_order"),
    path("add_order/", views.add_order, name="add_order"),
    path("choose_mechanic/", views.choose_mechanic, name="choose_mechanic"),
    path("assign_mechanic/", views.assign_mechanic, name="assign_mechanic"),
    path(
        "choose_finishing_date/",
        views.choose_finishing_date,
        name="choose_finishing_date",
    ),
    path(
        "proceed_to_data_completion/",
        views.proceed_to_data_completion,
        name="proceed_to_data_completion",
    ),
    path("order_list", views.order_list, name="order_list"),
    path("car/", car, name="cars"),
    path("client/", client, name="clients"),
    path("mechanic/", mechanic, name="mechanics"),
    path("orderInitialDetails/", orderInitialDetails, name="orderInitialDetailss"),
    path(
        "orderAdditionalDetails/",
        orderAdditionalDetails,
        name="orderAdditionalDetailss",
    ),
]
