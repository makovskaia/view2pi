var viewer = new PhotoSphereViewer.Viewer({
    panorama: 'https://image.freepik.com/free-vector/stylish-hexagonal-line-pattern-background_1017-19742.jpg',
    container: document.querySelector('#photosphere'),
    defaultLat: 0.3,
    touchmoveTwoFingers: true,
    mousewheelCtrlKey: true,
    plugins: [
      [PhotoSphereViewer.MarkersPlugin, {
        markers: [{
      id: 1,
      latitude: '30deg',
      longitude: '15deg',
      image: 'https://www.pinpng.com/pngs/m/5-57589_download-svg-download-png-map-marker-png-icon.png',
      width: 50,
      height: 50,
    }]
      }], 
    ],
  });
var markersPlugin = viewer.getPlugin(PhotoSphereViewer.MarkersPlugin);
