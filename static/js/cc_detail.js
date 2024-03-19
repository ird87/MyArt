 $(document).ready(function() {
        $('#deleteButton').click(function() {
            $('#action').val('delete');
            $('#form').submit();
        });

        $('#saveButton').click(function() {
            $('#action').val('add');
            $('#form').submit();
        });
    });