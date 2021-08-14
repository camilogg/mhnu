import Layout from '@components/Layout'
import Link from 'next/link'
import { useState } from 'react'
import Swal from 'sweetalert2'

const Contact = () => {
  const [contactData, setContactData] = useState({})

  const { names = '', email = '', subject = '', message = '' } = contactData

  const handleSubmit = async (e) => {
    e.preventDefault()
    setContactData({})
    try {
      const response = await fetch('http://127.0.0.1:8000/museum/api/contact', {
        method: 'post',
        body: JSON.stringify(contactData),
        headers: { 'Content-Type': 'application/json' },
      })
      if (response.ok) {
        Swal.fire({
          title: '¡Tu mensaje ha sido enviado!',
          text: 'Pronto nos pondremos en contacto contigo',
          icon: 'success',
          showConfirmButton: false,
          timer: 2000,
        })
      } else {
        Swal.fire({
          title: '¡Ha ocurrido un error!',
          text: 'Intenta de nuevo más tarde',
          icon: 'error',
          showConfirmButton: false,
          timer: 2000,
        })
      }
    } catch {
      Swal.fire({
        title: '¡Ha ocurrido un error!',
        text: 'Intenta de nuevo más tarde',
        icon: 'error',
        showConfirmButton: false,
        timer: 2000,
      })
    }
  }

  const handleChange = (e) => {
    setContactData({
      ...contactData,
      [e.target.name]: e.target.value,
    })
  }

  return (
    <Layout>
      <main>
        <section className="contact-area ptb-100">
          <div className="container">
            {/* Contact Info */}
            <div className="row">
              <div className="col-lg-4 col-md-12">
                <div className="contact-box">
                  <div className="icon">
                    <i className="fa fa-phone"></i>
                  </div>
                  <div className="content">
                    <h4>Teléfono/Fax</h4>
                    <p>+57 (8) 6616800 ext: 204</p>
                    <p>+57 (8) 6616800 ext: 204</p>
                  </div>
                </div>
              </div>

              <div className="col-lg-4 col-md-12">
                <div className="contact-box">
                  <div className="icon">
                    <i className="fas fa-envelope"></i>
                  </div>
                  <div className="content">
                    <h4>Correo</h4>
                    <p>contacto@unillanos.edu.co</p>
                    <p>contacto@unillanos.edu.co</p>
                  </div>
                </div>
              </div>

              <div className="col-lg-4 col-md-12">
                <div className="contact-box">
                  <div className="icon">
                    <i className="fa fa-map-marker"></i>
                  </div>
                  <div className="content">
                    <h4>Ubicación</h4>
                    <p>Km. 12 Vía Puerto López - PBX. +57 (8) 6616800</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Contact Form */}
            <div className="row align-items-center">
              <div className="col-lg-6 col-md-6">
                <div className="contact-text">
                  <h3>Get in Touch</h3>
                  <p>
                    Orci varius natoque penatibus et magnis dis parturient
                    montes, nascetur ridiculus mus. Etiam tempus magna vel
                    turpis pharetra dictum.
                  </p>
                  <p>
                    Sed blandit tempus purus, sed sodales leo rutrum vel. Nam
                    vulputate ipsum ac est congue, eget commodo magna lobortis.
                  </p>

                  <ul className="social-links">
                    <li>
                      <Link href="/contact/#">
                        <a>
                          <i className="fab fa-facebook-f"></i>
                        </a>
                      </Link>
                    </li>
                    <li>
                      <Link href="/contact/#">
                        <a>
                          <i className="fab fa-twitter"></i>
                        </a>
                      </Link>
                    </li>
                    <li>
                      <Link href="/contact/#">
                        <a>
                          <i className="fab fa-instagram"></i>
                        </a>
                      </Link>
                    </li>
                    <li>
                      <Link href="/contact/#">
                        <a>
                          <i className="fab fa-linkedin"></i>
                        </a>
                      </Link>
                    </li>
                    <li>
                      <Link href="/contact/#">
                        <a>
                          <i className="fab fa-pinterest"></i>
                        </a>
                      </Link>
                    </li>
                  </ul>
                </div>
              </div>

              <div className="col-lg-6 col-md-6">
                <form id="contactForm" method="post" onSubmit={handleSubmit}>
                  <div className="row">
                    <div className="col-lg-6 col-md-12">
                      <div className="form-group">
                        <input
                          type="text"
                          className="form-control"
                          placeholder="Nombres"
                          name="names"
                          onChange={handleChange}
                          required
                          value={names}
                        />
                      </div>
                    </div>
                    <div className="col-lg-6 col-md-12">
                      <div className="form-group">
                        <input
                          type="email"
                          className="form-control"
                          placeholder="Correo"
                          name="email"
                          onChange={handleChange}
                          required
                          value={email}
                        />
                      </div>
                    </div>
                  </div>

                  <div className="form-group">
                    <input
                      type="text"
                      className="form-control"
                      placeholder="Asunto"
                      name="subject"
                      onChange={handleChange}
                      required
                      value={subject}
                    />
                  </div>

                  <div className="form-group">
                    <textarea
                      name="message"
                      className="form-control"
                      placeholder="Tu mensaje"
                      onChange={handleChange}
                      required
                      value={message}
                    ></textarea>
                  </div>

                  <div className="send-btn">
                    <button type="submit" className="send-btn-one">
                      Enviar
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  )
}

export default Contact
