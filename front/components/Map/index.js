import { MapContainer, TileLayer } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import styles from './Map.module.css'

const Map = () => (
  <MapContainer
    center={[4.1248423, -73.6441654]}
    zoom={14}
    // scrollWheelZoom={false}
    className={styles.map}
  >
    <TileLayer
      attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    />
  </MapContainer>
)

export default Map
