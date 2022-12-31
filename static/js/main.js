function clickWord(clickedElementOrWord) {
  // console.log({clickedElementOrWord})
  const wordString = typeof clickedElementOrWord === 'string'
    ? clickedElementOrWord
    : (() => {
      const clickedElement = clickedElementOrWord
      const clickedLink = clickedElement.tagName = 'A' ? clickedElement : clickedElement.parentChild
      return clickedElement.dataset.word || ''
    })()
  // console.log({clickedElementOrWord})
  const [word, pos = null] = wordString.split('/')

  // console.log({pos, word})
  const body = JSON.stringify({pos, word})
  // console.log({body})
  const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
  fetch('/addword', {method: 'POST', body, headers}).then((response) => {
    // console.log(response.json())
    const json = response.json()
    // console.log({json})
    if (json.word) {
      const newWordUrl = `/${encodeURI(json.word)}`
      if (confirm(`Redirect to ${newWordUrl}`)) window.location = newWordUrl
    }
    // const content = await rawResponse.json();
    // do a thing?
    // console.log('we fetched', fnord)
  })
}

// function clickRelephant(relephant) {
function clickRelephant(clickedElement) {
  // console.log('clickRelephant', {clickedElement})
  clickWord(clickedElement)
  // console.log('clickRelephant', relephant)
}
