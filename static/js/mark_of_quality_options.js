$("#id_administrative_region").change(function () {
    let url = $("#containerModelForm").attr("data-locations-url");
    let administrative_regionId = $(this).val();
    $.ajax({
        url: url,
        data: {
            'administrative_region': administrative_regionId
        },
        success: function (data) {
            $("#id_mark_of_quality").html(data);
        }
    });
});