import Layout from '@components/Layout'
import Error from 'next/error'
import Image from 'next/image'

const Member = ({ error, member }) => {
  console.log(member)
  if (error) {
    return <Error statusCode={error} />
  }

  return (
    <Layout>
      <main>
        <div className='container pt-100 pb-70'>
          <div className='row'>
            <div className='section-title'>
              <h3>{member.name}</h3>
              <p>{member.position}</p>
            </div>
            <div className='col-12 col-md-4 mb-4'>
              <Image
                src={member.image}
                alt='image'
                width={500}
                height={500}
                objectFit={'cover'}
              />
            </div>
            <div
              className='col-12 col-md-8'
              dangerouslySetInnerHTML={{ __html: member.description }}
            ></div>
          </div>
        </div>
      </main>
    </Layout>
  )
}

export default Member

export async function getServerSideProps({ query: { slug } }) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_HOST}/members/${slug}`)
  const error = res.ok ? false : res.status
  const data = await res.json()
  return {
    props: { error, member: data },
  }
}
