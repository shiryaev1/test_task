$("#id_geographic_region").change(function () {
    let url = $("#containerModelForm").attr("data-locations-url");
    let geographic_regionId = $(this).val();
    $.ajax({
        url: url,
        data: {
            'geographic_region': geographic_regionId
        },
        success: function (data) {
            $("#id_administrative_region").html(data);
        }
    });
});
