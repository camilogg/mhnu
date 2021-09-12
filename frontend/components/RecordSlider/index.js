import { Swiper, SwiperSlide } from 'swiper/react'
import Image from 'next/image'

import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/navigation'

import { Pagination, Navigation } from 'swiper'

const RecordSlider = ({ sliders }) => {
  return (
    <Swiper
      loop={true}
      pagination={{ clickable: true, dynamicBullets: true }}
      lazy={true}
      modules={[Pagination, Navigation]}
      navigation={true}
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
              objectFit='contain'
            />
          </SwiperSlide>
        )
      })}
    </Swiper>
  )
}

export default RecordSlider
