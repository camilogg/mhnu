import Image from 'next/image'

const TeamMember = ({ image, name, position, description }) => {
  return (
    <div className='team-item-area'>
      <div className='team-image'>
        <Image
          src={image}
          alt='image'
          width={500}
          height={500}
          objectFit={'cover'}
        />
      </div>
      <div className='team-content'>
        <h3>{name}</h3>
        <p>{position}</p>
      </div>
    </div>
  )
}

export default TeamMember
