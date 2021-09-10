const Footer = () => {
  const currentYear = new Date().getFullYear()

  return (
    <div className='copyright-area'>
      <div className='container'>
        <div className='row'>
          <div className='col-12'>
            <p className='text-center'>
              © {currentYear}. Todos los derechos reservados por{' '}
              <a
                href='https://www.unillanos.edu.co/'
                target='_blank'
                rel='noreferrer'
              >
                Unillanos
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Footer
