import Epub from "epubjs";
//框架是偷来的，所有语句结尾都不带分号，暂时没空改了，强迫症震怒(╯‵□′)╯︵┴─┴

export function useEpub() {
  let book
  let rendition
  let _element
  let _options
  let themeList = [
    {
      name: 'Light',
      style: {
        body:{
          'color': '#000',
          'background': '#FFF'
        }
      }
    },
    {
      name: 'Dark',
      style: {
        body:{
          'color': '#FFF',
          'background': '#000'
        }
      }
    }
  ]

  function createBook(urlOrData, options) {
    if (!urlOrData) {
      book = Epub(options)
    } else {
      book = Epub(urlOrData, options)
    }
    return book
  }

  /**实例化rendition */
  function render(element, options) {
    if (!book) {
      console.warn("book is undefined or null")
      return
    }
    if(rendition)
      rendition.destroy()
    rendition = book.renderTo(element, options)
    defaultStyleInit()
    rendition.display()
    _element = element
    _options = options
    test()
    return rendition
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

  /** 切换页面视图（连续/分页）
   * TODO: 记录阅读位置，否则切换时会从头开始
   */
  function setViewStyle() {
    if("flow" in _options)
      delete _options.flow
    else
      _options.flow = "scrolled-doc"
    render(_element, _options)
    return
  }

  function defaultStyleInit(){
    themeList.forEach(element => {
      rendition.themes.register(element.name, element.style)
    });
    // rendition.themes.default(themeList[0].style)
    return
  }

  function setTheme(index) {
    console.log("call setBackgroundColor, index = ", themeList[index].name)
    // debugger
    rendition.themes.select(themeList[index].name)
    return
  }

  /** 用于hack epubjs源码^^ */
  function test() {
    // debugger
    // rendition.themes.update();
    // debugger
  }

  return { createBook, render, getBook, getRendition, nextPage, prevPage , setFontSize, setViewStyle, test, setTheme}
}