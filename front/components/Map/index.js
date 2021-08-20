import { MapContainer, TileLayer, Marker } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'

const icon = L.icon({ iconUrl: '/images/marker-icon.png' })

const Map = ({ coords }) => (
  <MapContainer
    center={coords}
    zoom={14}
    // scrollWheelZoom={false}
    style={{ height: 400, width: '100%' }}
  >
    <TileLayer
      attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    />
    <Marker position={coords} icon={icon}></Marker>
  </MapContainer>
)

export default Map
