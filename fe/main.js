// Initialize map and set view
const map = L.map("map").setView([51.505, -0.09], 2);

// Add a base layer to the map (use any other tile provider you prefer)
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Function to handle clicks on countries
function onCountryClick(e) {
  console.log("onCountryClick called");
  const countryAbb = e.target.feature.properties.iso_a2;
  const username = "your_username"; // Replace with the actual username

  async function onCountryClick(e) {
    console.log("onCountryClick called");
    const countryAbb = e.target.feature.properties.iso_a2;
    const username = "your_username"; // Replace with the actual username
  
    // Add or remove a country
    if (e.originalEvent.ctrlKey) {
      try {
        await axios.delete(`/api/user/${username}/countries/${countryAbb}`, {
          data: {
            Country: countryAbb,
            User: username,
          },
        });
      } catch (error) {
        console.error(error);
        alert(
          "An error occurred while updating the visited countries. Your changes might not be saved."
        );
      }
    } else {
      try {
        await axios.post(`/api/user/${username}/countries/${countryAbb}`, {
          data: {
            Country: countryAbb,
            User: username,
          },
        });
      } catch (error) {
        console.error(error);
        alert(
          "An error occurred while updating the visited countries. Your changes might not be saved."
        );
      }
    }
  }
  

// Load GeoJSON data for countries and add to map
axios
  .get("https://unpkg.com/world-atlas@3.0.0/countries-50m.json")
  .then((response) => {
    console.log("GeoJSON data loaded");
    const countriesLayer = L.geoJSON(response.data, {
      onEachFeature: (feature, layer) => {
        layer.on("click", onCountryClick);
      },
    });
    countriesLayer.addTo(map);
  });
