import Layout from '@components/Layout'
import Table from '@components/Table'
import Select from 'react-select'
import { useMemo, useState, useCallback, useEffect } from 'react'
import { useRouter } from 'next/router'
import AsyncSelect from 'react-select/async'

const COLLECTIONS = [
  {
    label: 'Entomológica',
    value: 'MHNU-E',
  },
  {
    label: 'Herpetológica',
    value: 'MHNU-H',
  },
  {
    label: 'Ictiológica',
    value: 'MHNU-I',
  },
  {
    label: 'Macroinvertebrados',
    value: 'MHNU-MA',
  },
  {
    label: 'Mastozoológica',
    value: 'MHNU-M',
  },
  {
    label: 'Ornitológica',
    value: 'MHNU-O',
  },
  {
    label: 'Tejidos',
    value: 'MHNU-CT',
  },
]

const FILTERS = [
  {
    label: 'Especie',
    value: 'scientific-names',
  },
  {
    label: 'Familia',
    value: 'families',
  },
  {
    label: 'Género',
    value: 'genus',
  },
]

const SEARCH_FILTERS = {
  'scientific-names': 'scientific_name',
  families: 'family',
  genus: 'genus',
}

const Collections = () => {
  const router = useRouter()
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(false)
  const [pageCount, setPageCount] = useState(0)
  const [isSearchSelectDisable, setIsSearchSelectDisable] = useState(true)
  const [collection, setCollection] = useState(null)
  const [filter, setFilter] = useState(null)
  const [search, setSearch] = useState(null)

  const columns = useMemo(
    () => [
      {
        Header: '# Catálogo',
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

  const handleClick = id => router.push(`/records/${id}`)

  const loadOptions = async (inputText, callback) => {
    const response = await fetch(
      `http://127.0.0.1:8000/museum/api/${filter.value}?name=${inputText}&collection_code=${collection.value}`
    )
    const data = await response.json()
    callback(data.map(e => ({ label: e.name, value: e.id })))
  }

  const handleClickBtnSearch = async () => {
    setLoading(true)
    const response = await fetch(
      `http://127.0.0.1:8000/museum/api/records?collection=${
        collection.value
      }&${SEARCH_FILTERS[filter.value]}=${search.label}`
    )
    const data = await response.json()
    setData(data.results)
    setPageCount(Math.ceil(data.count / 8))
    setLoading(false)
  }

  const handleClickBtnClear = () => {
    setCollection(null)
    setFilter(null)
    setSearch(null)
    setData([])
    setPageCount(0)
  }

  useEffect(() => {
    console.log('render from collections')
    if (collection && filter) {
      setIsSearchSelectDisable(false)
    } else {
      setIsSearchSelectDisable(true)
      setSearch(null)
      setData([])
    }
  }, [collection, filter])

  const fetchData = useCallback(
    async ({ pageIndex, collection, filter, search }) => {
      if (collection && filter && search) {
        // Set the loading state
        setLoading(true)
        const response = await fetch(
          `http://127.0.0.1:8000/museum/api/records?collection=${
            collection.value
          }&${SEARCH_FILTERS[filter.value]}=${search.label}&limit=${8}&offset=${
            8 * pageIndex
          }`
        )
        const fetchData = await response.json()
        setData(fetchData.results)
        setPageCount(Math.ceil(fetchData.count / 8))
        setLoading(false)
      }
    },
    []
  )

  return (
    <Layout>
      <main>
        <div className='container h-100 mt-4'>
          <div className='filters p-3 p-sm-4'>
            <div className='row'>
              <div className='col-12 col-md-12 col-lg-4 mb-2'>
                <label>Collección</label>
                <Select
                  className='basic-single'
                  classNamePrefix='select'
                  instanceId='collection'
                  isClearable
                  name='collection'
                  options={COLLECTIONS}
                  placeholder='Selecciona una colección...'
                  noOptionsMessage={() => 'No hay opciones'}
                  onChange={setCollection}
                  value={collection}
                />
              </div>
              <div className='col-12 col-md-12 col-lg-4 mb-2'>
                <label>Tipo de filtro</label>
                <Select
                  className='basic-single'
                  classNamePrefix='select'
                  instanceId='filter'
                  isClearable
                  isSearchable
                  name='filter'
                  options={FILTERS}
                  placeholder='Selecciona un tipo de filtro...'
                  noOptionsMessage={() => 'No hay opciones'}
                  onChange={setFilter}
                  value={filter}
                />
              </div>
              <div className='col-12 col-md-12 col-lg-4 mb-2'>
                <label>Buscar</label>
                <AsyncSelect
                  value={search}
                  placeholder='Buscar...'
                  loadOptions={loadOptions}
                  instanceId='search'
                  onChange={setSearch}
                  noOptionsMessage={() => 'No hay opciones'}
                  loadingMessage={() => 'Cargando'}
                  isClearable
                  isDisabled={isSearchSelectDisable}
                />
              </div>
            </div>
            <div className='row'>
              <div className='col-6 col-md-6 col-lg-2'>
                <button
                  className='btnSearch'
                  onClick={handleClickBtnSearch}
                  disabled={!search}
                >
                  Buscar
                </button>
              </div>
              <div className='col-6 col-md-6 col-lg-2'>
                <button className='btnClear' onClick={handleClickBtnClear}>
                  Limpiar
                </button>
              </div>
            </div>
          </div>
          <div className='row my-4'>
            <div className='col-12'>
              <Table
                columns={columns}
                data={data}
                fetchData={fetchData}
                loading={loading}
                pageCount={pageCount}
                collection={collection}
                filter={filter}
                search={search}
              />
            </div>
          </div>
        </div>
      </main>
      <style jsx>{`
        .filters {
          /* box-shadow: 2px 2px 4px hsl(0deg 0% 51% / 16%); */
          box-shadow: 7px 5px 30px rgb(72 73 121 / 15%);
          background-color: #fff;
          border-radius: 5px;
        }
        label {
          font-weight: bold;
        }
        .btnSearch {
          display: inline-block;
          padding: 6px 30px;
          color: #fff;
          text-transform: capitalize;
          background-color: #e33b3b;
          border: 1px solid #e33b3b;
          -webkit-transition: 0.5s;
          transition: 0.5s;
          border-radius: 5px;
          font-size: 16px;
          font-weight: 500;
          width: 100%;
        }
        .btnSearch:disabled {
          background-color: #eaeaea;
          color: #6a6c72;
          border-color: #eaeaea;
        }
        .btnClear {
          display: inline-block;
          padding: 6px 30px;
          color: #e33b3b;
          text-transform: capitalize;
          background-color: #fff;
          border: 1px solid #e33b3b;
          -webkit-transition: 0.5s;
          transition: 0.5s;
          border-radius: 5px;
          font-size: 16px;
          font-weight: 500;
          width: 100%;
        }
      `}</style>
    </Layout>
  )
}

export default Collections
