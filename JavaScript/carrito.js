let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

function agregarAlCarrito(nombre, precio) {
    const existe = carrito.find(item => item.nombre === nombre);
    if (existe) {
        existe.cantidad++;
    } else {
        carrito.push({ nombre: nombre, precio: precio, cantidad: 1 });
    }
    actualizarTodo();
    alert(`¡${nombre} añadido al carrito!`);
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
            // Fuerza la desaparición añadiendo la clase de Bootstrap "d-none"
            if (botonPagar) botonPagar.classList.add("d-none");
            if (botonVaciar) botonVaciar.classList.add("d-none");
            tabla.innerHTML = `<tr><td colspan="5" class="text-center text-muted py-4">Tu carrito está vacío. ¡Anímate a añadir algo!</td></tr>`;
        } else {
            // Quita la clase para que vuelvan a aparecer
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

document.addEventListener('DOMContentLoaded', () => {
    actualizarTodo();
});