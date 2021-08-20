import { useTable, usePagination } from 'react-table'
import { Styles } from './styles'
import { useEffect } from 'react'

const Table = ({
  columns,
  data,
  fetchData,
  loading,
  pageCount: controlledPageCount,
}) => {
  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    page,
    canPreviousPage,
    canNextPage,
    pageOptions,
    pageCount,
    gotoPage,
    nextPage,
    previousPage,
    // Get the state from the instance
    state: { pageIndex },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0 }, // Pass our hoisted table state
      manualPagination: true, // Tell the usePagination
      // hook that we'll handle our own data fetching
      // This means we'll also have to provide our own
      // pageCount.
      pageCount: controlledPageCount,
    },
    usePagination
  )

  useEffect(() => {
    console.log('render form Table')
    fetchData({ pageIndex })
  }, [fetchData, pageIndex])

  return (
    <Styles>
      <div className='tableWrap'>
        <table {...getTableProps()}>
          <thead>
            {headerGroups.map(headerGroup => {
              const { key, ...restHeaderGroupProps } =
                headerGroup.getHeaderGroupProps()
              return (
                <tr key={key} {...restHeaderGroupProps}>
                  {headerGroup.headers.map(column => {
                    const { key, ...restColumn } = column.getHeaderProps({
                      className: column.collapse ? 'collapse' : '',
                    })
                    return (
                      <th key={key} {...restColumn}>
                        {column.render('Header')}
                      </th>
                    )
                  })}
                </tr>
              )
            })}
          </thead>
          <tbody {...getTableBodyProps()}>
            {page.map(row => {
              prepareRow(row)
              const { key, restRow } = row.getRowProps()
              return (
                <tr key={key} {...restRow}>
                  {row.cells.map(cell => {
                    const { key, restCell } = cell.getCellProps({
                      className: cell.column.collapse ? 'collapse' : '',
                    })
                    return (
                      <td key={key} {...restCell}>
                        {cell.render('Cell')}
                      </td>
                    )
                  })}
                </tr>
              )
            })}
            <tr>
              {loading && (
                // Use our custom loading state to show a loading indicator
                <td colSpan='10000'>Cargando...</td>
              )}
            </tr>
          </tbody>
        </table>
      </div>
      <div className='pagination row'>
        <div className='d-flex mb-2 justify-content-center'>
          <button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
            <i className='fas fa-angle-double-left'></i>
          </button>
          <button onClick={() => previousPage()} disabled={!canPreviousPage}>
            <i className='fas fa-angle-left'></i>
          </button>
          <button onClick={() => nextPage()} disabled={!canNextPage}>
            <i className='fas fa-angle-right'></i>
          </button>
          <button
            onClick={() => gotoPage(pageCount - 1)}
            disabled={!canNextPage}
          >
            <i className='fas fa-angle-double-right'></i>
          </button>
        </div>
        {!!pageOptions.length && (
          <div className='text-center'>
            <span>
              Página{' '}
              <strong>
                {pageIndex + 1} de {pageOptions.length}
              </strong>{' '}
            </span>
            <span>
              | Ir a la página:{' '}
              <input
                type='number'
                value={pageIndex + 1}
                onChange={e => {
                  const page = e.target.value ? Number(e.target.value) - 1 : 0
                  gotoPage(page)
                }}
                style={{ width: '50px' }}
              />
            </span>{' '}
          </div>
        )}
      </div>
    </Styles>
  )
}

export default Table
