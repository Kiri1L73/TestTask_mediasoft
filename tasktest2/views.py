from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasktest2.models import Shop, City, Street
from tasktest2.forms import ShopForm

def city(request):
    cities = City.objects.order_by('name')
    print(request.GET)

    return render(request, 'city.html', {'cities': cities})




def street(request, city_id):
    city = get_object_or_404(City, id=city_id)
    streets = Street.objects.filter(city=city).order_by('name')
    return render(request, 'street.html', {'streets': streets, 'city': city})


def shop(request):
    shops = Shop.objects.order_by('name')
    print(request.GET)

    return render(request, 'shops.html', {'shops': shops})


def shops(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            new_shop = form.save()
            return redirect('id_newshop', shop_id=new_shop.pk)
    else:
        form = ShopForm()

    return render(request, 'shop.html', {'form': form})


def id_newshop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'id_newshop.html', {'shop': shop})



def about_shop(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    cities = City.objects.filter(shop=shop).order_by('name')
    streets = Street.objects.filter(shop=shop).order_by('name')
    is_open = 1 if shop.is_open() else 0
    return render(request, 'about_shop.html', {'cities': cities, 'streets' : streets, 'is_open': is_open, 'shop': shop})




# Create your views here.
