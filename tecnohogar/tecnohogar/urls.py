from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('audifonos/', views.audifonos, name='audifonos'),
    path('componentes/', views.componentes, name='componentes'),
    path('laptops/', views.laptops, name='laptops'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ofertapc/', views.ofertapc, name='ofertapc'),
    path('ofertapcGamer/', views.ofertapc_gamer, name='ofertapc_gamer'),
    path('ofertaTablet/', views.oferta_tablet, name='oferta_tablet'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('registro/', views.registro, name='registro'),
    path('tablets/', views.tablets, name='tablets'),
    path('sesion/', views.sesion_activa, name='sesion_activa'),
    path('pagar/', views.procesar_pago, name='pagar'),
    path('historial/', views.historial, name='historial'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('buscar/', views.buscar, name='buscar'),
]