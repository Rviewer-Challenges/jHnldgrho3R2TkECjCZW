function convertSuccessful(value) {
    $('#unit2').val(value['result']);
}

function convert(units, from_unit, to_unit) {
    $.get({
        url: apiUrl,
        header: {'X-CSRFToken': csrfToken},
        data: {
            units: units,
            from_unit: from_unit,
            to_unit: to_unit
        },
        success: convertSuccessful
    });
}

function changed() {
    let option = $('#unit_selector').find(':selected');
    let from = option.data('from-unit');
    let to = option.data('to-unit');
    let units = $('#units').val();
    if(from !== undefined && to !== undefined && units !== undefined) {
        convert(units, from, to)
    }
}

$(function() {
    $('#unit_selector').on('change', changed);
    $('#units').on('change', changed);
});