from django.shortcuts import render
from .models import Customer


def dashboard(request):

    total_customers = Customer.objects.count()

    context = {
        "total_customers": total_customers,
    }

    return render(request, "crm/dashboard.html", context)

def customer_list(request):

    customers = Customer.objects.all()

    context = {
        "customers": customers,
    }

    return render(
        request,
        "crm/customers.html",
        context
    )