import '../public/css/bootstrap.min.css'
import '../public/css/fontawesome.min.css'
import '../public/css/flaticon.css'
import 'animate.css'
import 'react-accessible-accordion/dist/fancy-example.css'
import '../styles/global.css'
import '../public/css/responsive.css'
import GoTop from '../components/GoTop'
import Head from 'next/head'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Museo de Historia Natural Unillanos</title>
        <meta
          name="description"
          content="Museo de Historia Natural Unillanos"
        />
      </Head>
      <Component {...pageProps} />
      <GoTop />
    </>
  )
}

export default MyApp
