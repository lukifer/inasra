async function clickWord(clickedElementOrWord, endpoint = 'addword') {
  // console.log({clickedElementOrWord})
  const wordString = typeof clickedElementOrWord === 'string'
    ? clickedElementOrWord
    : (() => {
      const clickedElement = clickedElementOrWord
      const clickedLink = clickedElement.tagName = 'A' ? clickedElement : clickedElement.parentChild
      return clickedElement.dataset.word || ''
    })()
  const [word, pos = null] = wordString.split('/')

  // console.log({pos, word})
  const body = JSON.stringify({pos, word})
  // console.log({body})
  const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
  // TO LUKE AND DAFE NEXT TIME: fix the pos arg for words after the first
  // (AND maybe infer endpoint from whether pos is present or not)
  const response = await fetch(`/${endpoint}`, {method: 'POST', body, headers})
  response.json().then((json) => {
    if (json.word) {
      const newWordUrl = `/${encodeURI(json.word)}`
      if (confirm(`Redirect to ${newWordUrl}`)) window.location = newWordUrl
    }
  })
}

// function clickRelephant(relephant) {
function clickRelephant(clickedElement) {
  // console.log('clickRelephant', {clickedElement})
  clickWord(clickedElement)
  // console.log('clickRelephant', relephant)
}
