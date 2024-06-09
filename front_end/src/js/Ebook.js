import Epub, { EpubCFI } from "epubjs";
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
  /**在切换渲染参数前储存当前阅读位置
   * 后续可以考虑缓存该属性
   */
  let currentLocation
  let isLocationLoadFinished = false
  let fillColorList = [//一些合理的颜色选择
    'yellow', 'green', 'pink', 'red'
  ]
  let fillColorIndex = 0
  let noteList = []
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
          'color': '#808080',
          'background': '#000'
        }
      }
    }
  ]

  function createBook(_urlOrData, _options) {
    console.log("Book init...")
    if (!_urlOrData) {
      book = Epub(_options)
    } else {
      book = Epub(_urlOrData, _options)
    }
    book.ready
      .then(() => {
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

  /**设置页码 */
  //TODO: 与GUI的对接、兼容输入页码模式
  function setPage(progress) {
    const percentage = progress / 100
    console.log(percentage)
    const location = locations.cfiFromPercentage(percentage)
    rendition.display(location)
  }


  /**epubjs中编辑样式是使用svg来实现的 */
  //TODO: 几乎解决了自定义样式的问题，但下划线颜色无法编辑
  function takeNote(takeNoteType, cfiRange) {
    console.log("try to take note")
    switch (takeNoteType) {
      case 'highlight':
        rendition.annotations.highlight(cfiRange, {}, () => { }, null, {
          "fill": fillColorList[fillColorIndex]
        });
        break;
      case 'underline':
        rendition.annotations.underline(cfiRange, {}, () => { }, null, {
          "stroke": 'transparent',
          "stroke-opacity": "0.8",
          "mix-blend-mode": "normal"
        })
        break;
      default:
        console.error("unkown operation")
        break;
    }
    noteList.push({ 'cfiRange': cfiRange, 'note': null, 'type': takeNoteType, isPublic: false })
    console.log("push cfiRange to noteList")

}

  function setFillColor(index) {
    fillColorIndex = index
  }

  function getIsLocationLoadFinished() {
    return isLocationLoadFinished
  } 

  function removeMark(cfiRange) {
    let note
    console.log("in Ebook.js, remove mark, note list: ", noteList)
    noteList.forEach(element => {
      console.log("note in noteList", element)
      if(element.cfiRange == cfiRange){
        note = element 
        rendition.annotations.remove(note.cfiRange, note.type)
        noteList.splice(noteList.indexOf(note), 1)
        console.log("after splice, note list: ", noteList)
        return
      }
    });
    if(!note)
      console.warn("cfiRange not found")
  }
  /**TODO: 此处代码有待处理：对笔记进行处理的流程应该重构(有时间的话) */
  function setNoteText(noteText, isNotePublic, isTakeNote) {
    console.log("set note text")
    let note = noteList.pop()
    if(isTakeNote){
      note.note = noteText
      note.isPublic = isNotePublic
      console.log(note)
      noteList.push(note)
    }
    else{
      noteList.push(note)
      removeMark(note.cfiRange)
    }
  }

  function getNoteText(cfiRange) {
    console.log("get note text:", cfiRange)
    let noteText
    noteList.forEach(note => {
      console.log(note.cfiRange)
      if(note.cfiRange == cfiRange){
        console.log(note, note.note)
        noteText = note.note
      }
    })
    return noteText
  }

  
  function checkCFIRangeLegal(cfiRange) {
    console.log("call check cfi range legel, cfiRange:", cfiRange)
    let {startCfi: _startCfi, endCfi: _endCfi} = cfiRange2cfi(cfiRange)
    let EF = new EpubCFI();
    for (let i = 0; i < noteList.length; i++) {
      let itemEf = noteList[i].cfiRange;
      let { startCfi , endCfi } = cfiRange2cfi(itemEf);
      // 四个点
      let s1_s2 = EF.compare(startCfi, _startCfi);
      let e1_s2 = EF.compare(endCfi, _startCfi);
      // 判断 后者的起始点是否在前者的区间内
      if (s1_s2 == -1 && e1_s2 == 1 || s1_s2 == 0 || e1_s2 == 0) {
        console.log("起始点在区间内");
        return false;
      }
      let s1_e2 = EF.compare(startCfi, _endCfi);
      let e1_e2 = EF.compare(endCfi, _endCfi);
      if (s1_e2 == -1 && e1_e2 == 1 || s1_e2 == 0 || e1_e2 == 0) {
        console.log("终点在区间内");
        return false;
      }
  
      if (s1_s2 == -1 && e1_e2 == 1) {
        console.log("不能在已经标记内容内选择");
        return false;
      }
  
      if (s1_s2 == 1 && e1_e2 == -1) {
        console.log("选择范围内包含了已经标记内容");
        return false;
      }
  
    }
    return true;
  }

  /**private function */
  function cfiRange2cfi(cfiRange) {
    console.log("call cfi range 2 cfi, cfiRange: ", cfiRange)
    let cfiParts = cfiRange.split(','); 
    // 起始点
    let startCfi = cfiParts[0] + cfiParts[1] + ')';  
    //  终点
    let endCfi = cfiParts[0] + cfiParts[2];
    return {startCfi, endCfi}
  }

  function doSearch(q) {
    return Promise.all(
      book.spine.spineItems.map((section) => 
        section
          .load(book.load.bind(book))
          .then(section.find.bind(section, q))
          .finally(section.unload.bind(section))
      )
    ).then((results) => Promise.resolve([].concat.apply([], results)))
  }

  function getNoteList() {
    return noteList
  }

  function setLatedPage() {
    console.log("set page to currentLocation")
    rendition.display(currentLocation.start.cfi)
  }

  function highlight(cfiRange) {
    rendition.annotations.highlight(cfiRange, {}, () => { }, null, {
      "fill": 'red'
    })
    setTimeout(() => {
      rendition.annotations.remove(cfiRange, 'highlight')
    }, 5000);
  }

  /**用于hack epubjs源码^^
   * 或是一些临时的测试函数
   */
  function test(location) {
    rendition.display(location)
  }

  return {
    createBook, render, getBook, getRendition, nextPage, prevPage, setFontSize, setViewStyle, test, setTheme, setPage, setLatedPage,
    takeNote, setFillColor, getIsLocationLoadFinished, removeMark, setNoteText, getNoteText, checkCFIRangeLegal, highlight, 
    doSearch, getNoteList
  }
}