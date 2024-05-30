<template>
  <el-container style="background-color: aliceblue;">
    <el-header style="width: 100vw;">
      <h1 style="display: flex;">新作品上传</h1>
    </el-header>
    <!-- 新作品提交 -->
    <el-main>
      <el-form style="float: left;">
        <el-form-item style="width: 30vw;">
          <!-- 文件上传区域 -->
          <el-upload style="display: flex;" drag :action="url" multiple>
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
        <el-form-item label="上传封面" label-position="left" label-width="80px" style="width: 30vw;">
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
    <!-- 已有作品更新 -->
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
          <el-upload
          class="upload-demo"
          :action="url"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :before-remove="beforeRemove"
          multiple
          :limit="3"
          :on-exceed="handleExceed"
          :file-list="fileList">
            <el-button type="text">点击上传</el-button>
          </el-upload>
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
  </el-container>
</template>

<script>
export default{
  name: 'Upload',
  data() {
    return {
      works:[
        {
          "bookId": "1", 
          "title": "我看见的世界", 
          "tips": "这是一本描述人工智能领域的书籍，详细介绍了作者在这一领域的研究和见解。",
          "date": "23-12-21", 
          "progress": "12"
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
      user_id: 11,
      novel_id: 101,
      url: '/novels/addnovel?user_id='+this.user_id+'&novel_id='+this.novel_id,
      imgUpload: '/upload',
      imageUrl: '',
    }
  },
  methods: {
    previewNew(){
      console.log('preview my new Work');
    },
    submitNew(){
      console.log('submit my new work');
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
      this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeRemove(file) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    },
    handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    }
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