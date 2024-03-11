$(document).ready(function() {

    // Обработка двойного клика на строке
    $('.center-row').dblclick(function() {
        var id = $(this).data('id');
        $.get('/cc/' + id+'/', function(data) {
            // Заполнение формы данными записи
            $('#centerId').val(id);
            $('#name').val(data.name);
            $('#repertoire_url').val(data.repertoire_url);
            $('#poster_url').val(data.poster_url);
            $('#address').val(data.address);
            $('#image_url').val(data.image_url);
            // Открытие модального окна
            $('#addModal').modal('show');
        });
    });

    // Обработка клика на кнопку "Добавить"
    $('#addButton').click(function() {
        // Очистка формы
        $('#centerId').val(0);
        $('#name').val('');
        $('#repertoire_url').val('');
        $('#poster_url').val('');
        $('#address').val('');
        $('#image_url').val('');
        // Открытие модального окна
        $('#addModal').modal('show');
    });

    $('#saveButton').click(function() {
        var id = $('#centerId').val();
        var formData = $('#form').serializeArray();
        var data = {};
        $(formData).each(function(index, obj){
            data[obj.name] = obj.value;
        });
        $.ajax({
            url: '/cc/' + id + '/',
            type: 'post',
            dataType: 'json',
            contentType: 'application/json',
            success: function () {
                location.reload();
            },
            data: JSON.stringify(data)
        });
    });

});
