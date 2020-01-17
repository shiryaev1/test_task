document.querySelector('#id_administrative_region').onchange = function getMarkRegion() {
    let url = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let administrativeRegionId = this.value;
    let parameters = `administrative_region=${administrativeRegionId}`;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_mark_of_quality").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url + '?' + parameters, true);
    xhr.send();
};
