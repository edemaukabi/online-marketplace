from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import NewItemForm
from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:4]
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, 'item/detail.html', context)


@login_required
def new_item(request):
    form = NewItemForm()
    context = {
        'form': form,
        'title': 'New Item'
    }
    return render(request, 'item/form.html', context)