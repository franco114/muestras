from django.urls import path
from .views import listaPendientes, EditarTareas, Logueo
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(listaPendientes.as_view()), name="tareas"),
    path("login/", Logueo.as_view(), name="login"),
    path("logout/", login_required(LogoutView.as_view(next_page="login")), name="logout"),
    path("editar-tarea/<int:pk>", login_required(EditarTareas.as_view()), name="editar-tarea"),
    
] 
