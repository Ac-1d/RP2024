<template>
  <el-container>
    <el-upload
      class="upload-demo"
      drag
      action="#"
      multiple>
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">上传文件不超过500kb</div>
    </el-upload>
  </el-container>
</template>

<script>
export default{
  name: 'Uploader',
}
</script>