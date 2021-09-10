import Image from 'next/image'

const Team = ({ members }) => {
  return (
    <section className='container pb-70'>
      <div className='section-title'>
        <h3>Conoce nuestro equipo</h3>
      </div>
      <div className='row justify-content-center'>
        {members.map(member => {
          return (
            <div className='col-lg-4 col-sm-6' key={member.id}>
              <div className='team-item-area'>
                <div className='team-image'>
                  <Image
                    src={member.image}
                    alt='image'
                    width={500}
                    height={500}
                    objectFit={'cover'}
                  />
                </div>
                <div className='team-content'>
                  <h3>{member.name}</h3>
                  <span>{member.position}</span>
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </section>
  )
}

export default Team
