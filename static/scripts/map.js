
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
      var map = new Map({
        basemap: "topo"
      });
      var view = new MapView({
        container: "viewDiv", 
        map: map, 
        zoom: 7, 
        center: [javalon, javalat], 
      });

    var point = {
        type: "point",
        longitude: javalon,
        latitude: javalat,
    };

    var markerSymbol = {
        type: "simple-marker",
        color: [226, 119, 40],
  outline: {
      color: [0, 0, 0],
      width: 2
  }
    }

    var pointGraphic = new Graphic({
        geometry: point,
        symbol: markerSymbol,
    })
    view.graphics.add(pointGraphic);
   
    
    });


