from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomerForm, CustomerModelForm, CommentForm
from .models import Customer, Comment


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('customer_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment_pk = comment.post.pk
    comment.delete()
    return redirect('customer_detail', pk=comment_pk)


def add_comment_to_customer(request, pk):
    post = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('customer_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'customer/add_comment_to_customer.html', {'form': form})


def customer_list(request):
    cus = Customer.objects.order_by('name')
    return render(request, 'customer/customer_list.html', {'customer_list': cus})


def customer_detail(request, pk):
    cu = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'cus': cu})


@login_required
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


@login_required
def customer_edit(request, pk):
    cust = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        cust_form = CustomerModelForm(request.POST, instance=cust)
        if cust_form.is_valid():
            customer = cust_form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        cust_form = CustomerModelForm(instance=cust)
        return render(request, 'customer/customer_edit.html', {'form': cust_form})


@login_required
def customer_remove(request, pk):
    cust = get_object_or_404(Customer, pk=pk)
    cust.delete()
    return redirect('customer_list_home')
