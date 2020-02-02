from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse,Http404



from .models import Item
from .forms import AddItem

def IndexView(request):
    #HOME PAGE CONTENT
	items = Item.objects.order_by('-created_date')
	args = {
	'items':items,
	}
	return render(request, 'index.html', args)


def listingdetail(request,slug):
    #LIST DETAIL ONCE CLICKED
    try:
        objects = Item.objects.all()
        items = Item.objects.get(slug=slug)
        context = {'items':items,
        'objects': objects,
        }
        return render(request,'detailview.html',context)
    except:
        raise Http404



@login_required
def listing_create(request):
    #ADD AN ITEM BUT USER MUST SIGN UP/IN TO POST SOMETHING
    title = 'Create'
    form = AddItem(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('')
    context = {
        'title': title,
        'form': form
    }
    return render(request, "additem.html", context)