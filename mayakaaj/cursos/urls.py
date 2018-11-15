from django.urls import path
from .views import UnidadListView,deleteUnidad,deleteLeccion
#DetailViewLeccion,
from . import views

urlpatterns = [    
    path('unidad', views.Unidad, name='unidad'),
    path('leccion', views.Leccion, name='leccion'),
    path('curso', views.Curso, name='curso'),
    path('temario', views.temario, name='temario'),
    path('detalleLeccion/<int:idLeccion>', views.detalleLeccion, name='detalleLeccion'),
    
    path('unidades', UnidadListView.as_view(), name='unidades'),
    path('detalleUnidad/<int:idUnidad>', views.detalleUnidad, name='detalleUnidad'),
    path('deleteUnidad/<int:pk>/', deleteUnidad.as_view(), name='deleteUnidad'),
    path('deleteLeccion/<int:pk>/', deleteLeccion.as_view(), name='deleteLeccion'),
]
    