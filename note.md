# Adding Users

to make each user have their own todo list 
```
response.user.todolist_set.create(name=n)

```

display todo list in the views 
```
{% for td in user.todolist_set %}
    <p><a href="{{td.id}}"></a>{{td.name}}</p>
{% endfor %}
```

we loop through todo and get todo id and name

i run to an error when trying to create a todolist but the problem was i'm using response instead of request here's how i fix it

```
if request.user.is_authenticated:
            request.user.todolist.add(name=t)
```