from .models import Tarea

from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class Logueo(LoginView):
    template_name = "base/login.html"
    field = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tareas")


class listaPendientes(ListView):
    model = Tarea
    context_object_name = "tareas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        valor_buscado = self.request.GET.get("titulo", "")
        completo = self.request.GET.get("completo")
        medicion_completa = self.request.GET.get("medicion_completa")
        
        tareas = Tarea.objects.all()
        
        if valor_buscado:
            tareas = tareas.filter(titulo__icontains=valor_buscado)
        
        if completo is not None and completo != "":
            tareas = tareas.filter(completo=(completo == 'True'))
        
        if medicion_completa is not None and medicion_completa != "":
            tareas = tareas.filter(medicion_completa=(medicion_completa == 'True'))
        
        context["tareas"] = tareas
        context["valor_buscado"] = valor_buscado
        context["completo"] = completo
        context["medicion_completa"] = medicion_completa
        return context




class EditarTareas(UpdateView, User):
    model = Tarea
    success_url = reverse_lazy("tareas")
    fields = ["completo", "fecha", "medicion_completa", "fecha_medicion"]

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["user_visita"] = Group.objects.get(name="visitantes").user_set.all()
        except Group.DoesNotExist:
            context["user_visita"] = []
        try:
            context["user_muestreo"] = Group.objects.get(name="muestreo").user_set.all()
        except Group.DoesNotExist:
            context["user_muestreo"] = [] 
        try:       
            context["user_mediciones"] = Group.objects.get(name="mediciones").user_set.all()
        except Group.DoesNotExist:
            context["user_mediciones"] = []
        return context
