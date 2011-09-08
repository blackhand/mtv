$(document).ready(function(){
    // great ... all forms use the same clases for send :/
    $('a.btn-enviar').click( function(){

        $('.form1').addClass('not-visible');
        $('.form2').removeClass('not-visible');
        $('.scroll-pane').jScrollPane();
        //$('#iframe_ga').attr('src','inicio.html');
        //$('#iframe_ga').load();
    });
});

function validate() {
    return true;
}
