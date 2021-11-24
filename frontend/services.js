const HOST = process.env.NEXT_PUBLIC_HOST

export const getSliders = async () => {
  const response = await fetch(`${HOST}/sliders`)
  return await response.json()
}

export const getMembers = async () => {
  const response = await fetch(`${HOST}/members?limit=6`)
  return await response.json()
}

export const sendContact = async data => {
  return await fetch(`${HOST}/contact`, {
    method: 'post',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' },
  })
}
