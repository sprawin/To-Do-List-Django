from django.shortcuts import redirect, render
from .models import ListItem, List


def ListView(request):
    if request.method == 'GET':
        List_Obj = List.objects.all()
        List_Itm_Obj = ListItem.objects.all()
        template = 'ListView.html'
        context = {'list_obj': List_Obj, 'list_itm_obj': List_Itm_Obj}
        return render(request, template, context)

def addListItem(request):
    if request.method == 'POST':
        list_id = request.POST['list']
        list_item = request.POST['list_item']

        List_Obj = List.objects.get(pk = list_id)
        List_Itm_Obj = ListItem()
        List_Itm_Obj.list = List_Obj
        List_Itm_Obj.name = list_item

        List_Obj.save()
        List_Itm_Obj.save()

        return redirect('/')

def deleteList(request, list_id):
    List_Obj = List.objects.get(pk = list_id)
    List_Obj.delete()

    return redirect('/')

def addNewList(request):
    if request.method == 'POST':
        List_Obj  = List()
        List_Obj.name = request.POST['ListName']
        List_Obj.save()
        return redirect('/')

def deleteListItem(request, list_item_id):
    List_Itm_Obj = ListItem.objects.get(pk = list_item_id)
    List_Itm_Obj.delete()

    return redirect('/')