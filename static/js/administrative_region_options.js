document.querySelector('#id_geographic_region').onchange = function geAdministrativeRegion() {
    let url = $("#containerModelForm").attr("data-locations-url");
    let xhr = new XMLHttpRequest();
    let geographicRegionId = this.value;
    console.log(geographicRegionId);

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_administrative_region").innerHTML = this.responseText;
          console.log(this.responseText);
        }
      };
    xhr.open("GET", url + '?' + 'geographic_region=' + geographicRegionId, true);
    xhr.send();
};
