function formatParams( params ){
  return "?" + Object
        .keys(params)
        .map(function(key){
          return key+"="+encodeURIComponent(params[key])
        })
        .join("&")
}

document.querySelector('#id_country').onchange = function getGeographicRegion() {
    let endpoint = '/locations/load/location/';
    let xhr = new XMLHttpRequest();
    let countryId = this.value;
    let parameter = {
        country: countryId
    };
    let url = endpoint + formatParams(parameter);
    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_geographic_region").innerHTML = this.responseText;
        }
      };

    xhr.open("GET", url, true);
    xhr.send();
};
