function showModal(title, url) {
    // Загрузка URL в iframe и отображение модального окна
    $('#modal-iframe').attr('src', url);
    var myModal = new bootstrap.Modal(document.getElementById('myModal'));
    myModal.show();

    // Установка заголовка модального окна
    $('#addModalLabel').text(title);

    // Изменение высоты iframe после его загрузки
    $('#modal-iframe').on('load', function() {
        this.style.height = this.contentWindow.document.body.scrollHeight + 'px';

        // Привязка обработчика события submit к форме после ее загрузки
        this.contentWindow.$('#form').on('submit', function(e) {
            e.preventDefault();

            $.ajax({
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function(response) {
                    // Закрытие модального окна и обновление страницы
                    myModal.hide();
                    location.reload();
                }
            });
        });
    });
}