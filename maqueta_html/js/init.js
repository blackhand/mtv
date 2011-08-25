// JavaScript Document
$(document).ready(function(){ 
	
	//transparencia png
	var badBrowser = (/MSIE ((5\.5)|6)/.test(navigator.userAgent) && navigator.platform == "Win32");
	if (badBrowser) {
		// later code goes here
		$(document).pngFix();
		$('img').pngFix();
	}
	
	$('.scroll-pane').jScrollPane();
	
	$('#cycleSite').cycle({
		fx:     'scrollHorz',
		speed:  5000,
		timeout: 0,
		next:   '.btn-right',
		prev:   '.btn-left'
	});
	
	$('.cycle').cycle({
		fx:     'scrollHorz',
		speed:  'fast',
		timeout: 0,
		next:   '.next',
		prev:   '.prev'
	});
	
	$('.tab-suzuki-vitara').click(function(){
		$('ul.tabs-menu li').addClass('not-visible')
		$('.tab-menu-suzuki-vitara').removeClass('not-visible')
		$('ul.tabs-content li').addClass('not-visible')
		$('.tab-bg-suzuki-vitara').removeClass('not-visible')
	});
	$('.tab-suzuki-swift').click(function(){
		$('ul.tabs-menu li').addClass('not-visible')
		$('.tab-menu-suzuki-swift').removeClass('not-visible')
		$('ul.tabs-content li').addClass('not-visible')
		$('.tab-bg-suzuki-swift').removeClass('not-visible')
	});
	$('.tab-ipod').click(function(){
		$('ul.tabs-menu li').addClass('not-visible')
		$('.tab-menu-ipod').removeClass('not-visible')
		$('ul.tabs-content li').addClass('not-visible')
		$('.tab-bg-ipod').removeClass('not-visible')
	});
	
});


function codEmpaque(val){
	if($('.codigo-empaque').hasClass('hidden')){
		$('.codigo-empaque').css('visibility','visible');
		$('.codigo-empaque').removeClass('hidden')
	}else{
		$('.codigo-empaque').css('visibility','hidden');
		$('.codigo-empaque').addClass('hidden')
	}
}








