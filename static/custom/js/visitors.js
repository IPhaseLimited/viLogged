$(document).ready(function() {
  $('#submit-btn').click(function(e) {
    e.preventDefault();
    var formThings = $('#visitorsForm').serialize();
    var uuid = uuidGenerator();
    $.ajax({
      url: '/rest/visitors/',
      data: formThings+'&uuid='+uuid,
      dataType: 'json',
      type: 'post',
      success: function(response) {
        window.location.href = '/visitors/'
      },
      error: function(response) {
        if (response.status === 400) {
          var reason = JSON.parse(response.responseText);
          (Object.keys(reason)).forEach(function(key) {
            $('#'+key).after('<div class="text-danger text-center">'+ reason[key][0]+'</div>')
          });
        }
        console.log(reason);
      }
    });
  });
  $( "#date_of_birth" ).datepicker({changeYear: true,
                                     dateFormat: "yy-mm-dd",
                                     minDate: new Date('1940'),
                                     maxDate: 'now'});
});
