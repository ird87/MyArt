$(document).ready(function() {

    $('.center-row').dblclick(function() {
        var id = $(this).data('id');
        var name = $(this).data('name');
        var url = '/cc/' + id+'/';

        var title =  name;
        showModal(title, url);
    });

    // Обработка клика на кнопку "Добавить"
    $('#addButton').click(function() {
        var url = '/cc/0/';
        var title = 'Добавить новый центр';
        showModal(title, url);
    });

});

