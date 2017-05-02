function enviar() {
      var username = $('#').val();

  $.ajax({
    url: '/andromeda/validate_username/',
    data: {
      'username': username
    },
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        alert("A user with this username already exists.");
      }
    }
  });
}
