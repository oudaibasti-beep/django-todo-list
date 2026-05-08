from django.contrib import admin
from django.urls import path
from todo.views import home, delete_task # Importe bien les deux

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]