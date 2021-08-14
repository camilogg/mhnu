import Layout from '@components/Layout'
import SearchCard from '@components/SearchCard'

const Herpetologica = () => {
  return (
    <Layout>
      <main>
        <div className="container h-100">
          <div className="row h-100 justify-content-center align-items-center">
            <div className="col-md-8 col-lg-5 col-xl-4">
              <SearchCard collection="MHNU-E" />
            </div>
          </div>
        </div>
      </main>
      <style jsx>{`
        main {
          background-color: #f4f5f8;
          {/* background-image: url('http://www.biovirtual.unal.edu.co/static/amphibians.jpg');
          background-size: cover;
          background-repeat: no-repeat; */}
        `}</style>
    </Layout>
  )
}

export default Herpetologica
