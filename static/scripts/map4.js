const items = document.querySelectorAll('.volcdiv div');
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
    var map3 = new Map({
      basemap: "topo"
    });
    var view3 = new MapView({
      container: "viewDiv3", 
      map: map3, 
      zoom: 3, 
      center: [-130,15], 
    });
    
  [...items].forEach(item => {
 // iterating through each div
 var point3 = {
      type: "point",
      longitude: javavlon,
      latitude: javavlat,
  };

  var markerSymbol3 = {
      type: "simple-marker",
      color: [225, 0, 0],
outline: {
    color: [0, 0, 0],
    width: 1.5
}
  }

  var pointGraphic3 = new Graphic({
      geometry: point3,
      symbol: markerSymbol3,
  })

  view3.graphics.add(pointGraphic3);

  });


//   var point3 = {
//       type: "point",
//       longitude: javavlon,
//       latitude: javavlat,
//   };

//   var point4 = {
//       type: "point",
//       longitude: 0,
//       latitude: 0,
//   };

//   var markerSymbol3 = {
//       type: "simple-marker",
//       color: [225, 0, 0],
// outline: {
//     color: [0, 0, 0],
//     width: 1.5
// }
//   }

  // var pointGraphic3 = new Graphic({
  //     geometry: point3,
  //     symbol: markerSymbol3,
  // })

  // var pointGraphic4 = new Graphic({
  //     geometry: point4,
  //     symbol: markerSymbol3,
  // })

  // view3.graphics.add(pointGraphic3);

  view3.graphics.add(pointGraphic4);
 
  
  });