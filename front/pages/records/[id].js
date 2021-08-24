import Layout from '@components/Layout'
import dynamic from 'next/dynamic'

const Map = dynamic(() => import('@components/Map'), { ssr: false })

const RecordDetail = record => {
  return (
    <Layout>
      <main>
        <div className='container my-5'>
          <div className='row'>
            <h1>
              {record.scientificName?.name}{' '}
              {record.scientificNameAuthorship?.name}
            </h1>
            <div className='col-lg-6'>
              <div className='row'>
                <h3>Información General</h3>
                <div className='col-6 fw-bold'>Número de Catálogo</div>
                <div className='col-6'>{record.catalogNumber}</div>
                <div className='col-6 fw-bold'>Registrado por</div>
                <div className='col-6'>{record.recordedBy?.name}</div>
                <div className='col-6 fw-bold'>Número del registro</div>
                <div className='col-6'>{record.recordNumber}</div>
                <div className='col-6 fw-bold'>Georrferenciado por</div>
                <div className='col-6'>{record.georeferencedBy}</div>
                <div className='col-6 fw-bold'>Identificado por</div>
                <div className='col-6'>{record.identifiedBy?.name}</div>
              </div>
              <div className='row'>
                <h3 className='mt-4'>Taxonomía</h3>
                <div className='col-6 fw-bold'>Reino</div>
                <div className='col-6'>{record.kingdom?.name}</div>
                <div className='col-6 fw-bold'>Phylum</div>
                <div className='col-6'>{record.phylum?.name}</div>
                <div className='col-6 fw-bold'>Clase</div>
                <div className='col-6'>{record.Class?.name}</div>
                <div className='col-6 fw-bold'>Orden</div>
                <div className='col-6'>{record.order?.name}</div>
                <div className='col-6 fw-bold'>Familia</div>
                <div className='col-6'>{record.family?.name}</div>
                <div className='col-6 fw-bold'>Género</div>
                <div className='col-6'>{record.genus?.name}</div>
                <div className='col-6 fw-bold'>Epiteto específico</div>
                <div className='col-6'>{record.specificEpithet?.name}</div>
                <div className='col-6 fw-bold'>Categoría</div>
                <div className='col-6'>{record.taxonRank?.name}</div>
                <div className='col-6 fw-bold'>
                  Autoría del nombre científico
                </div>
                <div className='col-6'>
                  {record.scientificNameAuthorship?.name}
                </div>
                <div className='col-6 fw-bold'>Código nomenclatural</div>
                <div className='col-6'>{record.nomenclaturalCode?.name}</div>
              </div>
              <div className='row'>
                <h3 className='mt-4'>Información geográfica</h3>
                <div className='col-6 fw-bold'>País</div>
                <div className='col-6'>{record.country?.name}</div>
                <div className='col-6 fw-bold'>Departamento</div>
                <div className='col-6'>
                  {record.county?.stateProvince?.name}
                </div>
                <div className='col-6 fw-bold'>Municipio</div>
                <div className='col-6'>{record.county?.name}</div>
                <div className='col-6 fw-bold'>Localidad</div>
                <div className='col-6'>{record.locality?.name}</div>
                <div className='col-6 fw-bold'>Altitud mínima (m)</div>
                <div className='col-6'>{record.minimumElevationInMeters}</div>
                <div className='col-6 fw-bold'>Altitud máxima (m)</div>
                <div className='col-6'>{record.maximumElevationInMeters}</div>
                <div className='col-6 fw-bold'>Latitud (georreferenciada)</div>
                <div className='col-6'>{record.verbatimLatitude}</div>
                <div className='col-6 fw-bold'>Longitud (georreferenciada)</div>
                <div className='col-6'>{record.verbatimLongitude}</div>
                <div className='col-6 fw-bold'>Latitud decimal</div>
                <div className='col-6'>{record.decimalLatitude}</div>
                <div className='col-6 fw-bold'>Longitud decimal</div>
                <div className='col-6'>{record.decimalLongitude}</div>
                <div className='col-6 fw-bold'>Datum geodésico</div>
                <div className='col-6'>{record.geodeticDatum}</div>
              </div>
            </div>
            <div className='col-lg-6'>
              <div className='row'>
                <div className='col-12'>
                  <Map
                    coords={{
                      lat: record.decimalLatitude,
                      lng: record.decimalLongitude,
                    }}
                  />
                </div>
                <div className='col-12 mt-4'>
                  <img src={record.images[0]?.image} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  )
}

export default RecordDetail

export async function getServerSideProps({ query: { id } }) {
  const res = await fetch(`http://127.0.0.1:8000/museum/api/records/${id}`)
  const data = await res.json()
  return {
    props: data,
  }
}
