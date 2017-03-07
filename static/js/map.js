  var directionDisplay;
  var directionsService = new google.maps.DirectionsService();


  function initialize() {
    var latlng = new google.maps.LatLng(42.353343,-71.056137);
    var UScenter = {lat: 40.461881, lng: -99.757229};
    directionsDisplay = new google.maps.DirectionsRenderer();
    var myOptions = {
      zoom: 14,
      center: UScenter,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      mapTypeControl: false
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById("directionsPanel"));


  var contentString = '<div id="content">'+
            '<div id="siteNotice">'+
            '</div>'+
            '<h1 id="firstHeading" class="firstHeading">Uluru</h1>'+
            '<div id="bodyContent">'+
            '<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
            'Heritage Site.</p>'+
            '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">'+
            'https://en.wikipedia.org/w/index.php?title=Uluru</a> '+
            '(last visited June 22, 2009).</p>'+
            '</div>'+
            '</div>';

  var infowindow = new google.maps.InfoWindow({
          content: contentString
        });
 





  var marker = new google.maps.Marker({
      position: UScenter, 
      map: map, 
      title:"My location"
    }); 

  var i, locations
  locations= {{marker_list | tojason}};

  
  for (i = 0; i < 1; i++) { 
      var location = {lat: locations[i][0], lng: locations[i][1]};
      marker = new google.maps.Marker({
      position: 
      map: map, 
      title:"My location"
      }); 

      map.addListener('center_changed', function() {
              // 3 seconds after the center of the map has changed, pan back to the
              // marker.
              window.setTimeout(function() {
                map.panTo(marker.getPosition());
              }, 3000);
            });

            marker.addListener('click', function() {
              map.setZoom(8);
              map.setCenter(marker.getPosition());
              infowindow.open(map, marker);


            });

      }

  }


  function calcRoute() {
    var start = document.getElementById("routeStart").value;
    var end = "51.764696,5.526042";
    var request = {
      origin:start,
      destination:end,
      travelMode: google.maps.DirectionsTravelMode.DRIVING
    };
    directionsService.route(request, function(response, status) {
      if (status == 'ZERO_RESULTS') {
        alert('No route could be found between the origin and destination.');
      } else if (status == 'UNKNOWN_ERROR') {
        alert('A directions request could not be processed due to a server error. The request may succeed if you try again.');
      } else if (status == 'REQUEST_DENIED') {
        alert('This webpage is not allowed to use the directions service.');
      } else if (status == 'OVER_QUERY_LIMIT') {
        alert('The webpage has gone over the requests limit in too short a period of time.');
      } else if (status == 'NOT_FOUND') {
        alert('At least one of the origin, destination, or waypoints could not be geocoded.');
      } else if (status == 'INVALID_REQUEST') {
        alert('The DirectionsRequest provided was invalid.');         
      } else {
        alert("There was an unknown error in your request. Requeststatus: nn"+status);
      }
    });
  }