from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_html(request):
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
 
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_pesan(request):
    data_my_watch_list = MyWatchList.objects.all()

    watched_count = 0
    unwatched_count = 0

    for movie in data_my_watch_list:
        if movie.watched == True:
            watched_count += 1
        else:
            unwatched_count += 1

    if watched_count >= unwatched_count:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
       
    context_pesan = {
        'pesan': pesan,
    }

    return render(request, "pesan.html", context_pesan)


data_my_watch_list = MyWatchList.objects.all()

context = {
    'watch_list': data_my_watch_list,
    'nama': 'Natania Deandra',
    'npm': 2106633090,
}

