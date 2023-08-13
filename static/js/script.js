// Cambiar el color de fondo del cuerpo de la página al hacer clic en un botón
function changeBackgroundColor() {
    document.body.style.backgroundColor = getRandomColor();
}

// Generar un color aleatorio en formato hexadecimal
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
