import Layout from '@components/Layout'
import dynamic from 'next/dynamic'

const Map = dynamic(() => import('@components/Map'), { ssr: false })

const Contact = () => {
  return (
    <Layout>
      <main>
        <section className='contact-area ptb-100'>
          <div className='container'>
            <Map
              coords={{
                lat: 4.1551704,
                lng: -73.6428228,
              }}
            />
          </div>
        </section>
      </main>
    </Layout>
  )
}

export default Contact
