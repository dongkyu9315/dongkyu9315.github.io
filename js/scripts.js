var mcgillLocation = new google.maps.LatLng(45.504785,-73.577151);
	
function showMapMcgill() {
	var mapProp = {
			center: mcgillLocation,
			zoom: 14,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			scrollwheel: false
	};
	
	var map = new google.maps.Map(document.getElementById("mcgillMap"),mapProp);
	
	var marker = new google.maps.Marker({
		position: mcgillLocation,
	});
	
	marker.setMap(map);
}

google.maps.event.addDomListener(window, 'load', showMapMcgill);

var paLocation = new google.maps.LatLng(49.188744,-122.754181);

function showPacificAcademy() {
	var mapProp = {
			center: paLocation,
			zoom: 14,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			scrollwheel: false
	};
	
	var map = new google.maps.Map(document.getElementById("paMap"),mapProp);
	
	var marker = new google.maps.Marker({
		position: paLocation,
	});
	
	marker.setMap(map);
}

google.maps.event.addDomListener(window, 'load', showPacificAcademy);

$(function() {
	$('a[href*="#"]:not([href="#"])').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			if (target.length) {
				$('html, body').animate({
					scrollTop: target.offset().top
				}, 800);
				return false;
			}
		}
	});
});
