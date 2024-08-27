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
            <el-form-item>
              <!-- 文件上传区域 -->
              <el-upload
                class="upload-demo"
                action="https://jsonplaceholder.typicode.com/posts/"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                multiple
                :limit="3"
                :on-exceed="handleExceed"
                :file-list="fileList">
                <el-button type="primary" style="display: flex;">点击上传</el-button>
              </el-upload>
            </el-form-item>
            <el-form-item >
              <el-button type="primary" style="display: flex;" @click="submitNew">确认创建</el-button>
            </el-form-item>
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
                  v-for="item in category"
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

      </div>
    </div>
  </div>
</template>

<script>
import {category} from '@/js/Api.js';
import {createNovel} from '@/js/Api.js';
import '@/css/layout.css';

export default{
  name: 'Upload',
  data() {
    return {
      newWork: {
        workName: '',
        intro: '',
        chapter: '',
        category: '',
      },
      
      imgUpload: '/upload',
      imageUrl: '',
      url: '',
      author_name: '',

      category: [],
      fileList: [],
    }
  },
  async created() {
    this.category = await category();
  },
  computed: {
    formData() {
      const formData = new FormData();
      formData.append('novel_status', 0);
      formData.append('novel_name', this.newWork.workName);
      formData.append('detail', this.newWork.intro);
      formData.append('author', this.$store.getters.userInfo.id);
      if (this.fileList) {  
        formData.append('novel_img', this.fileList);  
      }  
      return formData;
    }
  },
  methods: {
    async submitNew(){
      // let url = this.url;
      // axios.post({url, params: this.newWork});
      createNovel(this.formData);

      console.log('submit my new work');
    },
    uploadFile() {
      // 添加文件
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