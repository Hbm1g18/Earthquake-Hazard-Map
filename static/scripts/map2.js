var map;
javalat = document.getElementById("lat").innerHTML;
javalon = document.getElementById("lon").innerHTML;
javavlat = document.querySelector(".volcanolat").innerHTML;
javavlon = document.querySelector(".volcanolon").innerHTML;

require([
  "esri/map", "esri/geometry/webMercatorUtils", "dojo/dom",  "esri/config",
  "dojo/domReady!",
  "esri/layers/FeatureLayer",
  
], function(
  Map, esriConfig, webMercatorUtils, dom
) {
  esriConfig.apiKey = "AAPKe19f8d9fa7244403a0724025389d650fkLXD3IR8eyIrHO4nJSYeASjxL7i9pxhcOiJKUmgBYWDUd7nerMMaULRjf4HP8qaO";
  map = new Map("map", {
    basemap: "topo",
    center: [javalon, javalat],  
  //   DO THIS
    zoom: 8
  });
  // 
  
  // 
  map.on("load", function() {

  });


});