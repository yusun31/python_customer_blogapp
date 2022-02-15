from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomerForm
from .models import Customer


def customer_list(request):
    cus = Customer.objects.order_by('name')
    return render(request, 'customer/customer_list.html', {'customer_list': cus})


def customer_detail(request, pk):
    cu = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'cus': cu})


def customer_new(request):
    if request.method == "POST":
        cust_form = CustomerForm(request.POST)
        if cust_form.is_valid():
            clean_data_dict = cust_form.cleaned_data
            # create() 함수가 호출되면 등록처리가 이루어짐
            customer = Customer.objects.create(
                name=clean_data_dict['name'],
                email=clean_data_dict['email'],
                birthdate=clean_data_dict['birthdate'],
                gender=clean_data_dict['gender'],
            )
            return redirect('customer_detail', pk=customer.pk)
    else:
        cust_form = CustomerForm()
    return render(request, 'customer/customer_edit.html', {'form': cust_form})
