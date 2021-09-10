import { Swiper, SwiperSlide } from 'swiper/react'
import Image from 'next/image'

import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/navigation'

import SwiperCore, { Autoplay, Pagination } from 'swiper'

SwiperCore.use([Autoplay, Pagination])

const Slider = ({ sliders }) => {
  return (
    <Swiper
      loop={true}
      autoplay={{ delay: 4000, disableOnInteraction: false }}
      pagination={{ clickable: true }}
      lazy={true}
    >
      {sliders.map(slider => {
        return (
          <SwiperSlide key={slider.id}>
            <Image
              src={slider.image}
              alt={slider.name}
              width={1920}
              height={905}
              objectFit={'cover'}
            />
          </SwiperSlide>
        )
      })}
    </Swiper>
  )
}

export default Slider
