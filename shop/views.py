from django.shortcuts import render, redirect
from shop.forms import Catform, CatSalesForm, Itemform
from shop.models import Item, CatSales, Categories

def home(request):
    return render(request, 'home.html')

def user(request):
    if request.method == "POST":
        form = Catform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else:
        form = Catform()
    return render(request, 'selectcat.html', {'form': form})

def user_items(request):
    if request.method == "POST":
        form = Itemform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_items')
            except:
                pass

    else:
        form = Itemform()
        print("wrong")
    return render(request, 'enter_items.html', {'form': form})

def user_catsales(request):
    if request.method == "POST":
        form = CatSalesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_catsales')
            except:
                pass

    else:
        form = CatSalesForm()
        print("wrong")
    return render(request, 'enter_CatSales.html', {'form': form})

def show(request):
    materials = Categories.objects.all()
    return render(request, 'show.html', {'materials':materials})

def show_items(request):
    things = Item.objects.all()
    return render(request, 'show_items.html', {'things':things})

def show_catsales(request):
    things1 = CatSales.objects.all()
    return render(request, 'show_catsales.html', {'things1':things1})

def edit(request, id):
    categories = Categories.objects.get(id=id)
    return render(request, 'edit.html', {'categories':categories})

def edit_items(request, id):
    shop_item = Item.objects.get(id=id)
    return render(request, 'edit_items.html', {'shop_item':shop_item})
def update(request, id):
    categories = Categories.objects.get(id=id)
    forms = Catform(request.POST, instance= categories)
    if forms.is_valid():
        forms.save()
        return redirect('/show')
    return render(request, 'edit.html', {'categories':categories})
def update_items(request, id):
    shop_item = Item.objects.get(id=id)
    forms = Itemform(request.POST, instance= shop_item)
    if forms.is_valid():
        forms.save()
        return redirect('/show_items')
    return render(request, 'edit_items.html', {'shop_item':shop_item})
def delete(request, id):
    items = Categories.objects.get(id=id)
    items.delete()
    return redirect('/show')

def delete_items(request, id):
    items1 = Item.objects.get(id=id)
    items1.delete()
    return redirect('/show_items')
def delete_catsales(request, id):
    items1 = CatSales.objects.get(id=id)
    items1.delete()
    return redirect('/show_catsales')




    