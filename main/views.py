from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, User
from .form import CreateNewList

from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request, id):
    ls = ToDoList.objects.get(id=id)
    # show user their todolist only
    if ls in request.user.todolist.all():
        if request.method == "POST":
            print(request.POST)
            if request.POST.get("save"):
                for item in ls.item_set.all():  # get all the items in the list
                    # get the item and set the status to complete
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif request.POST.get("newItem"):
                txt = request.POST.get('message')  # get the message input

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid Input!!")

            elif request.POST.get("deleteItem"):
                for delete_item in ls.item_set.all():
                    if request.POST.get("c" + str(delete_item.id)):
                        delete_item.delete()

        return render(request, "main/list.html", {"ls": ls})
    return render(request, "main/view.html", {})


def home(request):
    return render(request, "main/home.html", {})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            # create each user's todo list
            t = User(name=n, user=request.user)
            t.save()
            if request.user.is_authenticated:
                request.user.todolist.add(t)
        return HttpResponseRedirect("/%i" % t.id)  # type: ignore
    else:
        form = CreateNewList()
    return render(request, "main/create.html", {"form": form})


# @login_required
def view(request):
    return render(request, "main/view.html", {"user": request.user})
