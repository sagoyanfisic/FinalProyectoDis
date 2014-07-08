$(function() {
		
			$('#da-slider').cslider({
				autoplay	: true,
				bgincrement	: 1000
			});
		
		});
    	$( ".navbar-toggle" ).click(function() {
            $( ".collapse" ).toggle("slow"); 
        });
		$( ".dropdown" ).click(function() {
            $( ".dropdown-menu" ).toggle("slow"); 
        });