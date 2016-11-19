$(document).ready(function() {
    $('h1').text('boo');
    console.log('hi');
    require('nw.gui').Window.get().showDevTools();
});
