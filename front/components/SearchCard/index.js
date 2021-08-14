import styles from './styles.module.css'
import AsyncSelect from 'react-select/async'
import { useState } from 'react'
import { useRouter } from 'next/router'

const SearchCard = ({ collection }) => {
  const [selectValue, setSelectValue] = useState('')
  const [radioValue, setRadioValue] = useState('scientific-names')
  const router = useRouter()

  const loadOptions = async (inputText, callback) => {
    const response = await fetch(
      `http://127.0.0.1:8000/museum/api/${radioValue}?name=${inputText}`
    )
    const data = await response.json()

    callback(data.map((e) => ({ label: e.name, value: e.id })))
  }

  const handleSelectChange = (value) => {
    console.log(value)
    setSelectValue(value)
  }

  const handleRadioChange = (e) => {
    setSelectValue('')
    setRadioValue(e.target.value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const radioValueFormatted =
      radioValue === 'scientific-names' ? 'scientificName' : radioValue
    router.push(
      `/records?collection=${collection}&${radioValueFormatted}=${selectValue.label}`
    )
  }

  return (
    <div className={styles.searchCard}>
      <form method="get" onSubmit={handleSubmit}>
        <div className="mb-3">
          <input
            defaultChecked="checked"
            id="id_level_0"
            name="level"
            type="radio"
            value="scientific-names"
            className="me-2"
            onChange={handleRadioChange}
          />
          <label htmlFor="id_level_0" className="me-4">
            Especie
          </label>
          <input
            id="id_level_1"
            name="level"
            type="radio"
            value="families"
            className="me-2"
            onChange={handleRadioChange}
          />
          <label htmlFor="id_level_1" className="me-4">
            Familia
          </label>
          <input
            id="id_level_2"
            name="level"
            type="radio"
            value="genus"
            className="me-2"
            onChange={handleRadioChange}
          />
          <label htmlFor="id_level_2">Genero</label>
        </div>
        <div className="mb-3">
          <AsyncSelect
            value={selectValue}
            placeholder="Buscar..."
            loadOptions={loadOptions}
            instanceId
            onChange={handleSelectChange}
            noOptionsMessage={() => 'No hay opciones'}
            loadingMessage={() => 'Cargando'}
            isClearable
          />
        </div>
        <div className="send-btn">
          <button type="submit" className={styles.btn}>
            Buscar
          </button>
        </div>
      </form>
      <style jsx>{`
        input[type='radio']:checked + label:before {
          background-clip: content-box;
          background-color: #e33b3b;
          padding: 3px;
        }
        input[type='radio'] + label:before {
          border: 2px solid #e1e1e1;
          border-radius: 50%;
          content: '';
          display: inline-block;
          height: 16px;
          margin-bottom: 2px;
          margin-right: 10px;
          vertical-align: middle;
          width: 16px;
        }
        input[type='radio'] {
          opacity: 0;
          margin-left: -20px;
        }
        label {
          cursor: pointer;
        }
      `}</style>
    </div>
  )
}

export default SearchCard
