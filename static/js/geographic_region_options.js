$("#id_country").change(function () {
    let url = $("#containerModelForm").attr("data-locations-url");
    let countryId = $(this).val();
    $.ajax({
        url: url,
        data: {
            'country': countryId
        },
        success: function (data) {
            $("#id_geographic_region").html(data);
        }
    });
});


// let url = 'http://127.0.0.1:8000/locations/load/location/';
// let countryId = document.getElementById('id_country');
// let geo = document.getElementById('id_geographic_region');
//
//
// fetch(url, {
//     method : "POST",
//     body: {
//         'country': countryId
//     }
// }).then( function(data){
//     geo.innerHTML(data)
// }
    // .json(), etc.
    // same as function(response) {return response.text();}
// );
// geographic_region_option();
// selectValue.setAttribute('onchange');
// // form.action = 'http://127.0.0.1:8000/locations/package/create/';
// form.innerHTML = '<select name="country"><option value="1"></option>';
// document.body.append(form);
// form.submit();
