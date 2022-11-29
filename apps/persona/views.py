from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status

# Forms
from .forms.persona_forms import PersonaForm, SolicitudForm
# API
from .api.views.ApiViews import ApiViewPersona


# Create your views here.
def crear_persona(request):
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            instance_api_persona = ApiViewPersona.as_view()(request=request)
            print(instance_api_persona.status_code)
            if instance_api_persona.status_code == status.HTTP_201_CREATED:
                print("Se registro")
                return HttpResponseRedirect(reverse('pet_list'))
            else:
                print("No se registro")
                print(instance_api_persona.data)
    else:
        persona_form = PersonaForm()
    return render(request, 'persona_agregar.html', {'persona_form': persona_form})
