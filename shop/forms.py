from django import forms
from shop.models import Categories, Item, CatSales

class Catform(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

class Itemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class CatSalesForm(forms.ModelForm):
    class Meta:
        model = CatSales
        fields = "__all__"