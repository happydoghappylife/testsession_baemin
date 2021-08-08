from django.shortcuts import get_object_or_404, redirect, render
from .models import Store
from .forms import StoreForm

def mainpage(request):
    stores = Store.objects.all()
    stores_count = Store.objects.count()

    return render(request, 'mainpage.html', {"stores" : stores, "stores_count" : stores_count})


def detail(request, store_id):

    return render(request, 'detail.html')


def detail(request, store_id):
    store = get_object_or_404(Store, id = store_id)

    return render(request, 'detail.html', {'store': store})

def create(request):
    if request.method == "POST":
        # POST
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save()
            return redirect('detail', store.id)

    else:
        # GET
        form = StoreForm()

    context = {'form' : form}

    return render(request, 'create.html', context)