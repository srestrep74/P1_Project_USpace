//Coordenadas de la esquina superior izquierda y esquina inferio derecha que forman un rectangulo encerrando la zona
const bounds = [
    [6.202708, -75.58052], // Esquina superior izquierda
    [6.197644, -75.5757], // Esquina inferior derecha
];

// Crear un mapa centrado en la Universidad EAFIT y con límite de visualización en la zona de EAFIT
const map = L.map('map', {
    maxBounds: bounds,
    maxBoundsViscosity: 1.0,
    minZoom : 18, // Ajusta el límite incluso cuando el usuario intente hacer zoom fuera de los límites.
}).setView([6.200146, -75.577256], 20);

// Agregar la capa base de OpenStreetMap
//L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}').addTo(map);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

