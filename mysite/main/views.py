from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreateNewList

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all(): # get all the items in the list
                if response.POST.get("c" + str(item.id))== "clicked": # get the item and set the status to complete
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get('message') # get the message input

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid Input!!")

        elif response.POST.get("deleteItem"):
            for delete_item in ls.item_set.all():
                if response.POST.get("c" + str(delete_item.id)):
                    delete_item.delete()


    return render(response, "main/list.html", {"ls":ls})


def home(response):
    return render(response, "main/home.html", {"name": "Test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id) #type: ignore
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})