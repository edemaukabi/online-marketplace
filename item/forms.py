from django.forms import ModelForm
from .models import Item


class NewItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']