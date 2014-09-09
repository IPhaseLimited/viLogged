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


});

function uuidGenerator() {
  var now = Date.now();
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
    // jshint bitwise: false
    var r = (now + Math.random() * 16) % 16 | 0;
    now = Math.floor(now / 16);
    return (c === 'x' ? r : (r & 0x7 | 0x8)).toString(16);
  });
}
