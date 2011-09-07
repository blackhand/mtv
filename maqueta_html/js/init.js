// JavaScript Document
$(document).ready(function(){ 
	
	//transparencia png
	var badBrowser = (/MSIE ((5\.5)|6)/.test(navigator.userAgent) && navigator.platform == "Win32");
	if (badBrowser) {
		// later code goes here
		$(document).pngFix();
		$('img').pngFix();
	}
	
	// scroll
	$('.scroll-pane').jScrollPane();
	
});







