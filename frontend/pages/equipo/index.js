import Layout from '@components/Layout'
import TeamMember from '@components/TeamMember'
import Link from 'next/link'

const Members = ({ results: members }) => {
  return (
    <Layout>
      <main>
        <div className='container pt-100 pb-70'>
          <div className='section-title'>
            <h3>Conoce nuestro equipo</h3>
          </div>
          <div className='row justify-content-center'>
            {members.map(member => (
              <div className='col-12 col-sm-6 col-lg-4 mb-4' key={member.id}>
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
        </div>
      </main>
    </Layout>
  )
}

export default Members

export async function getServerSideProps() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_HOST}/members`)
  const data = await res.json()
  return {
    props: data,
  }
}
