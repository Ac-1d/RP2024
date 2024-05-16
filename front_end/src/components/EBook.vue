<template>
  <div id="ebook" @mouseup="getSelectedTextPosition">
    <!-- TODO: 窗口大小溢出，原因未知 -->
    <div id="epub_render" @click="checkclick"></div>
    <div id="mask">
      <button id="tableButton" @click="callTable">点我呼出菜单</button>
      <button id="nextPageButton" @click="nextPage">点我向后翻页</button>
      <button id="prevPageButton" @click="prevPage">点我向前翻页</button>
    </div>
    <div id="table" v-if="showTable">
      <div id="bookInfo">这里是书籍信息</div>
      <div id="setting">
        <h1>这里是设置</h1>
        <!-- TODO: 最好改为按下回车/点击页面时修改数值 -->
        调整字体大小：
        <input type="text" v-model="fontSize">
        <div>{{ fontSize }}</div>
        <button id="changeViewStyleButton" @click="changeViewStyle">点我修改视图</button>
        <button @click="test">点我查看代码实现</button>
        <button @click="changeTheme(0)">点我切换浅色模式</button>
        <button @click="changeTheme(1)">点我切换深色模式</button>
        <button @click="getLocation">点我获取locations</button>
      </div>
      <div id="progressBar">这里是进度条</div>
    </div>
  </div>
</template>

<script>
import {useEpub} from "../js/Ebook.js";

export default {
  name: "EBook",
  data() {
    return {
      showTable: true,
      fontSize: ''
    }
  },
  props: [
    'showNav'
  ],
  mounted() {
    this.epubReader = useEpub();
    this.loadEpub();
  },
  watch: {
    fontSize(newValue) {
      console.log("call fontSize in watch");
      this.changeFontSize(newValue);
    }
  },
  methods: {
    loadEpub() {
      this.epubReader.createBook("books_tmp/09.epub");
      this.epubReader.render("epub_render", {
        width: window.innerWidth,
        height: window.innerHeight,
        flow: "scrolled-doc",
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
    getSelectedTextPosition() {
      var selection = window.getSelection(); // 获取用户选择的文本
      if (selection.rangeCount > 0) { // 如果存在选中文本
        var range = selection.getRangeAt(0); // 获取选中文本的范围
        var startContainer = range.startContainer; // 起始节点
        var startOffset = range.startOffset; // 起始偏移量
        var endContainer = range.endContainer; // 结束节点
        var endOffset = range.endOffset; // 结束偏移量

        console.log("Start Node:", startContainer);
        console.log("Start Offset:", startOffset);
        console.log("End Node:", endContainer);
        console.log("End Offset:", endOffset);
      } else {
        console.log("No text selected.");
      }
    },
    getLocation() {
      this.epubReader.getBook().locations.generate(0)
    //   let cfi = this.epubReader.getBook().locations[0];
    //   this.epubReader.getRendition().annotations.underline(cfi, {}, this.emptyFunction(), "", {
    // "background-color": "rgba(255, 255, 0, 0.5)",
    //       })
    },
    test() {
      this.epubReader.test();
    },
    emptyFunction() {
    },
    checkclick() {
      console.log("success click the block")
    }
  },
};
</script>

<style lang="scss" scoped>
#ebook {
  position: relative;
  // #epub_render {
  //   width: 100%;
  //   height: 100vh;
  //   justify-content: center;
  //   align-content: center;
  // }
  #mask {
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
      width: 200px;
      height: 100%;
      background-color: grey;
    }
    #setting {
      position: fixed;
      top: 0;
      right: 0;
      width: 200px;
      height: 100%;
      background-color: grey;
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
}
</style>