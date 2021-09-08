async function getImage(id){
  try{
    const response = await fetch('http://127.0.0.1:8000/api/image/'+id+'/') 
    const data = await response.json()
    await viewer.setPanorama(data.image)
    const markersParsed = data.markers.map(m => ({
        id: m.id,
        latitude: m.lat,
        longitude: m.lng,
        image: 'http://127.0.0.1:8000/static/web/marker.png',
        width: 50,
        height: 50,
      }))
    await markersPlugin.setMarkers(markersParsed)
  }catch(err){
    console.log(err)
  }
}
viewer.once('ready', () => {
  getImage(5)
})
markersPlugin.on('select-marker', (e, marker) => getImage(marker.id))
