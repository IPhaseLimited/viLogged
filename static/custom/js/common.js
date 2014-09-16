'use strict';

var siteUrl = document.URL;
var urlArray = siteUrl.split('/');

function setActiveMenu(){

  var menuList = [
    'appointments',
    'home',
    'visitors',
    'reports',
    'documents',
    'staff',
    'system-settings'
  ];
  var found = [];
  urlArray.forEach(function(item) {
    if (parseInt(menuList.indexOf(item)) !== -1) {
      found.push(item);
    }
  });
  if (found.length > 0) {
    $('#li-'+found[0]).addClass('open');
  } else {
    $('#li-home').addClass('open');
  }
}

function uuidGenerator() {
  var now = Date.now();
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
    // jshint bitwise: false
    var r = (now + Math.random() * 16) % 16 | 0;
    now = Math.floor(now / 16);
    return (c === 'x' ? r : (r & 0x7 | 0x8)).toString(16);
  });
}

setActiveMenu();