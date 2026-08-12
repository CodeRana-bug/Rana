from django.shortcuts import render, redirect
from .models import Customer


def dashboard(request):

    total_customers = Customer.objects.count()

    recent_customers = Customer.objects.order_by(
        "-created_at"
    )[:5]

    context = {
        "total_customers": total_customers,
        "recent_customers": recent_customers,
    }

    return render(
        request,
        "crm/dashboard.html",
        context
    )


def customer_list(request):

    search = request.GET.get("search", "")

    customers = Customer.objects.all()

    if search:
        customers = customers.filter(
            name__icontains=search
        )

    context = {
        "customers": customers,
        "search": search,
    }

    return render(
        request,
        "crm/customers.html",
        context
    )

def customer_detail(request, id):

    customer = Customer.objects.get(id=id)

    context = {
        "customer": customer,
    }

    return render(
        request,
        "crm/customer_detail.html",
        context
    )


def customer_create(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        company = request.POST.get("company")

        Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company
        )

        return redirect("customer_list")

    return render(
        request,
        "crm/customer_form.html"
    )
def customer_edit(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == "POST":

        customer.name = request.POST.get("name")
        customer.email = request.POST.get("email")
        customer.phone = request.POST.get("phone")
        customer.company = request.POST.get("company")

        customer.save()

        return redirect("customer_list")

    context = {
        "customer": customer,
    }

    return render(
        request,
        "crm/customer_edit.html",
        context
    )
def customer_delete(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == "POST":

        customer.delete()

        return redirect("customer_list")

    context = {
        "customer": customer,
    }

    return render(
        request,
        "crm/customer_delete.html",
        context
    )