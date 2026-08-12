from django.urls import path
from . import views


urlpatterns = [

    path("", views.dashboard, name="dashboard"),

    path(
        "customers/",
        views.customer_list,
        name="customer_list"
    ),

    path(
        "customers/add/",
        views.customer_create,
        name="customer_create"
    ),

    path(
        "customers/<int:id>/",
        views.customer_detail,
        name="customer_detail"
    ),

    path(
        "customers/<int:id>/edit/",
        views.customer_edit,
        name="customer_edit"
    ),

    path(
        "customers/<int:id>/delete/",
        views.customer_delete,
        name="customer_delete"
    ),
    path(
        "leads/",
        views.lead_list,
        name="lead_list"
    ),

]