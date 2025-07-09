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