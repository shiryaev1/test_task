document.querySelector('#id_administrative_region').onchange = function getMarkOfQuality() {
    let endpoint = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let administrativeRegionId = this.value;
    const parameter = new URLSearchParams({
        administrative_region: administrativeRegionId,
    });
    let url = endpoint + '?' + parameter;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_mark_of_quality").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url, true);
    xhr.send();
};
