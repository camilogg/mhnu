import Layout from '../components/Layout'

const Home = () => {
  return (
    <Layout>
      <main>
        <div className='container'>
          <div className='row'>asdf</div>
        </div>
        <div className='container'>
          <div className='row'>asdf</div>
        </div>
        <div className='container'>
          <div className='row'>asdf</div>
        </div>
      </main>
      <style jsx>{`
        div > .row {
          padding-top: 300px;
        }
      `}</style>
    </Layout>
  )
}

export default Home
