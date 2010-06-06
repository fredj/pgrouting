var mapPanel;

Ext.onReady(function() {

    mapPanel = new GeoExt.MapPanel({
        renderTo: "map",
        map: {
             layers: [new OpenLayers.Layer.OSM("Simple OSM Map")]
        },
        center: [245300, 5070600],
        zoom: 12
    });
});
