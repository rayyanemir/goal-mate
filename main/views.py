from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app_name': 'GoalMate',
        'student_name': request.user.username,
        'student_class': 'PBP B',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'category': product.category,
            'brand': product.brand,
            'rating': float(product.rating) if product.rating else 0.0,
            'thumbnail': product.thumbnail,
            'description': product.description,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        xml_data = serializers.serialize("xml", [product_item])
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'brand': product.brand,
            'rating': float(product.rating) if product.rating else 0.0,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat() if hasattr(product, 'created_at') else None,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        # Handle AJAX requests
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                form = UserCreationForm(data)
                
                if form.is_valid():
                    user = form.save()
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your account has been successfully created!'
                    })
                else:
                    # Return form errors in JSON format
                    errors = {}
                    for field, error_list in form.errors.items():
                        if field == '__all__':
                            errors['non_field_errors'] = error_list
                        else:
                            errors[field] = error_list
                    
                    return JsonResponse({
                        'status': 'error',
                        'message': 'Please correct the errors below',
                        'errors': errors
                    }, status=400)
                    
            except Exception as e:
                return JsonResponse({
                    'status': 'error',
                    'message': 'An error occurred during registration',
                    'errors': {'non_field_errors': [str(e)]}
                }, status=500)
        
        # Handle regular form submission (fallback)
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_http_methods(["POST"])
def add_product_ajax(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            print("Received data:", data)  # Debug print
            
            # Create product
            new_product = Product(
                name=data.get('name'),
                price=data.get('price'),
                description=data.get('description', ''),
                category=data.get('category'),
                brand=data.get('brand', ''),
                stock=data.get('stock', 0),
                user=request.user
            )
            new_product.save()

            return JsonResponse({
                "status": "success",
                "message": "Product created successfully",
                "product_id": new_product.id
            }, status=201)
            
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_product_ajax(request, id):  # ← TERIMA ID DARI URL
    if request.method == 'PUT':
        try:
            # TERIMA DATA JSON DARI REQUEST BODY
            data = json.loads(request.body)
            
            product = Product.objects.get(pk=id, user=request.user)  # ← PAKAI ID DARI URL
            
            product.name = data.get("name")
            product.price = data.get("price")
            product.description = data.get("description")
            product.category = data.get("category", "lainnya")
            product.stock = data.get("stock", 0)
            product.brand = data.get("brand", "")
            product.thumbnail = data.get("thumbnail", "")
            
            product.save()
            
            return JsonResponse({
                "status": "success",
                "message": "Product updated successfully"
            }, status=200)
            
        except Product.DoesNotExist:
            return JsonResponse({
                "status": "error", 
                "message": "Product not found"
            }, status=404)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_product_ajax(request, id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=id, user=request.user)
            product.delete()
            return HttpResponse(b"DELETED", status=200)
        except Product.DoesNotExist:
            return HttpResponse(b"NOT_FOUND", status=404)

def get_product_json(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'stock': product.stock,
            'category': product.category,
            'brand': product.brand,
            'thumbnail': product.thumbnail,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def login_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = AuthenticationForm(data=data)
            
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                
                response_data = {
                    'status': 'success',
                    'message': 'Login successful!',
                    'redirect_url': reverse('main:show_main')
                }
                
                response = JsonResponse(response_data)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid username or password',
                    'errors': {'non_field_errors': ['Invalid credentials']}
                }, status=400)
                
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'An error occurred during login',
                'errors': {'non_field_errors': [str(e)]}
            }, status=500)

