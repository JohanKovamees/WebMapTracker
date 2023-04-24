// Initialize map and set view
const map = L.map('map').setView([51.505, -0.09], 2);

// Add a base layer to the map (use any other tile provider you prefer)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Function to handle clicks on countries
function onCountryClick(e) {
  const countryAbb = e.target.feature.properties.iso_a2;
  const username = 'your_username'; // Replace with the actual username

  // Add or remove a country
  if (e.originalEvent.ctrlKey) {
    axios.delete(`/api/user/${username}/countries/${countryAbb}`);
  } else {
    axios.post(`/api/user/${username}/countries/${countryAbb}`);
  }
}

// Load GeoJSON data for countries and add to map
axios.get('https://unpkg.com/world-atlas@2.0.0-preview.4/countries-50m.json')
  .then(response => {
    const countriesLayer = L.geoJSON(response.data, {
      onEachFeature: (feature, layer) => {
        layer.on('click', onCountryClick);
      },
    });
    countriesLayer.addTo(map);
  });
