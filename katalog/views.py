from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html", context)

data_catalog_item = CatalogItem.objects.all()
context = {
    'list_barang': data_catalog_item,
    'nama': 'Natania Deandra',
    'npm': 2106633090,
}