<template>
  <div class="comments">
    <!-- 用户信息 -->
    <div class="info">
      <p>用户名：{{ myname }}</p>
      <p>ID-{{ myid }}</p>
    </div>
    <!-- 评论显示 -->
    <el-main>
      <div v-for="(comment, index) in comments" :key="index" class="comment">
        <!-- 循环显示的每条评论 -->
        <div>
          <el-row>
            <el-col :span="20">
              <el-link class="text-larger" style="float: left;" type="primary">{{ comment.author }}</el-link>
              <el-rate class="text-larger" style="float: left;" v-model="value" disabled text-color="#ff9900"></el-rate>
              <el-link class="text-larger" style="float: left;" type="primary">{{ comment.time }}</el-link>
            </el-col>
            <el-col :span="16">
              <div class="auto-wrap">
                <p class="text-medium">{{ comment.text }} </p>
              </div>
            </el-col>
            <el-col :span="16">
              <el-button class="text-larger" style="float: left;" type="text" 
              icon="el-icon-caret-top" @click="likeComment(index)">{{ comment.likes > 0 ? comment.likes:'' }}</el-button>
              <el-button class="text-larger" style="float: left;" type="text" 
              icon="el-icon-edit" @click="beginReply(index)">回复{{ comment.replies.length }}</el-button>
              <el-button class="text-larger" style="float: left;" type="text" 
              :icon="comment.showReply ? 'el-icon-arrow-up':'el-icon-arrow-down' " @click="showReply(index)"></el-button>
              <!-- element的type如果为text，则结果是文字按钮 -->
            </el-col>
            <!-- 回复区 -->
            <el-col v-if="comment.showReply">  
              <!-- 回复显示 -->
              <div style="margin-left: 100px" v-for="(reply, replyIndex) in comment.replies" 
              :key="replyIndex" class="auto-wrap">  
                <div>
                  <el-link class="text-larger">{{ reply.author }}</el-link>
                </div>
                <p class="text-medium">{{ reply.text }}</p>  
              </div>  
            </el-col>
          </el-row>
        </div>
      </div>
    </el-main>
    <!-- 评论、回复框 -->
    <div class="comment-box">
      <el-form >
        <el-form-item>
          <el-input type="textarea" v-model="content" maxlength="10000" show-word-limit/>
        </el-form-item>
        <el-form-item>
          <el-button v-if="replying" @click="endReply()">返回评论</el-button><!-- 退出回复，返回评论 -->
          <el-button @click="addComment">发送</el-button>
          <p v-if="replying">正在回复 {{ comments[replyIndex].author }}</p><!-- 显示正在回复给某人 -->
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import {currentTime} from "../js/Time.js";

export default {
  name: "CommentBlock",
  components: {
  },
  props: {
    myname: {
      type: String,
      default: '匿名'
    },// 传入用户名
    myid: {
      type: Number,
      default: 100
      // 传入用户id
    }
  },
  data() {
    return {
      form: {
          to: '',
          
        },
      value: 4,
      comments: [],// 已有评论
      content: '',// 输入内容
      replying: false,// 正在回复
      replyIndex: 0,// 回复的评论号
    };
  },
  methods: {
    addComment() {
      if (this.content) {
        if (this.replying) {
          const newReply = {
            text: this.content, 
            author: this.myname
          };
          this.comments[this.replyIndex].replies.push(newReply);
          this.endReply();
        }
        else {
          const newComment = { 
            text: this.content, 
            author: this.myname, 
            showReply: false,
            likes: 0, 
            replyText: '',
            replies: [],
            time: currentTime()
          };
          this.comments.push(newComment);
        }
        this.content = '';
      }
    },
    likeComment(index) {
      if (index < this.comments.length && index >= 0) {
        this.comments[index].likes++;
      }
    },
    showReply(index) {
      if (index < this.comments.length && index >= 0) {  
        this.comments[index].showReply = !(this.comments[index].showReply);
      }  
    },
    beginReply(index){
      this.replyIndex=index;
      this.replying=true;
    },
    endReply(){
      this.replyIndex=0;
      this.replying=false;
    }
  }
};  
</script>

<style scoped>
.text-larger {
  font-family: 
  "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size: larger;
}
.text-medium {
  font-family: 
  "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font-size: medium
}
.auto-wrap {
  width: 200px; /* 定义容器宽度 */
  border: none; /* 为了清楚地看到效果，加上边框 */
  word-wrap: break-word; /* 允许在长单词内部换行 */
  word-break: break-all; /* 允许在任意位置换行 */
  text-align: left;
}
</style>