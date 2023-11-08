//Coordenadas de la esquina superior izquierda y esquina inferio derecha que forman un rectangulo encerrando la zona
const bounds = [
    [6.202708, -75.58052], // Esquina superior izquierda
    [6.197644, -75.5757], // Esquina inferior derecha
];

// Crear un mapa centrado en la Universidad EAFIT y con límite de visualización en la zona de EAFIT
const map = L.map('map', {
    maxBounds: bounds,
    maxBoundsViscosity: 0.7, // Ajusta la viscosidad de los límites
    minZoom: 15, // Ajusta el nivel de zoom inicial
    dragging: true,
}).setView([6.20020, -75.57842], 20); // Ajusta el nivel de zoom

// Agregar la capa base de OpenStreetMap
//L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}').addTo(map);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);