from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self, request):
        topwears =  Product.objects.filter(category='TW')
        bottomwears =  Product.objects.filter(category='BW')
        mobiles =  Product.objects.filter(category='M')
        laptops =  Product.objects.filter(category='L')
        context = {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles':mobiles, 'laptops':laptops}
        return render(request, 'esell/home.html', context)





class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        # template_name = 'templ/'+str(product.id)+'.html'
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render (request, 'esell/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart})


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id') # ths id id from the form in product detail html
    product = Product.objects.get(id=product_id)
    add_cart = Cart(user=user, product=product)
    add_cart.save()
    return redirect('/esell/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                single_amount = (p.quantity * p.product.discounted_price)
                amount += single_amount
            return render(request, 'esell/addtocart.html', {'carts':cart, 'total_amount':amount + shipping_amount, 'amount':amount})
        else:
            return render(request, 'esell/emptycart.html')



def plus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        user=request.user
        c = Cart.objects.get(Q(product=product_id) & Q(user=user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            single_amount = (p.quantity * p.product.discounted_price)
            amount += single_amount
        
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'toatl_amount': amount + shipping_amount
        }

        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        user=request.user
        c = Cart.objects.get(Q(product=product_id) & Q(user=user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            single_amount = (p.quantity * p.product.discounted_price)
            amount += single_amount
        
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'toatl_amount': amount + shipping_amount
        }

        return JsonResponse(data)



def remove_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        user=request.user
        c = Cart.objects.get(Q(product=product_id) & Q(user=user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            single_amount = (p.quantity * p.product.discounted_price)
            amount += single_amount
        
        data = {
            'amount': amount,
            'toatl_amount': amount + shipping_amount
        }

        return JsonResponse(data)




@login_required
def checkout(request):
    user = request.user
    addr = Customer.objects.filter(user=user)
    cart_item = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            single_amount = (p.quantity * p.product.discounted_price)
            amount += single_amount
        total_amount = amount + shipping_amount
    
    return render(request, 'esell/checkout.html', {'addr': addr, 'total_amount': total_amount, 'cart_item':cart_item})

@login_required
def payment_done(request):
    custid = request.GET.get('custid')
    user = request.user
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")




@login_required
def buy_now(request):
    user = request.user
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    addr = Customer.objects.filter(user=user)
    shipping_cost = 70.0
    total_amount = product.discounted_price + shipping_cost
    return render(request, 'esell/buynow.html', {'product':product, 'addr':addr, 'total_amount': total_amount})


@login_required
def buy_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    OrderPlaced(user=user, customer=customer, product=product, quantity=1).save()
    return redirect("orders")



@login_required
def address(request):
    addr = Customer.objects.filter(user=request.user)
    return render(request, 'esell/address.html', {'addr':addr})


@login_required
def orders(request):
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'esell/orders.html', {'order_placed':order_placed})




class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'esell/customerregistration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registered Successfully, Please login")
            form.save()
        return render(request, 'esell/customerregistration.html', {'form':form})



@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'esell/profile.html', {'form':form})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            delivary_mail = form.cleaned_data['delivary_mail']
            district = form.cleaned_data['district']
            village = form.cleaned_data['village']
            division = form.cleaned_data['division']
            postal = form.cleaned_data['postal']
            reg = Customer(user=usr, name=name, district=district, village=village, division=division,
            postal=postal, delivary_mail=delivary_mail)
            reg.save()
            messages.success(request, 'Congratulations!! your profile updated successfully.')
        return render(request, 'esell/profile.html', {'form':form})







