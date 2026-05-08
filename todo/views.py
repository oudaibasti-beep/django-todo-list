from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    # Si on appuie sur le bouton "Ajouter"
    if request.method == "POST":
        titre = request.POST.get('title')
        if titre:
            Task.objects.create(title=titre)
        return redirect('home')

    # Affichage de la liste
    toutes_les_taches = Task.objects.all()
    return render(request, 'todo/home.html', {'tasks': toutes_les_taches})

# Fonction pour supprimer une tâche
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')