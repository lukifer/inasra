// function clickWord(word, pos) {
function clickWord(clickedElement) {
  debugger
  console.log({clickedElement})
  const clickedLink = clickedElement.tagName = 'A' ? clickedElement : clickedElement.parentChild
  console.log({clickedLink})
  const wordString = clickedElement.dataset.word || ''
  console.log({wordString})
  const [word, pos] = wordString.split('/')
  if (pos === undefined) return

  console.log({pos, word})
  const body = JSON.stringify({pos, word})
  // console.log({body})
  const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
  fetch('/addword', {method: 'POST', body, headers}).then((fnord) => {
    // const content = await rawResponse.json();
    // do a thing?
    console.log('we fetched', fnord)
  })
}

// function clickRelephant(relephant) {
function clickRelephant(clickedElement) {
  console.log({clickedElement})
  // console.log('clickRelephant', relephant)
}
