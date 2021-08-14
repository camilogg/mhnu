import Layout from '@components/Layout'
import { useRouter } from 'next/router'
import { useMemo, useState, useRef, useCallback } from 'react'
import Table from '@components/Table'

const Records = ({
  results,
  count,
  next,
  previous,
  collection,
  genus,
  family,
  scientificName,
}) => {
  const router = useRouter()
  const [data, setData] = useState(results)
  const [loading, setLoading] = useState(false)
  const [pageCount, setPageCount] = useState(0)
  const fetchIdRef = useRef(0)
  const columns = useMemo(
    () => [
      {
        Header: 'Catálogo',
        accessor: 'catalogNumber',
      },
      {
        Header: 'Tipo',
        accessor: 'type.name',
      },
      {
        Header: 'Registrado por',
        accessor: 'recordedBy.name',
      },
      {
        Header: 'País',
        accessor: 'country.name',
      },
      {
        Header: 'Departamento',
        accessor: 'county.stateProvince.name',
      },
      {
        Header: 'Municipio',
        accessor: 'county.name',
      },
      {
        Header: 'Detalles',
        accessor: 'id',
        Cell: function button({ row }) {
          return (
            <button
              className='btn btn-danger btn-sm'
              onClick={() => handleClick(row.original.id)}
            >
              Ver
            </button>
          )
        },
      },
    ],
    []
  )

  const handleClick = id => {
    router.push(`/records/${id}`)
  }

  const fetchData = useCallback(async ({ pageIndex }) => {
    // This will get called when the table needs new data
    // You could fetch your data from literally anywhere,
    // even a server.

    // Give this fetch an ID
    const fetchId = ++fetchIdRef.current

    // Set the loading state
    setLoading(true)

    // Only update the data if this is the latest fetch
    if (fetchId === fetchIdRef.current) {
      const response = await fetch(
        `http://127.0.0.1:8000/museum/api/records?collection=${collection}&genus=${genus}&family=${family}&scientific_name=${scientificName}&limit=${8}&offset=${
          8 * pageIndex
        }`
      )
      const fetchData = await response.json()
      setData(fetchData.results)
      setPageCount(count)
      setLoading(false)
    }
  }, [])

  return (
    <Layout>
      <main>
        <div className='container mt-5'>
          <div className='row mt-4'>
            <h3>
              {count === 1
                ? 'Se encontró 1 resultado'
                : `Se encontraron ${count} resultados`}
            </h3>
            <div className='col-md-12'>
              <Table
                columns={columns}
                data={data}
                fetchData={fetchData}
                loading={loading}
                pageCount={pageCount}
              />
            </div>
          </div>
        </div>
      </main>
    </Layout>
  )
}

export default Records

export async function getServerSideProps({ query }) {
  const {
    collection = '',
    genus = '',
    family = '',
    scientificName = '',
  } = query
  const response = await fetch(
    `http://127.0.0.1:8000/museum/api/records?collection=${collection}&genus=${genus}&family=${family}&scientific_name=${scientificName}`
  )
  const data = await response.json()
  return {
    props: {
      ...data,
      collection,
      genus,
      family,
      scientificName,
    },
  }
}
