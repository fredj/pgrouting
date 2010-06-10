Ext.onReady(function() {
    var header = new Ext.Panel({
        region: 'north',
        height: 50
    });

    var map = new GeoExt.MapPanel({
        region: 'center',
        map: {
             layers: [new OpenLayers.Layer.OSM("Simple OSM Map")]
        },
        center: [245300, 5070600],
        zoom: 12
    });

    var form = new Ext.form.FormPanel({
        region: 'south',
        height: 150
    });

    var viewport = new Ext.Viewport({
        layout: 'border',
        defaults: {
            frame: false
        },
        items: [header, map, form]
    });
});
