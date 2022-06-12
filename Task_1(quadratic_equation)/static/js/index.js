$("form").submit(function(event) {
  event.preventDefault();
  $.ajax({
        url: '/',
        type: 'POST',
        data: $(this).serialize(),
        success: function (response) {
        $(".result-wrapper").empty()
        console.log(response)
           if (response === false) {alert("That's mistake! You entered incorrect values. Remember that ratio 'a' shouldn't be zero")}
           	else if (response === '') {$(".result-wrapper").append("<h3>This equation has no answer</h3>")}
           		else {
           			for (var i = 0; i < response.length; i++) {
           				{$(".result-wrapper").append(`<h3>${i+1}) Equation: <span>${response[i]}</h3>`)}
           			}
           		}
        },
        error: function (response) {
        }
    });
});