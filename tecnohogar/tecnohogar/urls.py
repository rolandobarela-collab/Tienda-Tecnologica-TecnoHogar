from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('stock/<str:nombre>/', views.stock_producto, name='stock_producto'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_done.html'), name='password_reset_complete'),
]