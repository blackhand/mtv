// JavaScript Document
function carga(){
	calculateBackgroundDimensions();	
}
function calculateBackgroundDimensions(){
	screen_width = $('.content-wrapper').width();
	screen_height = $('.content-wrapper').height();
	$('.bgDiv img').attr('width',screen_width);
	$('.content-body').css('width',screen_width);
	$('.content-body, .content-body-hidden, .content-body-item').css('height',screen_height);
	$('.content-body-item').css('width',screen_width);
	
	//$('.bgDiv, .bgDivSep').fadeIn(4000);
	//$('.content-wrapper').fadeIn(4000);
	$('.bgDiv, .bgDivSep').fadeIn(4000);
	
	total_width = $('.bgDiv img').width();
	total_height = $('.bgDiv img').height();
	//alert(total_height);
	$('.content-body-hidden').css('width',(screen_width * 6) + (total_width * 5));
	$('.bgDivSep img').attr('height',total_height);
	//
	$("#contenedor_1").scrollTo($('#bgDiv1'), 0);
	$("#contenedor_2").scrollTo('#divInicio', 0);
}

$(document).ready(function(){
	
	// precarga site
	//alert(navigator.appVersion)
	/*IE7 = (navigator.appVersion.indexOf("MSIE 7.")==-1) ? false : true;
	if(IE7){
		QueryLoader.init(carga);
	}else{
		QueryLoader.init();
		calculateBackgroundDimensions();
	}*/
	QueryLoader.init(carga);
	$('.content-wrapper').removeClass('not-visible');
	
	infoProd(2);
	
	
	// parallax home
	var myImages = new Array();
	myImages[0] = "images/img-home-layer-0.png";
	myImages[1] = "images/img-home-layer-1.png";
	myImages[2] = "images/img-home-layer-2.png";
	myImages[3] = "images/img-home-layer-3.png";
	$("#myimage2").imageparallax({ images: myImages, allowVertical: false });
	
	
	// inicializar valor
	$('#txtAutoCycle').val('1');
	
	
	// colorbox
	$('#ganadoras').click(function(){
		$('#youtube-player-container').tubeplayer('stop');
		$("#ganadoras").colorbox({iframe:true, href:"ganadoras.html", innerWidth:547, innerHeight:381});
	});
	$('#bases').click(function(){
		$('#youtube-player-container').tubeplayer('stop');
		$("#bases").colorbox({iframe:true, href:"static/bases.html", innerWidth:547, innerHeight:381});
	});
	$('#contactenos').click(function(){
		$('#youtube-player-container').tubeplayer('stop');
		$("#contactenos").colorbox({iframe:true, href:"contact/send", innerWidth:547, innerHeight:381});
	});
	
	
	// animacion home
	var flashvars = {
	};
	var params = {
	  menu: "false",
	  wmode: "transparent",
	  allowScriptAccess: "always"
	};
	var attributes = {
	  wmode: "transparent"
	};
	swfobject.embedSWF("static/swf/NosotrasCartels.swf", "NosotrasCartels", "772", "267", "9.0.0", "", flashvars, params, attributes);
	
	// reproductor youtube
	$("#youtube-player-container").tubeplayer({
		width: 290, // the width of the player
		height: 195, // the height of the player
		allowFullScreen: "true", // true by default, allow user to go full screen
		initialVideo: "5ILvSM7iGFk", // the video that is loaded into the player
		preferredQuality: "default"
	});
	
	
	// validar campos de texto
	$('#txtNombres, #txtApePa, #txtApeMa, #txtDireccion').alpha({allow:" ñÑáéíóúÁÉÍÓÚ"});
	$('#txtTelfCasa, #txtTelfCel, #txtDni').numeric();
	
	
	// cycle
	$('.cycle').cycle({
		fx:     'scrollHorz',
		speed:  'fast',
		timeout: 0,
		next:   '.next',
		prev:   '.prev'
	});
	
	
	// botones secciones cycle
	$('a.btn-bot-01').click(function(){
		secAutoCycle(1);
		$("#contenedor_1").scrollTo($('#bgDiv1'), 3000);
		$("#contenedor_2").scrollTo('#divInicio', 3000);
		$('#youtube-player-container').tubeplayer('stop');
		//
		//$('#iframe_ga').attr('src','inicio.html');
		//$('#iframe_ga').load();
	});
	$('a.btn-bot-02').click(function(){
		secAutoCycle(2);
		$("#contenedor_1").scrollTo($('#bgDiv2'), 3000);
		$("#contenedor_2").scrollTo('#divIntra1', 3000);
		$('#youtube-player-container').tubeplayer('stop');
		//
		$('#iframe_ga').attr('src','/manejatuvida/login.html');
		$('#iframe_ga').load();
	});
	$('a.btn-bot-03').click(function(){
		secAutoCycle(3);
		$("#contenedor_1").scrollTo($('#bgDiv3'), 3000);
		$("#contenedor_2").scrollTo('#divCompartir', 3000);
		$('#youtube-player-container').tubeplayer('stop');
		//
		$('#iframe_ga').attr('src','/manejatuvida/compartir.html');
		$('#iframe_ga').load();
	});
	$('a.btn-bot-04').click(function(){
		secAutoCycle(4);
		$("#contenedor_1").scrollTo($('#bgDiv4'), 3000);
		$("#contenedor_2").scrollTo('#divPremios', 3000);
		$('#youtube-player-container').tubeplayer('stop');
		//
		$('#iframe_ga').attr('src','/manejatuvida/premios.html');
		$('#iframe_ga').load();
	});
	$('a.btn-bot-05').click(function(){
		secAutoCycle(5);
		$("#contenedor_1").scrollTo($('#bgDiv5'), 3000);
		$("#contenedor_2").scrollTo('#divProductos', 3000);
		$('#youtube-player-container').tubeplayer('stop');
		//
		$('#iframe_ga').attr('src','/manejatuvida/empaques.html');
		$('#iframe_ga').load();
	});
	$('a.btn-bot-06, .btn-comercial').click(function(){
		secAutoCycle(6);
		$("#contenedor_1").scrollTo($('#bgDiv6'), 3000);
		$("#contenedor_2").scrollTo('#divComercial', 3000);
		$('#youtube-player-container').tubeplayer('play','5ILvSM7iGFk');
		//
		$('#iframe_ga').attr('src','/manejatuvida/comercial.html');
		$('#iframe_ga').load();
	});
	
	// tabs cycle
	$('.tab-suzuki-vitara').click(function(){
		$('ul.tabs-menu li').addClass('not-visible');
		$('.tab-menu-suzuki-vitara').removeClass('not-visible');
		$('ul.tabs-content li').addClass('not-visible');
		$('.tab-bg-suzuki-vitara').removeClass('not-visible');
	});
	$('.tab-suzuki-swift').click(function(){
		$('ul.tabs-menu li').addClass('not-visible');
		$('.tab-menu-suzuki-swift').removeClass('not-visible');
		$('ul.tabs-content li').addClass('not-visible');
		$('.tab-bg-suzuki-swift').removeClass('not-visible');
	});
	$('.tab-ipod').click(function(){
		$('ul.tabs-menu li').addClass('not-visible');
		$('.tab-menu-ipod').removeClass('not-visible');
		$('ul.tabs-content li').addClass('not-visible');
		$('.tab-bg-ipod').removeClass('not-visible');
	});
	
});

function secAutoCycle(val){
	tmp = $('#txtAutoCycle').val();
	if(val > tmp){
		aux = (val - tmp) * 95;
		sig = '+';
		BGsig = '-';
	}else{
		aux = (tmp - val) * 95;
		sig = '-';
		BGsig = '+';
	}
	$(".btn-auto").animate({ "left": ""+sig+"="+aux+"px" }, 3000);
	$('#txtAutoCycle').val(val);
}

function codEmpaque(val){
	if($('.codigo-empaque').hasClass('hidden')){
		$('.codigo-empaque').css('visibility','visible');
		$('.codigo-empaque').removeClass('hidden');
	}else{
		$('.codigo-empaque').css('visibility','hidden');
		$('.codigo-empaque').addClass('hidden');
	}
}

function secCycle(val){
	$('a.popup-bot-0'+val).removeClass('not-visible');
}
function secCycleOut(){
	$('ul.btns-popups li a').addClass('not-visible');
}

// vista de productos

function infoProd(val){
	$("ul.info-cartel li").animate({ "top": "-120px" }, 500);
	$("#img"+val+"").animate({ "top": "0" }, 500);
}

$(function(){
    $('#flip').jcoverflip({
		current:1,
		beforeCss: function( el, container, offset ){
			return [
				$.jcoverflip.animationElement( el, { left: ( container.width( )/2 - 200 - 140*offset + 20*offset )+'px', top:'20px' }, { } ),
				$.jcoverflip.animationElement( el.find( 'img' ), { width: Math.max(40,120-20*offset*offset) + 'px' }, {} ),
				$.jcoverflip.animationElement( el.find( 'canvas' ), { width: Math.max(40,120-20*offset*offset) + 'px' }, {} )
			];
		},
		afterCss: function( el, container, offset ){
			return [
				$.jcoverflip.animationElement( el, { left: ( container.width( )/2 + 70 + 140*offset + 20*offset )+'px', top:'20px'}, { } ),
				$.jcoverflip.animationElement( el.find( 'img' ), { width: Math.max(40,120-20*offset*offset) + 'px' }, {} ),
				$.jcoverflip.animationElement( el.find( 'canvas' ), { width: Math.max(40,120-20*offset*offset) + 'px' }, {} )
			];
		},
		currentCss: function( el, container ){
			return [
				$.jcoverflip.animationElement( el, { left: ( container.width( )/2 - 100 )+'px', top: '40px' }, { } ),
				$.jcoverflip.animationElement( el.find( 'img' ), { width: '192px' }, { } ),
				$.jcoverflip.animationElement( el.find( 'canvas' ), { width: '192px' }, { } )
			];
		},
		change: function(event, ui){
			var item_index = jQuery( '#flip' ).jcoverflip( 'current')
			infoProd(item_index+1);
		}
	});
	$(".ui-jcoverflip--item").unbind('click');
	$(".ui-jcoverflip").unbind('click');
});

function ingresaClave(){
	secAutoCycle(2);
	$("#contenedor_1").scrollTo($('#bgDiv2'), 3000);
	$("#contenedor_2").scrollTo('#divIntra1', 3000);
	$('#youtube-player-container').tubeplayer('stop');
	//
	$('#iframe_ga').attr('src','/manejatuvida/login.html');
	$('#iframe_ga').load();
}

function moveToNext(){
	var item_length = jQuery( '#flip' ).jcoverflip( 'length')
	var current_index = jQuery( '#flip' ).jcoverflip( 'current')
	
	if(parseInt( current_index ) < parseInt(item_length)-1){
		$(".flecha_der_carousel_productos").show();
		$(".flecha_izq_carousel_productos").show();
		jQuery( '#flip' ).jcoverflip( 'next', 1 );
	}
	if(parseInt( current_index ) > parseInt(item_length)-3 ){
		$(".flecha_der_carousel_productos").hide();
	}
}

function moveToPrev(){
	var current_index = jQuery( '#flip' ).jcoverflip( 'current')
	if( parseInt(current_index) > 0){
		$(".flecha_der_carousel_productos").show();
		$(".flecha_izq_carousel_productos").show();
		jQuery( '#flip' ).jcoverflip( 'previous', 1 );
	}

	if(parseInt( current_index ) < 2 ){
		$(".flecha_izq_carousel_productos").hide();
	}
}


function loginFacebook(){
	FB.login(function(response) {
	  if (response.session) {
		if (response.perms) {
			shareFacebook()
		  // user is logged in and granted some permissions.
		  // perms is a comma separated list of granted permissions
		} else {
		  // user is logged in, but did not grant any permissions
		}
	  } else {
		// user is not logged in
	  }
	}, {perms:'read_stream,publish_stream,user_birthday,email'});;
}

function shareFacebook(){
	FB.api('/me', function(responseName) {
		FB.ui({
			method: 'feed',
			name: 'Necesito espacio en la cochera para mi carro nuevo... mmm ¿Cómo haríamos?',
			link: 'http://www.nosotrasonline.com.pe/manejatuvida/',
			picture: 'http://dev.tribalperu.com/sancela_nosotras/images/share-facebook.jpg',
			//caption: 'Yo quiero el iPod y los vales de Saga que regala Nosotras esta semana',
			description: responseName.name+' ya compartió la frase de la semana y está participando por un iPod y vales de Saga Falabella.\n¡Tú también ENTRA AL SITE de la promoción, comparte la frase y participa!.',
			actions: [
				{ name: 'Comparte la frase', link: 'http://www.nosotrasonline.com.pe/manejatuvida/' }
			]},
			function(response) {
				FB.api('/me?fields=id,name,link,gender,birthday,email', function(response2) {
						$.ajax({
							type: 'POST',
							url: "/manejatuvida/facebook_save/",
							data: response2
						});
						/*
						valores para Yonsy
						id
						username
						gender
						email
						birthday
						link
						*/
						
						/*for(var i in response2){
							alert(i+" "+response2[i]);
						}*/
					});
				
		});
	});
}
