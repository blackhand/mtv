// JavaScript Document
$(document).ready(function(){ 
	
	//transparencia png
	var badBrowser = (/MSIE ((5\.5)|6)/.test(navigator.userAgent) && navigator.platform == "Win32");
	if (badBrowser) {
		// later code goes here
		$(document).pngFix();
		$('img').pngFix();
	}
	
	
	// dimensiones
	screen_width = screen.width;
	screen_height = screen.height;
	
	//$('.bg-body img').attr('width',screen_width*11);
	//$('.bg-body img').attr('height',screen_height);
	
	//$('.content-body').css('width',screen_width);
	$('.content-body-hidden').css('width',screen_width*11);
	$('.content-body-item').css('width',screen_width);
	
	// scroll
	$('.scroll-pane').jScrollPane();
	
	// cycle
	$('.cycle').cycle({
		fx:     'scrollHorz',
		speed:  'fast',
		timeout: 0,
		next:   '.next',
		prev:   '.prev'
	});
	
	// botones secciones cycle
	var $paneOptions = $('.content-body');
	
	$('a.btn-bot-01').click(function(){
		secAutoCycle(1);
		$paneOptions.scrollTo('#divInicio', 3000);
	});
	$('a.btn-bot-02').click(function(){
		secAutoCycle(2);
		$paneOptions.scrollTo('#divIntra1', 3000);
	});
	$('a.btn-bot-03').click(function(){
		secAutoCycle(3);
		$paneOptions.scrollTo('#divCompartir', 3000);
	});
	$('a.btn-bot-04').click(function(){
		secAutoCycle(4);
		$paneOptions.scrollTo('#divPremios', 3000);
	});
	$('a.btn-bot-05').click(function(){
		secAutoCycle(5);
		$paneOptions.scrollTo('#divProductos', 3000);
	});
	$('a.btn-bot-06, .btn-comercial').click(function(){
		secAutoCycle(6);
		$paneOptions.scrollTo('#divComercial', 3000);
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
	for(i=0; i <= aux; i++){
		$(".btn-auto").animate({ "left": ""+sig+"=1px" }, 1);
	}
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





