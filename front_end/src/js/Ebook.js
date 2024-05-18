import Epub from "epubjs";
//框架是偷来的，所有语句结尾都不带分号，暂时没空改了，强迫症震怒(╯‵□′)╯︵┴─┴

export function useEpub() {
  /**.epub文件所解析出的实例 */
  let book
  /**由book渲染出的页面实例   */
  let rendition
  /**渲染参数 */
  let element
  /**渲染参数 */
  let options
  /**book中所有cfi标识符
   * 好像存起来也没啥用，先存着吧
   */
  let locations
  /**目录  */
  let navigation
  /**在切换渲染参数前储存当前阅读位置
   * 后续可以考虑缓存该属性
   */
  let currentLocation
  let isLocationLoadFinished = false
  let cfiRange
  let contents
  let takeNoteType = 'underline'
  let takeNoteAvailable = false
  let themeList = [
    {
      name: 'Light',
      style: {
        body: {
          'color': '#000',
          'background': '#FFF'
        }
      }
    },
    {
      name: 'Dark',
      style: {
        body: {
          'color': '#FFF',
          'background': '#000'
        }
      }
    }
  ]
  let underlineStyle = {
    style: {
      textDecoration: "underline",
      textDecorationStyle: "dashed",
      textDecorationColor: "pink"
    }
    
  }

  console.log(underlineStyle)

  function createBook(_urlOrData, _options) {
    console.log("Book init...")
    if (!_urlOrData) {
      book = Epub(_options)
    } else {
      book = Epub(_urlOrData, _options)
    }
    book.ready
      .then(() => {
        navigation = book.navigation
        console.log(navigation)
        console.log("Location init...")
        return book.locations.generate()
      })
      .then(() => {
        console.log("Location init finished")
        isLocationLoadFinished = true
        locations = book.locations
      })
    return book
  }

  /**实例化rendition */
  function render(_element, _options) {
    if (!book) {
      console.warn("book is undefined or null")
      return
    }
    if (rendition) {
      currentLocation = rendition.currentLocation()
      console.log("储存currentLocation")
      rendition.destroy()
    }
    rendition = book.renderTo(_element, _options)
    // console.log(options)
    defaultStyleInit()
    if (currentLocation) {
      console.log("检测到缓存Location:", currentLocation)
      rendition.display(currentLocation.start.cfi)
    }
    else {
      console.log("未发现缓存Location")
      rendition.display()
    }
    element = _element
    options = _options
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
   * TODO: 有些epub文件似乎并不兼容这种切换模式，原因尚不清楚
   */
  function setViewStyle() {
    if ("flow" in options)
      delete options.flow
    else
      options.flow = "scrolled-doc"
    render(element, options)
    return
  }

  function defaultStyleInit() {
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

  /**设置页码
   * TODO: 与GUI的对接、兼容输入页码模式
   */
  function setPage(progress) {
    const percentage = progress / 100
    console.log(percentage)
    const location = locations.cfiFromPercentage(percentage)
    rendition.display(location)
  }

  function setForNote(_cfiRange, _contents) {
    cfiRange = _cfiRange
    contents = _contents
    console.log(cfiRange, contents)
    console.log(takeNoteAvailable)
    if (takeNoteAvailable)
      takeNote()
  }

  /**TODO: 几乎解决了自定义样式的问题，下划线颜色似乎无法编辑，尝试修改epubjs源码(?)
   * epubjs中编辑样式是使用svg来实现的
   */
  function takeNote() {
    console.log("try to take note")
    if (cfiRange) {
      // let marker
      // let range
      switch (takeNoteType) {
        case 'highlight':
          rendition.annotations.highlight(cfiRange, {}, () => {}, null, {
            "fill": 'pink'
          });
          break;
        case 'underline':
          // debugger
          rendition.annotations.underline(cfiRange, {}, () => {}, null, {
            "stroke": 'transparent',
            "stroke-opacity": "0.8",
            "mix-blend-mode": "normal"
          })
          break;
        default:
          console.error("unkown operation")
          break;
      }
      contents.window.getSelection().removeAllRanges();
      cfiRange = null
      takeNoteAvailable = false
    }
    else
      console.warn("cfiRange is undefined")
  }

  function setTakeNoteAvailable() {
    takeNoteAvailable = true
  }

  /**用于hack epubjs源码^^
   * 或是一些临时的测试函数
   */
  function test(parameter) {
    console.log(parameter)
    setInterval(() => {
      if (isLocationLoadFinished)
        console.log(rendition.markClicked)
      console.log(rendition.selected)
    }, 1000)
  }

  function setLatedPage() {
    console.log("set page to currentLocation")
    rendition.display(currentLocation.start.cfi)
  }

  return {
    createBook, render, getBook, getRendition, nextPage, prevPage, setFontSize, setViewStyle, test, setTheme, setPage, setLatedPage,
    setForNote, takeNote, setTakeNoteAvailable
  }
}