<template>
  <el-container style="background-color: aliceblue;">
    <el-header style="width: 100vw;">
      <h1 style="display: flex;">新作品上传</h1>
    </el-header>
    <el-main>
      <el-form style="float: left;">
        <el-form-item style="width: 30vw;">
          <el-upload style="display: flex;"
          class="upload-demo"
          drag
          action="#"
          multiple>
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">上传文件不超过500kb</div>
          </el-upload>
        </el-form-item>
      </el-form>
      <el-form style="float:left">
        <el-form-item label="作品名" label-position="left" label-width="80px" style="width: 30vw;">
          <el-input></el-input></el-form-item>
        <el-form-item label="备注" label-position="left" label-width="80px" style="width: 30vw;">
          <el-input></el-input></el-form-item>
        <el-form-item label="章节" label-position="left" label-width="80px" style="width: 30vw;">
          <el-input></el-input></el-form-item>
        
      </el-form>
      <el-form style="float:left">
        <el-form-item label="上传封面" label-position="left" label-width="80px" style="width: 30vw;">
          <!-- <el-upload class="avatar-uploader"
          action="https://jsonplaceholder.typicode.com/posts/"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"> -->
          <el-upload style="float:left;" class="avatar-uploader">
          <img v-if="imageUrl" :src="imageUrl" class="avatar">
          <i class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload></el-form-item>
      </el-form>
    </el-main>

    <el-header style="width: 100vw;">
      <h1 style="display: flex;">创作更新</h1>
    </el-header>
    <el-main>
      <el-table :data="works" style="width: 100%;">
        <el-table-column prop="title" label="作品名" width="180"></el-table-column>
        <el-table-column prop="tips" label="作品备注" width="360"></el-table-column>
        <el-table-column prop="date" label="上次更新时间" width="180"></el-table-column>
        <el-table-column prop="progress" label="进度"></el-table-column>
        <el-table-column fixed="right" width="120">
          <template slot-scope="scope">
            <el-button @click.native.prevent="upload(scope.$index, mails)"
              type="text" size="small">上传
            </el-button>
          </template>
        </el-table-column>
        <el-table-column fixed="right" width="120">
          <template slot-scope="scope">
            <el-button @click.native.prevent="check(scope.$index, mails)"
              type="text" size="small">查看
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
export default{
  name: 'Upload',
  data() {
    return {
      works:[{"title": "我看见的世界", "tips": "这是一本描述人工智能领域的书籍，详细介绍了作者在这一领域的研究和见解。",
       "date": "23-12-21", "progress": "12"},],
    }
  },
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
    font-size: 178px;
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