var viewer = new PhotoSphereViewer.Viewer({
    panorama: 'https://image.freepik.com/free-vector/stylish-hexagonal-line-pattern-background_1017-19742.jpg',
    container: document.querySelector('#photosphere'),
    defaultLat: 0.3,
    touchmoveTwoFingers: true,
    mousewheelCtrlKey: true,
    plugins: [
      [PhotoSphereViewer.MarkersPlugin, {
        markers: []
      }], 
    ],
  });
var markersPlugin = viewer.getPlugin(PhotoSphereViewer.MarkersPlugin);
