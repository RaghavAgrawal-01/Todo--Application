from django.shortcuts import render, redirect
from .models import Todo, Profile

# =================================== VIEWS HERE =========================

def home(request):    
    return render(request, "home.html")

# ====================================== TODO =========================================

def todo(request):
    
    todos = Todo.objects.filter(is_completed = False)

    completed = Todo.objects.filter(is_completed = True)

    
    parameters = {
        "todos": todos, # isme koi bhi completed todo nhi h
        "completed": completed
    }
    
    return render(request, "todo.html", parameters) # isme jo parameter ja rha h usme bhi koi completed todo nhi h

# ===================================== ADD TODO =======================================

def add_todo(request):
    
    if request.method == "POST":
        
        # Template s view m data la rha hu
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        # View vala data model m save kr rha hu
        new_todo = Todo(
            task=user_task, 
            created_at=user_created_at
            )
        new_todo.save()
        
        return redirect("todo")
        
    return render(request, "add_todo.html")

# ================================== DELETE TODO ===================================

def delete_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    todo.delete()

    return redirect("todo")

# ================================== UPDATE TODO ==========================

def update_todo(request, todo_id):
    
    todo = Todo.objects.get(id = todo_id)
    
    if request.method == "POST":
        user_task = request.POST.get("task")
        user_created_at = request.POST.get("created_at")
        
        todo.task = user_task
        todo.created_at = user_created_at
        
        todo.save()
        
        return redirect("todo")
    
    parameters = {
        'todo': todo
    }
    
    return render(request, "update_todo.html", parameters)

# ================================== MARK COMPLETE ================================

def mark_complete(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    
    todo.is_completed = True
    todo.save()
    
    return redirect("todo")

# ================================== UPLOAD PROFILE ===============================

def upload_profile(request):
    
    if request.method == "POST":
        profile_pic = request.FILES["profile_pic"]
        
        new_profile = Profile(
            title="demo title",
            profile_pic = profile_pic
            )
        
        new_profile.save()
        
        return redirect("todo")
    
    return render(request, "upload_profile.html")