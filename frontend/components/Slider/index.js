import { Swiper, SwiperSlide } from 'swiper/react'
import Image from 'next/image'

import 'swiper/css'
import 'swiper/css/pagination'

import { Autoplay, Pagination } from 'swiper'

const Slider = ({ sliders }) => {
  return (
    <Swiper
      loop={true}
      autoplay={{ delay: 4000, disableOnInteraction: false }}
      pagination={{ clickable: true, dynamicBullets: true }}
      lazy={true}
      modules={[Autoplay, Pagination]}
    >
      {sliders.map(slider => {
        return (
          <SwiperSlide key={slider.id}>
            <Image
              src={slider.image}
              alt={slider.name}
              width={16}
              height={9}
              layout='responsive'
              objectFit='cover'
            />
          </SwiperSlide>
        )
      })}
    </Swiper>
  )
}

export default Slider
