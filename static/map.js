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

// Definir el estilo para los marcadores (azul)
const markerStyle = L.icon({
    iconUrl: 'https://openlayers.org/en/latest/examples/data/icon.png', // Puedes usar tu propia imagen
    iconSize: [32, 32],
    iconAnchor: [16, 32],
});

const availableIcon = L.icon({
    iconUrl: 'https://openlayers.org/en/latest/examples/data/icon.png', // Icono disponible (puedes usar tu propia imagen)
    iconSize: [32, 32],
    iconAnchor: [16, 32],
});

const occupiedIcon = L.icon({
    iconUrl: 'static/pin.gif', // Icono ocupado (reemplaza con la URL de la imagen)
    iconSize: [32, 32],
    iconAnchor: [16, 32],
});

const poolCoordinates = [6.201110, -75.578756];
// Agregar el marcador de la piscina con el icono disponible por defecto
const poolMarker = L.marker(poolCoordinates, { icon: availableIcon }).addTo(map);
poolMarker.bindPopup('Piscina: Disponible').openPopup();

// Función para marcar la piscina como ocupada
function markPoolAsOccupied() {
    // Actualizar el marcador y el estado de la piscina
    poolMarker.setIcon(occupiedIcon);
    poolMarker.setPopupContent('Piscina: Ocupada').openPopup();
    // Puedes agregar aquí más lógica si necesitas realizar alguna acción adicional cuando la piscina se marque como ocupada.
}

// Evento del botón para marcar la piscina como ocupada
const btnPool = document.getElementById('btnPool');
btnPool.addEventListener('click', markPoolAsOccupied);

// Agregar los marcadores (puedes cambiar las coordenadas y los nombres)
const marker1 = L.marker([6.200854, -75.578756], { icon: markerStyle }).addTo(map);
marker1.bindPopup('Marcador 1').openPopup();

const marker2 = L.marker([6.201567, -75.576342], { icon: markerStyle }).addTo(map);
marker2.bindPopup('Marcador 2').openPopup();