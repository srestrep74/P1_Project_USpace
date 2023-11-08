//Coordenadas de la esquina superior izquierda y esquina inferio derecha que forman un rectangulo encerrando la zona
const bounds = [
    [6.20358,-75.57915], // Esquina superior izquierda
    [6.19657,-75.57830], // Esquina inferior derecha
];

// Crear un mapa centrado en la Universidad EAFIT y con límite de visualización en la zona de EAFIT
const map = L.map('map', {
    maxBounds: bounds,
    maxBoundsViscosity: 0.5, // Ajusta la viscosidad de los límites
    minZoom: 16, // Ajusta el nivel de zoom inicial
    dragging: true,
    zoomControl: false
}).setView([6.20018,-75.57845], 20); // Ajusta el nivel de zoom

// Agregar la capa base de OpenStreetMap
//L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}').addTo(map);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);