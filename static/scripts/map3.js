require(["esri/Map", 
"esri/views/MapView",
"esri/Graphic",
"esri/widgets/BasemapToggle",
"esri/widgets/BasemapGallery"], 
function(Map,
MapView,
Graphic,
  BasemapToggle,
  BasemapGallery
 )
 {
    var map2 = new Map({
      basemap: "topo"
    });
    var view = new MapView({
      container: "viewDiv2", 
      map: map2, 
      zoom: 3, 
      center: [javalon, javalat], 
    });

  var point = {
      type: "point",
      longitude: javalon,
      latitude: javalat,
  };

  var markerSymbol = {
      type: "simple-marker",
      style: "square",
      size: "20",
      // color: [226, 119, 40],
outline: {
    color: [255, 0, 0],
    width: 2
}
  }

  var pointGraphic2 = new Graphic({
      geometry: point,
      symbol: markerSymbol,
  })
  view.graphics.add(pointGraphic2);
 
  
  });