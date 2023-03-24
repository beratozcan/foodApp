from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,

    }

    return render(request,'foodApp/index.html',context)

class IndexClassView(ListView):
    model = Item
    template_name = 'foodApp/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse('This is a item view.')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'foodApp/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'foodApp/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('foodApp:index')
    
    return render(request,'foodApp/item-form.html',{'form':form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'foodApp/item-form.html'

    def form_valid(self,form):
        form.instance.user_name=self.request.user

        return super().form_valid(form)

def update_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('foodApp:index')
    
    return render(request,'foodApp/item-form.html',{'form':form,'item':item})

def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('foodApp:index')
    
    return render(request,'foodApp/item-delete.html',{'item':item})