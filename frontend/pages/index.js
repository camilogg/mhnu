import dynamic from 'next/dynamic'
import Layout from '@components/Layout'
import { getSliders } from 'services'
// import { getMembers, getSliders } from 'services'
// import TeamMember from '@components/TeamMember'
// import Link from 'next/link'

const Slider = dynamic(() => import('@components/Slider'), { ssr: false })

const Home = ({ sliders, members }) => {
  return (
    <Layout>
      <main>
        {!!sliders.length && <Slider sliders={sliders} />}
        <section className='container pt-100 pb-70'>
          <div className='section-title'>
            <h3>Misión</h3>
          </div>
          <p>
            Fomentar en la comunidad en general la apropiación de la diversidad
            biológica característica de la Orinoquia a través de la
            investigación científica y la educación. Esto incluye la
            preservación de una muestra del patrimonio natural nacional
            representada en especímenes biológicos de colecciones científicas,
            exhibiciones permanentes, temporales o itinerantes, y actividades
            educativas y didácticas que permitan promover su descubrimiento,
            estudio y divulgación.
          </p>
        </section>
        <section className='container pb-70'>
          <div className='section-title'>
            <h3>Visión</h3>
          </div>
          <p>
            El MHNU potenciará la investigación sobre la diversidad biológica
            nacional con énfasis en fauna de la Orinoquia colombiana, así como
            su conocimiento y acercamiento a la sociedad en general, esto
            mediante el apoyo a semilleros y grupos de investigación, íneas de
            profundización y convenios académicos, lo que permitirá consolidar
            al MHNU como referente de información sobre la biodiversidad
            regional, su uso y conservación.
          </p>
        </section>
        <section className='container pb-70'>
          <div className='section-title'>
            <h3>Servicios</h3>
          </div>
          <div className='row justify-content-center'>
            <div className='col-lg-4 col-md-6 col-sm-6'>
              <div className='single-services-box'>
                <div className='icon bg-faddd4'>
                  <i className='flaticon-landing-page'></i>
                </div>
                <h3>Visitas científicas</h3>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incutu labore et dolore magna aliqua.
                </p>
              </div>
            </div>
            <div className='col-lg-4 col-md-6 col-sm-6'>
              <div className='single-services-box'>
                <div className='icon bg-fcdeee'>
                  <i className='flaticon-goal'></i>
                </div>
                <h3>Visitas público en general</h3>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incutu labore et dolore magna aliqua.
                </p>
              </div>
            </div>
            <div className='col-lg-4 col-md-6 col-sm-6'>
              <div className='single-services-box'>
                <div className='icon bg-c5ebf9'>
                  <i className='flaticon-seo'></i>
                </div>
                <h3>Visitas educativas</h3>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incutu labore et dolore magna aliqua.
                </p>
              </div>
            </div>
            <div className='col-lg-4 col-md-6 col-sm-6'>
              <div className='single-services-box'>
                <div className='icon bg-cafbf1'>
                  <i className='flaticon-data-recovery'></i>
                </div>
                <h3>Transferencia de ejemplares y muestras del MHNU</h3>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incutu labore et dolore magna aliqua.
                </p>
              </div>
            </div>
            <div className='col-lg-4 col-md-6 col-sm-6'>
              <div className='single-services-box'>
                <div className='icon bg-ddd5fb'>
                  <i className='flaticon-contract'></i>
                </div>
                <h3>Depósito de especímenes y/o muestras al MHNU</h3>
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incutu labore et dolore magna aliqua.
                </p>
              </div>
            </div>
          </div>
        </section>
        {/* {members.length > 0 && (
          <section className='container pb-70'>
            <div className='section-title'>
              <h3>Conoce nuestro equipo</h3>
            </div>
            <div className='row justify-content-center'>
              {members.map(member => (
                <div className='col-lg-4 col-sm-6' key={member.id}>
                  {member.description ? (
                    <Link href={`/equipo/${member.slug}`}>
                      <a>
                        <TeamMember {...member} />
                      </a>
                    </Link>
                  ) : (
                    <TeamMember {...member} />
                  )}
                </div>
              ))}
            </div>
          </section>
        )} */}
      </main>
    </Layout>
  )
}

export default Home

export async function getServerSideProps() {
  // const [sliders, members] = await Promise.all([getSliders(), getMembers()])
  const [sliders] = await Promise.all([getSliders()])
  return {
    props: {
      sliders,
      // members: members.results,
    },
  }
}
