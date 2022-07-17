$(document).on('submit', '#filters', function (e) {
    var formData = $("#filters").serializeArray();
    $("#formButton").attr("disabled", true);
    $("#formButton").attr('value', 'Processing...');
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/filters',
        contentType: "application/json",
        data: JSON.stringify({ form_data: formData, track_id: $("#filters").data("track") }),
        success: function (response) {
            $("#formButton").attr("disabled", false);
            $("#formButton").attr('value', 'Apply Filters');
            $("#mapFrame").attr('src', 'map');
            $('#distance').text("Total distance: " + response.distance + " km");
        },
        error: function (e) {
            $("#formButton").attr("disabled", false);
            $("#formButton").attr('value', 'Apply Filters');
            console.log(e)
        }
    })
});