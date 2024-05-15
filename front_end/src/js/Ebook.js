import Epub from "epubjs";
//框架是偷来的，所有语句结尾都不带分号，暂时没空改了，强迫症震怒(╯‵□′)╯︵┴─┴

export function useEpub() {
  let book
  let rendition

  function createBook(urlOrData, options) {
    if (!urlOrData) {
      book = Epub(options)
    } else {
      book = Epub(urlOrData, options)
    }
    return book
  }

  function render(element, options) {
    if (!book) {
      console.warn("book is undefined or null")
      return
    }
    rendition = book.renderTo(element, options)
    return rendition
  }

  function display() {
    if (!rendition) {
      console.warn("rendition is undefined or null")
      return
    }
    return rendition.display()
  }

  function getBook() {
    return book
  }

  function getRendition() {
    return rendition
  }

  function nextPage() {
    if (!rendition) {
      console.warn("rendition is undefined or null")
      return
    }
    rendition.next()
    return
  }

  function prevPage() {
    if (!rendition) {
      console.warn("rendition is undefined or null")
      return
    }
    rendition.prev()
    return
  }

  function setFontSize(fontSize) {
    if (!rendition) {
      console.warn("rendition is undefined or null")
      return
    }
    rendition.themes.fontSize(fontSize + 'px');
    return;
  }

  return { createBook, render, display, getBook, getRendition, nextPage, prevPage , setFontSize}
}