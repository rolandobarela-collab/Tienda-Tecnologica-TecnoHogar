let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

function agregarAlCarrito(nombre, precio) {
    fetch(`/stock/${encodeURIComponent(nombre)}/`)
        .then(res => res.json())
        .then(data => {
            const stockDisponible = data.stock;
            const existe = carrito.find(item => item.nombre === nombre);
            const cantidadActual = existe ? existe.cantidad : 0;

            if (cantidadActual >= stockDisponible) {
                alert(`Solo hay ${stockDisponible} unidades disponibles de ${nombre}`);
                return;
            }

            if (existe) {
                existe.cantidad++;
            } else {
                carrito.push({ nombre: nombre, precio: precio, cantidad: 1 });
            }

            actualizarTodo();
            mostrarToast(`${nombre} añadido al carrito`);
        });
}

function mostrarToast(mensaje){
    const toastEl = document.getElementById('toastCarrito');
    if(!toastEl) return;
    const toastBody = toastEl.querySelector('.toast-body');
    toastBody.innerText = mensaje;
    const toast = new bootstrap.Toast(toastEl);
    toast.show();
}

function actualizarTodo() {
    localStorage.setItem('carrito', JSON.stringify(carrito));

    const contador = document.getElementById('carrito-count');
    if (contador) {
        contador.innerText = carrito.reduce((acc, item) => acc + item.cantidad, 0);
    }

    const tabla = document.getElementById('items-carrito');
    const totalHtml = document.getElementById('total-carrito');

    if (tabla) {
        tabla.innerHTML = "";
        let sumaTotal = 0;

        carrito.forEach((item, index) => {
            const subtotal = item.precio * item.cantidad;
            sumaTotal += subtotal;
            tabla.innerHTML += `
                <tr>
                    <td>${item.nombre}</td>
                    <td>$${item.precio.toLocaleString()}</td>
                    <td>${item.cantidad}</td>
                    <td>$${subtotal.toLocaleString()}</td>
                    <td>
                        <button class="btn btn-danger btn-sm" onclick="eliminarProducto(${index})">
                            <i class="bi bi-trash"></i> Borrar
                        </button>
                    </td>
                </tr>
            `;
        });

        if (totalHtml) totalHtml.innerText = sumaTotal.toLocaleString();

        let botonPagar = document.getElementById("btn-pagar");
        let botonVaciar = document.getElementById("vaciar-carrito");

        if (carrito.length === 0) {
            if (botonPagar) botonPagar.classList.add("d-none");
            if (botonVaciar) botonVaciar.classList.add("d-none");
            tabla.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center text-muted py-4">
                        Tu carrito está vacío. ¡Anímate a añadir algo!
                    </td>
                </tr>
            `;
        } else {
            if (botonPagar) botonPagar.classList.remove("d-none");
            if (botonVaciar) botonVaciar.classList.remove("d-none");
        }
    }
}

window.eliminarProducto = function(index) {
    carrito.splice(index, 1);
    actualizarTodo();
};

document.getElementById('vaciar-carrito')?.addEventListener('click', () => {
    if (confirm("¿Estás seguro de que deseas vaciar todo el carrito?")) {
        carrito = [];
        actualizarTodo();
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById("btn-pagar")?.addEventListener("click", () => {
    fetch('/sesion/')
        .then(res => res.json())
        .then(data => {
            if (!data.logueado) {
                mostrarToast("Debes iniciar sesión para comprar");
                setTimeout(() => {
                    window.location.href = "/login/";
                }, 1500);
            } else {
                fetch('/pagar/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify(carrito)
                })
                .then(res => res.json())
                .then(data => {
                    if (data.ok) {
                        carrito = [];
                        actualizarTodo();
                        window.location.href = '/confirmacion/?pedido_id=' + data.pedido_id;
                    } else if (data.error) {
                        alert(data.error); // muestra alerta si hay error de stock
                    }
                });
            }
        });
});

document.addEventListener('DOMContentLoaded', () => {
    actualizarTodo();
});