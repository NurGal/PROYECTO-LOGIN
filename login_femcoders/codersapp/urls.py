"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from codersapp.views import *
from codersapp.forms import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('evaluacion/', evaluacion, name='evaluacion'),
    path('evaluacion/perfilAlumno/<int:id>', perfilAlumno, name='perfilalumno'),
    path('EditarNota/<int:id>', editevau, name='ponernota'),
    path('evaluacion/<int:id>', eliminarEvau, name='eliminar'),
    path('nuevo_alumno/', nuevoAlumno, name='nuevoal'),
    path('mis_alumnos/', ListaAlumno, name='listaal'),
    path('nueva_evaluacion/', nuevaEvaluacion, name='nuevaevaluacion'),
]