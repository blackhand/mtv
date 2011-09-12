function validate_form1() {
    // login
    email = $('#txtEmail_1').val();
    day = $('#cboDia_1').val();
    month = $('#cboMes_1').val();
    year = $('#cboAnio_1').val();
    $.get(
        '/manejatuvida/validate_form1', 
        {'email': email, 'day': day, 'month': month, 'year': year}, 
        function(data) {
            if(data==='error') {
                $('#msg').html('Correo o Fecha de nacimiento invalida o en blanco');
                return false;
            }
            if(data==='exist') {
                dest='.form-captcha';
                $.get('/manejatuvida/captcha', function(captcha) {
                    $(".captcha").html(captcha);
                })
            }
            if(data==='not-exist') {
                dest='.form2';
            }

            $('#txtEmail_2').val(email);
            $('#cboDia_2').val(day);
            $('#cboMes_2').val(month);
            $('#cboAnio_2').val(year);

            transicion('.form1', dest);
        });
    return false;
}

function clean_form1() {
    $('#txtEmail_1').val('');
    $('#cboDia_1').val('[día]');
    $('#cboMes_1').val('[mes]');
    $('#cboAnio_1').val('[año]');

}

function validate_form2() {
    // register
    email = $('#txtEmail_2').val();
    day = $('#cboDia_2').val();
    month = $('#cboMes_2').val();
    year = $('#cboAnio_2').val();
    names = $('#txtNombres').val();
    last_name1 = $('#txtApePa').val();
    last_name2 = $('#txtApeMa').val();
    ubigeo = $('#cboProv').val()
    address = $('#txtDireccion').val();
    phone = $('#txtTelfCasa').val();
    mobile = $('#txtTelfCel').val();
    doc_number = $('#txtDni').val();
    $.get(
        '/manejatuvida/validate_form2', 
        {'email': email, 'day': day, 'month': month, 'year': year, 'names': names, 'last_name1': last_name1, 'last_name2': last_name2, 'ubigeo': ubigeo, 'address': address, 'phone': phone, 'mobile': mobile, 'doc_number': doc_number}, 
        function(data) {
            if(data==='error') {
                $('#msg_registro').html('Error en los datos de registro, por favor complete todos los campos obligatorios');
                return false;
            }
            if(data==='success') {
                $.get('/manejatuvida/captcha', function(captcha) {
                    $(".captcha").html(captcha);
                })

            $('#iframe_ga').attr('src','/manejatuvida/registro.html');
            $('#iframe_ga').load();

                transicion('.form2', '.form-captcha');
            }
        });
    return false;
}

function clean_form2() {
    $('#txtNombres').val('');
    $('#txtApePa').val('');
    $('#txtApeMa').val('');
    $('#cboProv').val('')
    $('#txtDireccion').val('');
    $('#txtTelfCasa').val('');
    $('#txtTelfCel').val('');
    $('#txtDni').val('');
}

function validate_form_captcha() {
    codigo = $('#codigoEmpaque').val()
    clave = new clavePersonal(codigo); //<-- clave nueva
    clave.validar();
    if(clave.esValida()) {
        $('.profile_name').load('/manejatuvida/get_profile_name');
        $.get('/manejatuvida/validate_generic', {'code': clave.getGenerico()}, function(data) {
            if(data==='notvalid') {
                transicion('.form-captcha', '.form-clave-no-valida');
            } else {
                if(data==='1') {
                    $('.profile_options').html('1 opción');
                } else {
                    $('.profile_options').html('2 opciones');
                }
            };
        });

        var recaptcha_challenge_field = $("input[name='recaptcha_challenge_field']").val()
        var recaptcha_response_field = $("input[name='recaptcha_response_field']").val()

        $.post(
            '/manejatuvida/validate_form_captcha',{'codigo':codigo,'recaptcha_challenge_field': recaptcha_challenge_field,'recaptcha_response_field': recaptcha_response_field},
            function(data) {
                $.get('/manejatuvida/captcha', function(captcha) {
                    $(".captcha").html(captcha);
                });
                if(data==='success') {
                    $('#iframe_ga').attr('src','/manejatuvida/codigo-correcto.html');
                    $('#iframe_ga').load();
                    transicion('.form-captcha', '.form-clave-correcta');
                    return false;
                };
                if(data==='exist') {
                    $('#iframe_ga').attr('src','/manejatuvida/codigo-incorrecto.html');
                    $('#iframe_ga').load();
                    transicion('.form-captcha', '.form-clave-ya-registrada');
                };
                if(data==='error') {
                    $('#iframe_ga').attr('src','/manejatuvida/codigo-ya-registrado.html');
                    $('#iframe_ga').load();
                    transicion('.form-captcha', '.form-clave-no-valida');
                }
            });
    } else {
        transicion('.form-captcha', '.form-clave-no-valida');
    };
}

function transicion(source, dest){
    $(source).fadeOut(500, function(){
        $(dest).fadeIn(500);
        $('.scroll-pane').jScrollPane();
    });
}


$(document).ready(function() {
    // Ubigeo magic here
    $('#cboDpto').change(function() {
      if($('#cboDpto').val() =='0')return false;
      $.get('/manejatuvida/ubigeo/get_ubigeo/'+$('#cboDpto').val()+"/", function(data){
        var provincias = jQuery.parseJSON(data);
        $("select[name='cboProv'] > option").remove();
        $("select[name='cboProv']").append('<option value="" selected="selected">[seleccionar]</option>');
        $("select[name='cboDist'] > option").remove();
        $("select[name='cboDist']").append('<option value="" selected="selected">[seleccionar]</option>');
        for(var i in provincias){
            $("select[name='cboProv']").append('<option value="'+provincias[i]['pk']+'">'+provincias[i]['fields']['name']+'</option>');
        }
      })
    });
    $('#cboProv').change(function() {
      if($('#cboProv').val() =='0')return false;
      $.get('/manejatuvida/ubigeo/get_ubigeo/'+$('#cboProv').val()+"/",function(data){
        var distritos = jQuery.parseJSON(data)
        $("select[name='cboDist'] > option").remove();
        $("select[name='cboDist']").append('<option value="" selected="selected">[seleccionar]</option>');
        for(var i in distritos){
            $("select[name='cboDist']").append('<option value="'+distritos[i]['pk']+'">'+distritos[i]['fields']['name']+'</option>');
        }
      })
    });
})
