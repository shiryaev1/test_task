document.querySelector('#id_geographic_region').onchange = function getAdministrativeRegion() {
    let endpoint = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let geographicRegionId = this.value;
    const parameter = new URLSearchParams({
        geographic_region: geographicRegionId,
    });
    let url = endpoint + '?' + parameter;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_administrative_region").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url, true);
    xhr.send();
};
