document.querySelector('#id_country').onchange = function getGeographicRegion() {
    let url = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let countryId = this.value;
    let parameters = `country=${countryId}`;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_geographic_region").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url + '?' + parameters, true);
    xhr.send();
};
