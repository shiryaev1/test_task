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
