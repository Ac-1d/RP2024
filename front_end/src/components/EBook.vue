<template>
  <div id="ebook">
    <!-- TODO: 窗口大小改变时应该重新渲染(?) -->
    <div id="epub_render"></div>
    <!-- TODO: 陆续被替换的设计 -->
    <div id="buttons">
      <button id="tableButton" @click="callTable">点我呼出菜单</button>
      <button id="nextPageButton" @click="nextPage">点我向后翻页</button>
      <button id="prevPageButton" @click="prevPage">点我向前翻页</button>
    </div>
    <div id="table" v-if="showTable">
      <div id="bookInfo" class="side-bar">
        <div id="bookInfo-header">
          <img :src="coverUrl" id="bookInfo-cover">
          <div id="bookInfo-text">
            <!-- 文本无法垂直方向居中 -->
            <p id="title" class="text bookInfo-text">{{ metadata.title }}</p>
            <p id="author" class="text bookInfo-text">作者：{{ metadata.creator }}</p>
            <p class="text bookInfo-text">已读：12h</p>
            <p class="text bookInfo-search">全文搜索：</p>
            <div id="block">
              <el-input class="search-input" @change="doSearch" v-model="searchText" placeholder="请输入内容"
                size="mini"></el-input>
              <el-button id="search-hide" icon="el-icon-close" circle
                @click="showNavigation = true; searchText = null"></el-button>
            </div>
          </div>
        </div>
        <div class="bookInfo-body" v-if="showNavigation">
          <div v-for="item in navigation" :key="item.index" class="text bookInfo-text">
            <hr v-if="item.index != 1" class="parting-line">
            <span @click="setHref(item.href)">
              {{ item.index }}.{{ item.label }}
            </span>
          </div>
        </div>
        <div class="bookInfo-body" v-if="!showNavigation"><!-- 与上面同级div块不同时渲染 -->
          <div v-if="!searchResult || searchResult.length === 0">
            <p class="bookInfo-text">搜索内容不存在</p>
          </div>
          <div v-else>
            <div v-for="item in searchResult" :key="item.index" class="text">
              <hr v-if="item.index != 1" class="parting-line">
              <div @click="setHref(item.cfi)" v-html="item.excerpt"></div>
            </div>
          </div>
          <!-- <div v-for="item in searchResult" :key="item.index" class="text">
              <hr v-if="item.index != 1" class="parting-line">
              <div @click="setHref(item.cfi)" v-html="item.excerpt"></div>
          </div> -->
        </div>
      </div>
      <div id="setting" class="side-bar">
        <div id="header">
          <el-row>
            <el-col :span="12">
              <div class="grid-content bg-purple"></div>
            </el-col>
            <el-col :span="12">
              <div class="grid-content bg-purple-light"></div>
            </el-col>
          </el-row>
        </div>
        <h1>这里是设置</h1>
        <!-- TODO: 最好改为按下回车/点击页面时修改数值 -->
        调整字体大小：
        <input type="text" v-model="fontSize">
        <button id="changeViewStyleButton" @click="changeViewStyle">点我修改视图</button>
        <button @click="changeTheme(0)">点我切换浅色模式</button>
        <button @click="changeTheme(1)">点我切换深色模式</button>
        <button @click="changeLocation">点我修改至储存location位置</button>
        <input type="text" v-model="testPageNumber">
        <button @click="changeTakeNoteType('highlight')">点我标记高亮</button>
        <button @click="changeTakeNoteType('underline')">点我做笔记</button>
        <button @click="testIsRemove = !testIsRemove">点我切换查看/删除</button>
        <button @click="showNavigation = !showNavigation">点我切换目录/搜索结果</button>
        <el-input change="doSearch" v-model="searchText"></el-input>
      </div>
      <div id="progressBar">
        这里是进度条
        <!-- TODO：需要添加更多修饰，如：在locations尚未加载完毕时隐藏进度条 -->
        <!-- 有点想去掉进度条了😑 -->
        <input type="range" v-model="pageNumber">
      </div>
    </div>
    <div id="take-note-component" v-if="showNoteInput">
      <div id="mask"></div>
      <div id="note-input">
        <p>笔记记录：</p>
        <textarea id="input" v-model="noteText"></textarea><br>
        <button @click="finishTakeNote">确认</button>
      </div>
    </div>
  </div>
</template>

<script>
import { useEpub } from "../js/Ebook.js";

export default {
  name: "EBook",
  data() {
    return {
      showTable: true,
      showNavigation: true,
      showNoteInput: false,
      fontSize: '',
      pageNumber: '',
      testPageNumber: '',
      testIsRemove: false,
      takeNoteType: 'underline',
      noteText: '',
      coverUrl: '',
      metadata: null,
      navigation: [],
      searchText: '',
      searchResult: [1],
    }
  },
  props: [
    'showNav'
  ],
  mounted() {
    this.epubReader = useEpub();
    this.loadEpub();
    let rendition = this.epubReader.getRendition()
    rendition.on("selected", (cfiRange, contents) => {
      console.log("listener detectes text selected:", cfiRange, contents)
      this.epubReader.setForNote(cfiRange, contents)
    })
    rendition.on("mouseup", () => {
      console.log("listener detectes mouseup")
      if (this.epubReader.checkIsTakingNote()) {
        if (this.takeNoteType == 'underline')
          this.showNoteInput = true
      }
      this.epubReader.takeNote(this.takeNoteType)
    })
    rendition.on("markClicked", (cfiRange) => {
      console.log("listener detectes 'markClicked'")
      console.log(cfiRange)
      if (this.testIsRemove)
        this.epubReader.removeMark(cfiRange)
      else {
        console.log(this.epubReader.getNoteText(cfiRange))
      }
    })
  },
  watch: {
    fontSize(newValue) {
      console.log("call fontSize in watch");
      this.changeFontSize(newValue);
    },
    pageNumber(newValue) {
      // console.log("pageNumber changed", newValue)
      this.changePage(newValue)
    },
    testPageNumber(newValue) {
      this.epubReader.test(newValue)
    }
  },
  methods: {
    loadEpub() {
      const book = this.epubReader.createBook("books_tmp/moby-dick.epub");
      book.loaded.cover.then((cover) => {
        if (cover) {
          book.archive.createUrl(cover).then((_url) => {
            this.coverUrl = _url
            console.log("parse url:", this.coverUrl)
          })
        }
        else {//TODO: 无封面加载一个默认封面

        }
      })
      book.loaded.metadata.then((_metadata) => {
        this.metadata = _metadata
        console.log("parse metadata:", this.metadata)
      })
      book.loaded.navigation.then((nav) => {
        let index = 0
        nav.toc.forEach((toc) => {
          this.navigation.push({ 'id': toc.id, 'href': toc.href, 'label': toc.label, 'index': ++index })
        })
        console.log("parse navigation")
      })
      /**缩小渲染尺寸，否则会出现页面大小溢出的问题 0.99依然会溢出^^'*/
      const x = 0.98
      this.epubReader.render("epub_render", {
        width: (window.innerWidth * x),
        height: (window.innerHeight * x),
        // flow: "scrolled-doc",
        allowScriptedContent: true
      });
    },
    prevPage() {
      this.epubReader.prevPage();
    },
    nextPage() {
      this.epubReader.nextPage();
    },
    callTable() {
      this.showTable = !this.showTable;
    },
    changeFontSize(fontSize) {
      console.log("call setFontSize");
      this.epubReader.setFontSize(fontSize);
    },
    changeViewStyle() {
      this.epubReader.setViewStyle();
    },
    changeTheme(index) {
      this.epubReader.setTheme(index);
    },
    changePage(pageNumber) {
      this.epubReader.setPage(pageNumber)
    },
    changeLocation() {
      this.epubReader.setLatedPage()
    },
    changeTakeNoteType(takeNoteType) {
      this.takeNoteType = takeNoteType
    },
    doSearch() {
      console.log("call do search")
      this.epubReader.getBook().ready.then(() => {
        if (!this.searchText) {
          console.log("empty input")
          return
        }
        this.epubReader.doSearch(this.searchText).then((results) => {
          this.searchResult = results
          this.searchResult.map((item) => {
            console.log(item.excerpt, "|||", this.searchText)
            let regexPattern = new RegExp(this.searchText, "gi")
            let tmp = item.excerpt.match(regexPattern)[0]
            let targetString = `<span style="color: red;">` + tmp + `</span>`
            item.excerpt = item.excerpt.replace(
              regexPattern,
              targetString
            )
            return item
          })
        })
        this.showNavigation = false
      })
    },
    finishTakeNote() {
      this.epubReader.setNoteText(this.noteText)
      this.noteText = null
      this.showNoteInput = false
    },
    test() {
      this.epubReader.test();
    },
    emptyFunction() {
    },
    setHref(href) {
      console.log("set page to", href)
      this.epubReader.getRendition().display(href)
    }
  },
  beforeDestroy() {
    // TODO: 销毁监听器
  }
};
</script>

<style lang="scss" scoped>
#ebook {
  position: relative;

  #buttons {
    #tableButton {
      position: fixed;
      left: 50%;
      transform: translateX(-50%);
      top: 0;
    }

    #nextPageButton {
      position: fixed;
      right: 0;
      bottom: 0;
    }

    #prevPageButton {
      position: fixed;
      left: 0;
      bottom: 0;
    }
  }

  #table {
    #bookInfo {
      position: fixed;
      top: 0;
      left: 0;
      width: 400px;
      height: 100%;

      #bookInfo-header {
        width: auto;
        height: 20%;
        display: flex;

        #bookInfo-cover {
          height: 100%;
          object-fit: contain;
        }

        #bookInfo-text {
          margin-top: 5%;
          height: 95%;
          width: 60%;
          display: flex;
          flex-direction: column;

          #block {
            width: 100%;

          }
        }
      }
    }

    #setting {
      position: fixed;
      top: 0;
      right: 0;
      width: 400px;
      height: 100%;

      #header {
        width: 100%;
        height: 30%;

        #view {
          background-color: #fff;
        }

        #theme {
          background-color: #000;
        }

        #highlight-color {
          background-color: #fff;
        }

        #takeNote {
          background-color: #000;
        }

        #remove {
          background-color: #fff;
        }
      }
    }

    #progressBar {
      position: fixed;
      align-content: center;
      left: 50%;
      transform: translateX(-50%);
      bottom: 0;
      width: 300px;
      height: 100px;
    }
  }

  #take-note-component {
    #note-input {
      position: fixed;
      left: 50%;
      transform: translateX(-50%);
      bottom: 10%;
      height: 300px;
      width: 500px;
      background: white;
      border: 1px dashed black;
      z-index: 9999;

      #input {
        height: 150px;
        width: 250px;
        resize: none;
      }
    }

    #mask {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.25);
      /* 半透明黑色背景 */
      z-index: 9998;
    }
  }
}

.search-input {
  width: 75%;
  margin-right: 5%;
}

.text {
  text-align: left;
}

.bookInfo-text {
  margin: 0%;
  width: 100%;
  flex-basis: 20%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.bookInfo-body {
  margin: 5% 20px;
  height: 75%;
  overflow: scroll;
}

.parting-line {
  height: 1px;
  border: none;
  border-top: 1px dashed grey;
}

.side-bar {
  background-color: white;
  border: 1px solid black;
  border-radius: 4px;
}

.settings {
  height: 20%;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>