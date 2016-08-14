$(function () {
    $('#begin_date').datetimepicker({
        format: "YYYY-MM-DD HH:mm:ss"
    });
    $('#begin_date').data('DateTimePicker').date(
        moment().startOf('day')
    );
});

$(function () {
    $('#final_date').datetimepicker({
        format: "YYYY-MM-DD HH:mm:ss"
    });
    $('#final_date').data('DateTimePicker').date(
        moment().endOf('day')
    );
});
