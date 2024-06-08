<template>
  <div class="home">
    <div class="content">
      <div class="main-content">
        <div class="category-bar">
          <span class="title">作品上传</span>
        </div><div class="separator"></div>

        <!-- 作品上传区域-->
        <el-main style="background-color: ghostwhite;">
          <el-form style="float: left;">
            <el-form-item style="width: 30vw;">
              <!-- 文件上传区域 -->
              <el-upload style="display: flex" drag :action="url" multiple>
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
              </el-upload>
            </el-form-item>

            <el-form-item style="width: 30vw;">
              <el-button type="primary" style="display: flex;" @click="previewNew">预览作品</el-button>
            </el-form-item>
            <!-- 预览按钮 -->
            <el-form-item style="width: 30vw;">
              <el-button type="primary" style="display: flex;" @click="submitNew">确认创建</el-button>
            </el-form-item>
            <!-- 提交按钮 -->
          </el-form>
          <el-form style="float: left;">
            <el-form-item label="作品名" label-position="left" label-width="80px" style="width: 30vw;">
              <el-input v-model="newWork.workName"></el-input></el-form-item>
            <el-form-item label="备注" label-position="left" label-width="80px" style="width: 30vw;">
              <el-input v-model="newWork.intro"></el-input></el-form-item>
            <el-form-item label="章节" label-position="left" label-width="80px" style="width: 30vw;">
              <el-input v-model="newWork.chapter"></el-input></el-form-item>
            <el-form-item label="分类" label-position="left" label-width="80px" style="width: 30vw;">
              <el-select v-model="newWork.category" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
          <el-form style="float: left;">
            <el-form-item label="上传封面" label-position="left" label-width="80px" style="width: 20vw;">
              <!-- 封面上传按钮 -->
              <el-upload style="float:left;" class="avatar-uploader"
              :action="imgUpload"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </el-form-item>
          </el-form>
        </el-main>

        <!-- 作品更新区域 -->
        <div class="separator"></div>
        <div class="category-bar">
          <span class="title">创作更新</span>
        </div><div class="separator"></div>
        <el-main style="background-color: ghostwhite;">
          <el-table :data="works" style="width: 100%;">
            <el-table-column prop="novel_name" label="作品名" width="180"></el-table-column>
            <el-table-column prop="novel_detail" label="作品备注" width="360"></el-table-column>
            <!-- <el-table-column prop="date" label="上次更新时间" width="180"></el-table-column> -->
            <!-- <el-table-column prop="progress" label="进度"></el-table-column> -->
            <el-table-column label="状态" width="120">
              <template slot-scope="scope">
                <span>{{ scope.row.novel_status==0?'连载中':'已完结' }}</span>
              </template>
            </el-table-column>
            <el-table-column fixed="right" width="120">
              <template slot-scope="scope">
                <el-upload
                  class="upload-demo"
                  :action="url"
                  :on-preview="handlePreview"
                  :on-remove="handleRemove"
                  :before-remove="beforeRemove"
                  multiple
                  :limit="1"
                  :on-exceed="handleExceed"
                  :file-list="fileList">
                  <el-button type="text" @click.native.prevent="uploadFile(scope.$index)">点击上传</el-button>
                </el-upload>
              </template>
            </el-table-column>
            <el-table-column fixed="right" width="120">
              <template slot-scope="scope">
                <el-button @click.native.prevent="preview(scope.$index)" type="text">预览
                </el-button>
              </template>
            </el-table-column>
            <el-table-column fixed="right" width="120">
              <template slot-scope="scope">
                <el-button @click.native.prevent="submit(scope.$index)" type="text">确认提交
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {novels} from '@/js/Api.js';
import {category} from '@/js/Api.js';
import '@/css/layout.css';

export default{
  name: 'Upload',
  data() {
    return {
      works:[
        {
          "id": "1", 
          "novel_name": "我看见的世界", 
          "novel_detail": "这是一本描述人工智能领域的书籍，详细介绍了作者在这一领域的研究和见解。",
          "novel_status" : 0,
        },
      ],
      options: [
        {value: '全部', label: '全部'},
        {value: '文学', label: '文学'}, 
        {value: '小说', label: '小说'},
        {value: '历史文化', label: '历史文化'},
        {value: '社会纪实', label: '社会纪实'},
        {value: '科学新知', label: '科学新知'}, 
        {value: '艺术设计', label: '艺术设计'}, 
        {value: '商业经管', label: '商业经管'}, 
        {value: '绘本漫画', label: '绘本漫画'},
      ],
      newWork: {
        workName: '',
        intro: '',
        chapter: '',
        category: '',
      },
      fileList: [
      ],
      imgUpload: '/upload',
      imageUrl: '',
      url: '',
      author_name: '',
    }
  },
  async created() {
    this.works = await novels(this.author_name).results; 
    this.options = await category();
  },
  methods: {
    async previewNew(){
      let url = this.url;
      axios.get({url, params: this.newWork});
      
      console.log('preview my new Work');
    },
    async submitNew(){
      let url = this.url;
      axios.post({url, params: this.newWork});

      console.log('submit my new work');
    },
    uploadFile() {
      // 添加文件
    },
    preview(index){
      console.log('preview updates of my work, workid=' + index);
    },
    submit(index){
      console.log('updating my work, workid=' + index);
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeRemove(file) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isPNG = file.type === 'image/png';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG && !isPNG) {
        this.$message.error('上传图片只能是 JPG/PNG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    },
  }
}
</script>

<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    background-color: white;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    text-align: center;
    font-size: 0px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>