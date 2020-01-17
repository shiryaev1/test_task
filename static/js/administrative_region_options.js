document.querySelector('#id_geographic_region').onchange = function geAdministrativeRegion() {
    let url = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let geographicRegionId = this.value;
    let parameters = `geographic_region=${geographicRegionId}`;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_administrative_region").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url + '?' + parameters, true);
    xhr.send();
};
