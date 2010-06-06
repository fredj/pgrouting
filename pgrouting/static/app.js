var mapPanel;
Ext.onReady(function() {
    var map = new OpenLayers.Map();
    var osm = new OpenLayers.Layer.OSM("Simple OSM Map");

    map.addLayer(osm);

//     mapPanel = new GeoExt.MapPanel({
//         map: map
//     });
});
