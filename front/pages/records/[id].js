import Layout from '@components/Layout'

const RecordDetail = (record) => {
  console.log(record)
  return (
    <Layout>
      <main>
        <div className="container mt-5">{record.catalogNumber}</div>
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
