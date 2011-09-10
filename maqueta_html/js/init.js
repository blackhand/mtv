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
	
	
	// solo digitos
	/*jQuery.fn.ForceNumericOnly =
	function()
	{
		return this.each(function()
		{
			$(this).keydown(function(e)
			{
				var key = e.charCode || e.keyCode || 0;
				// allow backspace, tab, delete, arrows, numbers and keypad numbers ONLY
				return (
					key == 8 || 
					key == 9 ||
					key == 46 ||
					(key >= 37 && key <= 40) ||
					(key >= 48 && key <= 57) ||
					(key >= 96 && key <= 105));
			});
		});
	};
	
	$("#txtDni").ForceNumericOnly();*/

	
});







