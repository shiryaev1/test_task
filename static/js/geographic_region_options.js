document.querySelector('#id_country').onchange = function getGeographicRegion() {
    let endpoint = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let countryId = this.value;
    const parameter = new URLSearchParams({
        country: countryId,
    });
    let url = endpoint + '?' + parameter;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_geographic_region").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url, true);
    xhr.send();
};
