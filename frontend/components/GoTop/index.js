import { useState, useEffect } from 'react'

const GoTop = () => {
  const [isVisible, setIsVisible] = useState(false)

  const toggleVisibility = () => {
    if (window.pageYOffset > 300) {
      setIsVisible(true)
    } else {
      setIsVisible(false)
    }
  }

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    })
  }

  useEffect(() => {
    document.addEventListener('scroll', function () {
      toggleVisibility()
    })
  })

  return (
    <div className="back-to-top">
      {isVisible && (
        <div className="top" onClick={scrollToTop}>
          <i className="fas fa-chevron-up"></i>
          <i className="fas fa-chevron-up"></i>
        </div>
      )}
    </div>
  )
}

export default GoTop
