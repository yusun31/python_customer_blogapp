from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Customer


# Create your views here.
def customer_list(request):
    cus = Customer.objects.filter(birthdate__lte=timezone.now()).order_by('-birthdate')
    return render(request, 'customer/customer_list.html', {'customer_list': cus})


def customer_detail(request, pk):
    cu = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'cus': cu})
