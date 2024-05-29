<template>
  <el-container>
    <el-header>
      作品上传
    </el-header>
    <el-main>
      <el-upload
      class="upload-demo"
      drag
      action="#"
      multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">上传文件不超过500kb</div>
      </el-upload>
    </el-main>
    <el-aside style="float: right;">
      <el-table>
        
      </el-table>
    </el-aside>
  </el-container>
</template>

<script>
export default{
  name: 'UploaderW',
}
</script>