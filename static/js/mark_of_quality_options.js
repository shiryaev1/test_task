document.querySelector('#id_administrative_region').onchange = function getMarkRegion() {
    let url = $("#containerModelForm").attr("data-locations-url");
    let xhr = new XMLHttpRequest();
    let administrativeRegionId = this.value;

    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_mark_of_quality").innerHTML = this.responseText;
          console.log(this.responseText);
        }
      };
    xhr.open("GET", url + '?' + 'administrative_region=' + administrativeRegionId, true);
    xhr.send();
};
