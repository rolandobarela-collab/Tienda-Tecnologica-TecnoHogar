from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .models import Producto, Pedido, ItemPedido
import json

def index(request):
    return render(request, 'index.html', {
        'usuario_logueado': request.user.is_authenticated
    })

def audifonos(request):
    productos = Producto.objects.filter(categoria='audifonos')
    return render(request, 'audifonos.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def componentes(request):
    productos = Producto.objects.filter(categoria='componentes')
    return render(request, 'componentes.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def laptops(request):
    productos = Producto.objects.filter(categoria='laptops')
    return render(request, 'laptops.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def ofertapc(request):
    productos = Producto.objects.filter(categoria='laptops')
    return render(request, 'ofertapc.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def ofertapc_gamer(request):
    productos = Producto.objects.filter(categoria='componentes')
    return render(request, 'ofertapcGamer.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def oferta_tablet(request):
    productos = Producto.objects.filter(categoria='tablets')
    return render(request, 'ofertaTablet.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def tablets(request):
    productos = Producto.objects.filter(categoria='tablets')
    return render(request, 'tablets.html', {
        'productos': productos,
        'usuario_logueado': request.user.is_authenticated
    })

def registro(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro')

        if User.objects.filter(email=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return redirect('registro')

        nombre = correo.split('@')[0]
        usuario = User.objects.create_user(username=correo, email=correo, password=password)
        usuario.first_name = nombre
        usuario.save()
        messages.success(request, 'Registro exitoso, ya puedes iniciar sesión')
        return redirect('login')

    return render(request, 'registro.html')

def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=correo)
            usuario = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            usuario = None

        if usuario is not None:
            login(request, usuario)
            if not usuario.is_staff:
                request.session['es_admin'] = False
            return redirect('index')
        else:
            messages.error(request, 'Correo o contraseña incorrectos')
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def recuperar(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        try:
            usuario = User.objects.get(email=correo)
            token = default_token_generator.make_token(usuario)
            uid = urlsafe_base64_encode(force_bytes(usuario.pk))
            link = f"http://127.0.0.1:8000/reset/{uid}/{token}/"

            send_mail(
                subject='Recuperar contraseña - TecnoHogar',
                message=f'Hola {usuario.first_name},\n\nHaz click en el siguiente enlace para recuperar tu contraseña:\n\n{link}\n\nSi no solicitaste esto, ignora este mensaje.',
                from_email='roliruana@gmail.com',
                recipient_list=[correo],
                fail_silently=False,
            )
            messages.success(request, 'Te enviamos un correo con instrucciones.')
        except User.DoesNotExist:
            messages.error(request, 'No existe una cuenta con ese correo.')
        return redirect('recuperar')

    return render(request, 'recuperar.html')

def sesion_activa(request):
    return JsonResponse({'logueado': request.user.is_authenticated})

def buscar(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'buscar.html', {
        'productos': productos,
        'query': query,
        'usuario_logueado': request.user.is_authenticated
    })

def stock_producto(request, nombre):
    producto = Producto.objects.filter(nombre=nombre).first()
    if producto:
        return JsonResponse({'stock': producto.stock})
    return JsonResponse({'stock': 0})

@login_required
def procesar_pago(request):
    if request.method == 'POST':
        carrito = json.loads(request.body)

        if not carrito:
            return JsonResponse({'error': 'Carrito vacío'}, status=400)

        for item in carrito:
            producto = Producto.objects.filter(nombre=item['nombre']).first()
            if producto and int(item['cantidad']) > producto.stock:
                return JsonResponse({
                    'error': f"Solo hay {producto.stock} unidades disponibles de {producto.nombre}"
                }, status=400)

        pedido = Pedido.objects.create(
            usuario=request.user,
            total=sum(int(item['precio']) * int(item['cantidad']) for item in carrito)
        )

        for item in carrito:
            producto = Producto.objects.filter(nombre=item['nombre']).first()

            if producto:
                producto.stock -= int(item['cantidad'])
                if producto.stock <= 0:
                    producto.stock = 0
                producto.save()

            ItemPedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=int(item['cantidad']),
                precio_unitario=int(item['precio'])
            )

        return JsonResponse({'ok': True, 'pedido_id': pedido.id})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

@login_required
def historial(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'historial.html', {
        'pedidos': pedidos,
        'usuario_logueado': request.user.is_authenticated
    })

def confirmacion(request):
    pedido_id = request.GET.get('pedido_id')
    return render(request, 'confirmacion.html', {
        'pedido_id': pedido_id,
        'usuario_logueado': request.user.is_authenticated
    })