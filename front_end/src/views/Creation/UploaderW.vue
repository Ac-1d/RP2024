<template>
  <el-container style="background-color: aliceblue;">
    <el-header style="width: 100vw;">
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

    <el-main>
      <el-table :data="works" style="width: 100%;">
        <el-table-column prop="title" label="作品名" width="180"></el-table-column>
        <el-table-column prop="date" label="更新时间" width="180"></el-table-column>
        <el-table-column prop="progress" label="进度"></el-table-column>
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
export default{
  name: 'UploaderW',
  data() {
    return {
      works:[],
    }
  }
}
</script>