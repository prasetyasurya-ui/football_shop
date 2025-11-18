from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse  
from main.forms import ProductForm
from main.models import Item
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    sort = request.GET.get("sort", "asc")

    
    if filter_type == "all":
        if sort == "asc":
            product_list = Item.objects.all().order_by("price")
        else:
            product_list = Item.objects.all().order_by("-price")
    else:
        if sort == "asc":
            product_list = Item.objects.filter(user=request.user).order_by("price")
        else:
            product_list = Item.objects.filter(user=request.user).order_by("-price")

    context = {
        'shopName': "Wolverhampton Shop",
        'name': 'Prasetya Surya Syahputra',
        'npm': '2406398381',
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username,
        'sort': sort
    }

    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def create_product(request):
    name = request.POST.get("name");
    description = request.POST.get("desc");
    category = request.POST.get("category");
    thumbnail = request.POST.get("thumbnail");
    is_featured = request.POST.get("is_featured") == 'on';
    price = request.POST.get("price");
    user = request.user;

    new_product = Item(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )

    new_product.save();

    return HttpResponse(b"CREATED", status=201);

@login_required(login_url='/login')
def show_product(request, product_id):
    product = get_object_or_404(Item, pk=product_id)

    context = {'product': product}

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Item.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Item.objects.all()
    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'category': item.category,
            'is_featured': item.is_featured,
            'terjual': item.terjual,
            'user_id': item.user_id
        }
        for item in product_list
    ]

    return JsonResponse(data, safe=False)

@login_required
def show_json_by_user(request):
    product_list = Item.objects.filter(user=request.user)
    
    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'category': item.category,
            'is_featured': item.is_featured,
            'terjual': item.terjual,
            'user_id': item.user_id
        }
        for item in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product = Item.objects.filter(pk = product_id)
        xml_data = serializers.serialize("xml", product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Item.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Item.objects.select_related('user').get(pk = product_id)
        json_data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'terjual': product.terjual,
            'user_id': product.user_id
        }
        return JsonResponse(json_data);
    except Item.DoesNotExist:
        return JsonResponse({'detail': 'Not Found'}, status=404);

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Account created! You will be redirected to login.'
            }, status=201)
        else:
            errors = json.loads(form.errors.as_json())
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    
    return render(request, 'register.html')
    

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response =  JsonResponse({
                'status': 'success',
                'message': 'Login succesfull!',
                'redirect_url': reverse('main:show_main')
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            errors = json.loads(form.errors.as_json())
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)

    return render(request, 'login.html')

@csrf_exempt
def logout_user(request):
    logout(request)

    redirect_url = reverse('main:login');

    response = JsonResponse({
        'status': 'success',
        'message': 'You have been logged out.',
        'redirect_url': redirect_url
    })

    response.delete_cookie('last_login');

    return response

@csrf_exempt
@require_POST
def edit_product(request, id):
    product = get_object_or_404(Item, pk = id)

    product.name = request.POST.get("name");
    product.description = request.POST.get("desc");
    product.category = request.POST.get("category");
    product.thumbnail = request.POST.get("thumbnail");
    product.is_featured = request.POST.get("is_featured") == 'on';
    product.price = request.POST.get("price");
    product.user = request.user;

    product.save();

    json_data = {
        'id': str(product.id),
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'thumbnail': product.thumbnail,
        'category': product.category,
        'is_featured': product.is_featured,
        'terjual': product.terjual,
        'user_id': product.user_id
    }

    return JsonResponse(json_data, status=201)

@csrf_exempt
@require_POST
def delete_product(request, id):
    product = get_object_or_404(Item, pk = id)

    if product.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Not authorized'}, status=403)
    
    product.delete()
    return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})


@login_required
def get_page_data(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'is_authenticated': True,
            'user_id': request.user.id,
            'username': request.user.username,
            'name': 'Prasetya Surya Syahputra',
            'npm': '2406398381',
            'class': 'PBP E',
        })
    else:
        return JsonResponse({'is_authenticated': False})


def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        price = data.get("price", "")
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Item(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)