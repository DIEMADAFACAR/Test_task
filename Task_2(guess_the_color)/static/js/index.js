$("form").submit(function(event) {
  event.preventDefault();
  $.ajax({
        url: '/',
        type: 'POST',
        data: $(this).serialize(),
        success: function (response) {
          $(".result-wrapper").empty()
          console.log(response)
            if (response === false) {alert("Incorrectly input data")}
                else {
                  $(".result-wrapper").append(`<span>${response}</span>`)
                }
        },
        error: function (response) {
        }
    });
});