document.querySelector('#id_country').onchange = function getGeographicRegion() {
    let url = $("#containerModelForm").attr("data-locations-url");
    let xhr = new XMLHttpRequest();
    let countryId = this.value;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_geographic_region").innerHTML = this.responseText;
          console.log(this.responseText);
        }
      };
    xhr.open("GET", url + '?' + 'country=' + countryId, true);
    xhr.send();
};
