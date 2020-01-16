// $("#id_country").change(function () {
//     let url = $("#containerModelForm").attr("data-locations-url");
//     let countryId = $(this).val();
//     $.ajax({
//         url: url,
//         data: {
//             'country': countryId
//         },
//         success: function (data) {
//             $("#id_geographic_region").html(data);
//         }
//     });
// });

document.querySelector('#id_country').onchange = function getGeographicRegion() {
    let url = $("#containerModelForm").attr("data-locations-url");
    let xhr = new XMLHttpRequest();
    // xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    let countryId = this.value;
    let data = {
        'country': countryId
    };
      xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
          document.getElementById("id_geographic_region").innerHTML = this.responseText;
          console.log(this.responseText);
        }
      };
      xhr.open("GET", url, true);
      xhr.send(data);
};

// function getAdmin(stateId) {
// let xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState === 4 && this.status === 200) {
//       document.getElementById("citydiv").innerHTML = this.responseText;
//     }
//   };
//    xhttp.open("GET", "/state/"+stateId, true);
//   xhttp.send();
// }
//
//
// $(document).on('submit','#locationform',function(e){
// 	e.preventDefault();
//
// });
//
// function result(){
// let xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState === 4 && this.status === 200) {
//       document.getElementById("result").innerHTML = this.responseText;
//     }
//   };
//    xhttp.open("GET", "/".concat($('select[name=country]').val(),"/",$('select[name=state]').val(),"/",$('select[name=city]').val()), true);
//   xhttp.send();
// }