import { useState } from 'react'
import Image from 'next/image'
import Link from '../../utils/ActiveLink'

const Navbar = () => {
  const [isCollapsed, setIsCollapsed] = useState(true)

  const toggleNavbar = () => {
    setIsCollapsed(!isCollapsed)
  }

  const classOne = isCollapsed
    ? 'collapse navbar-collapse'
    : 'collapse navbar-collapse show'
  const classTwo = isCollapsed
    ? 'navbar-toggler navbar-toggler-right collapsed'
    : 'navbar-toggler navbar-toggler-right'

  return (
    <>
      <header id='navbar' className='navbar-area is-sticky'>
        <div className='neemo-nav'>
          <div className='container'>
            <nav className='navbar navbar-expand-md navbar-light'>
              <Link href='/'>
                <a className='navbar-brand d-flex align-items-center'>
                  <Image
                    src='/images/logo.png'
                    alt='logo'
                    width={30}
                    height={30}
                  />
                  <span id='mhnu'>MHNU</span>
                </a>
              </Link>

              <button
                onClick={toggleNavbar}
                className={classTwo}
                type='button'
                data-toggle='collapse'
                data-target='#navbarSupportedContent'
                aria-controls='navbarSupportedContent'
                aria-expanded='false'
                aria-label='Toggle navigation'
              >
                <span className='icon-bar top-bar'></span>
                <span className='icon-bar middle-bar'></span>
                <span className='icon-bar bottom-bar'></span>
              </button>

              <div className={classOne} id='navbarSupportedContent'>
                <ul className='navbar-nav'>
                  <li className='nav-item'>
                    <Link href='/' activeClassName='active'>
                      <a className='nav-link'>Inicio</a>
                    </Link>
                  </li>

                  <li className='nav-item'>
                    <Link href='/colecciones' activeClassName='active'>
                      <a className='nav-link'>Colecciones</a>
                    </Link>
                  </li>

                  <li className='nav-item'>
                    <Link href='/equipo' activeClassName='active'>
                      <a className='nav-link'>Equipo</a>
                    </Link>
                  </li>

                  <li className='nav-item'>
                    <Link href='/contacto' activeClassName='active'>
                      <a className='nav-link'>Contacto</a>
                    </Link>
                  </li>
                </ul>
              </div>
            </nav>
          </div>
        </div>
      </header>
      <style jsx>{`
        #mhnu {
          color: #e33b3b;
          font-weight: bold;
          margin-left: 5px;
          font-size: 25px;
        }

        #navbar {
          -webkit-box-shadow: 0 0 15px 0 rgb(0 0 0 / 10%);
          box-shadow: 0 0 15px 0 rgb(0 0 0 / 10%);
        }
      `}</style>
    </>
  )
}

export default Navbar
