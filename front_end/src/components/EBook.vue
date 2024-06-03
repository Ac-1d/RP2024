<template>
  <div id="ebook">
    <!-- TODO: 窗口大小改变时应该重新渲染(?) -->
    <div id="epub_render"></div>
    <div id="buttons">
      <div id="tableButton">
        <el-button type="info" icon="el-icon-d-arrow-left" @click="prevPage" circle></el-button>
        <el-button type="info" icon="el-icon-setting" @click="callTable" circle></el-button>
        <el-button type="info" icon="el-icon-d-arrow-right" @click="nextPage" circle></el-button>
      </div>
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
            <hr class="parting-line">
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
              <hr class="parting-line">
              <div @click="setHref(item.cfi)" v-html="item.excerpt"></div>
            </div>
          </div>
        </div>
      </div>
      <div id="setting" class="side-bar">
        <div id="header">
          <el-form ref="settings" :model="settings" label-width="100px">
            <el-form-item label="深色模式">
              <el-switch v-model="settings.nightTheme"></el-switch>
            </el-form-item>
            <el-form-item label="笔记模式">
              <el-switch v-model="settings.isTakingNote"></el-switch>
            </el-form-item>
            <el-form-item label="笔记方式" v-if="settings.isTakingNote">
              <el-radio-group v-model="settings.noteType" size="small">
                <el-radio border label="underline">记笔记</el-radio>
                <el-radio border label="highlight">高亮</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="删除笔记" v-if="!settings.isTakingNote">
              <el-switch v-model="settings.isRemovingNote"></el-switch>
            </el-form-item>
            <el-form-item label="显示个人笔记">
              <el-switch v-model="settings.showPersonalNote"></el-switch>
            </el-form-item>
            <el-form-item label="字体大小" :rules="[
              { type: 'number', message: '字体大小必须为数字值' }
            ]">
              <el-input v-model.number="settings.fontSize" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="changeFontSize">设置</el-button>
              <el-button @click="defaultFontSize">默认大小</el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="danger" @click="exit">退出阅读</el-button>
            </el-form-item>
          </el-form>
        </div>
        <el-divider></el-divider>
        <el-form>
          <el-form-item>
            <el-button @click="showPersonalNote = true; showOthersNote = false">我的笔记</el-button>
            <el-button @click="showPersonalNote = false; showOthersNote = true">他的笔记</el-button>
          </el-form-item>
        </el-form>
        <div id="body">
          <div v-if="showPersonalNote" class="contents">
            <div v-for="item in personalNoteList" :key="item.index" class="text bookInfo-text">
              <hr class="parting-line">
              <span v-if="item.note && item.isPublic">{{ item.note }}</span>
            </div>
          </div>
          <div v-if="showOthersNote" class="contents">

          </div>
        </div>
      </div>
    </div>
    <div id="take-note-component" v-if="showNoteInput">
      <div id="mask"></div>
      <div id="note-input">
        <div id="contents">
          <el-form label-position="top" label-width="100px">
            <el-form-item label="笔记记录">
              <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 6 }" placeholder="请输入内容" v-model="noteText" resize="none">
              </el-input>
            </el-form-item>
          </el-form>
          <el-form>
            <el-form-item label="是否公开" style="margin: 5% 10%">
              <el-switch v-model="isNotePublic"></el-switch>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="finishTakeNote(true)">确认</el-button>
              <el-button @click="finishTakeNote(false)">取消</el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { useEpub } from "../js/Ebook.js"; 
import axios from "axios";

export default {
  name: "EBook",
  data() {
    return {
      showTable: true,
      showNavigation: true,
      showNoteInput: false,
      showPersonalNote: true,
      showOthersNote: false,
      isNotePublic: false,
      noteText: '',
      coverUrl: '',
      metadata: null,
      navigation: [],
      searchText: '',
      searchResult: [],
      noteCfiRange: '',
      noteContents: '',
      allowTakeNote: false,
      settings: {
        nightTheme: false,
        isTakingNote: false,
        isRemovingNote: false,
        showPersonalNote: true,
        showOthersNote: false,
        noteType: '',
        fontSize: '',
      },
      personalNoteList: [],
      othersNoteList: [],
    }
  },
  computed: {
    ...mapState(['currentBookId'])
  },
  mounted() {
    this.$store.commit('setShowTopBar')
    console.log("the book id is ", this.currentBookId)
    axios.get('http://127.0.0.1:8000/novels/bookrack?user_id=1')
      .then(response =>{
        console.log("response: ", response)
      })
      .catch(error =>{
        console.error("error: ", error)
      })
    this.epubReader = useEpub();
    this.loadEpub();
    //this.loadMark()
    let rendition = this.epubReader.getRendition()
    rendition.on("selected", (cfiRange, contents) => {
      console.log("listener detectes text selected:", cfiRange, contents)
      this.noteCfiRange = cfiRange
      this.noteContents = contents
      if(this.allowTakeNote){
        this.takeNote()
        this.allowTakeNote = false
      }
    })
    rendition.on("mouseup", () => {
      console.log("listener detectes mouseup")
      if(this.settings.isTakingNote == false)
        return
      if(this.noteCfiRange){
        this.takeNote()
      }
      else{
        console.warn("cfiRange is undefined")
        this.allowTakeNote = true
      }
    })
    rendition.on("markClicked", (cfiRange) => {
      console.log("listener detectes 'markClicked'")
      console.log(cfiRange)
      if (this.settings.isRemovingNote)
        this.epubReader.removeMark(cfiRange)
      else {
        console.log(this.epubReader.getNoteText(cfiRange))
      }
    })
  },
  watch: {
    'settings.nightTheme': function(nightTheme) {
      console.log("call set night theme",nightTheme)
      if(nightTheme)//true为深色模式
        this.epubReader.setTheme(1)
      else
        this.epubReader.setTheme(0)
    },
  },
  methods: {
    loadEpub() {
      //文件路径需要请求获取
      const book = this.epubReader.createBook("books_tmp/moby-dick.epub");
      console.log(book)
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
      this.epubReader.render("epub_render", {
        width: window.innerWidth,
        height: window.innerHeight,
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
    changeFontSize() {
      console.log("call setFontSize");
      this.epubReader.setFontSize(this.settings.fontSize);
    },
    defaultFontSize() {
      this.settings.fontSize = null
      this.epubReader.setFontSize(16)
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
    takeNote() {
      if(this.epubReader.checkCFIRangeLegal(this.noteCfiRange)){
          if (this.settings.noteType == 'underline')
            this.showNoteInput = true
          this.epubReader.takeNote(this.settings.noteType, this.noteCfiRange)
          console.log(this.noteList)
        }
        this.noteContents.window.getSelection().removeAllRanges()
        this.noteCfiRange = null
    },
    finishTakeNote(isTakeNote) {
      this.epubReader.setNoteText(this.noteText, this.isNotePublic, isTakeNote)
      this.isNotePublic = false
      this.noteText = null
      this.showNoteInput = false
    },
    loadMark() {
      //请求获取他人笔记与私人笔记
    },
    exit() {
      const url = '/book/' + this.currentBookId
      if(this.currentBookId)
        this.$router.push(url)
      else
        this.$router.push('/home')
    },
    test() {

    },
    emptyFunction() {
    },
    setHref(href) {
      console.log("set page to", href)
      this.epubReader.getRendition().display(href)
    },
  },
  beforeDestroy() {
    // TODO: 销毁监听器
    this.$store.commit('setShowTopBar')
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


      #bookInfo-header {
        width: auto;
        height: 20%;
        display: flex;

        #bookInfo-cover {
          height: 100%;
          object-fit: contain;
        }

        #bookInfo-text {//对低高度适配性极差^^'
          margin-top: 5%;
          height: 95%;
          width: 60%;
          display: flex;
          flex-direction: column;
          // overflow: scroll;
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

      #header {
        width: 90%;
        margin: 5% 5%;
        max-height: 50%;
        overflow: scroll;
      }
      #body {
        width: 90%;
        margin: 5% 5%;
        height: 50%;
        overflow: scroll;
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
      #contents {
        margin: 5%;
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
  width: 350px;
  height: 100%;
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
  min-height: 60px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>