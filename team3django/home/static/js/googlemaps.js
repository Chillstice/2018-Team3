var map;

function initMap() {
	var center = new google.maps.LatLng(39.7443305,-105.0229904);
	map = new google.maps.Map(document.getElementById('map'), {
		center: center, zoom: 10
	});
}

	//var marker = new google.maps.Marker({
	//	position: { lat: 39.742043, lng: -104.991531 },
	//	map: map
	//});

	//marker.setMap(map);

	//var infowindow = new google.maps.InfoWindow({
	//	content: '<p>Marker Location:' + marker.getPosition() + '</p>'
	//});

	//google.maps.event.addListener(marker, 'click', function () {
	//	infowindow.open(map, marker);
	//});


//google.maps.event.addDomListener(window, 'load', init);
