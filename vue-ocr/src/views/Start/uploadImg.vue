<template>
  <div>
<!-- 
    ref="upload" 获取dom元素 --upload
    action=''必选参数，上传的地址string
    :on-preview="handlePreview"点击文件列表中已上传的文件时的钩子 function(file)
    on-remove 文件列表移除文件时的钩子 function(file, fileList)
    on-success文件上传成功时的钩子 function(response，file，fileList)
    on-error 文件上传失败时的钩子function(err, file, fileList)
    on-progress文件上传时的钩子 function(event,file，fileList)
    auto-upload是否在选取文件后立即进行上传
    file-list上传的文件列表，例如:[{name: 'food.jpg', url: 'https:/ / xxx.cdn.com/xxx.jpg'}]array
 -->
      
  <!-- <el-upload
    class="upload-demo"
    ref="upload"
    @change="File()"
    action="http://127.0.0.1:4523/mock/956336/api/general_ocr"
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :on-success="successUpload"
    :file-list="fileList"
    :auto-upload="false">
    <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
    <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
  </el-upload> -->

  <el-upload
  list-type="picture"
   action=''
   accept=".jpg, .png"
   :limit="1"
   :auto-upload="false"
   :file-list="fileList"
   :on-change="getFile"
   :on-preview="handlePictureCardPreview"
   :on-remove="handleUploadRemove"
   >
	<el-button size="small" type="primary" @click="uploadimg">选择图片上传</el-button>
	<div slot="tip" class="el-upload__tip">只能上传一张jpg/png文件</div>
</el-upload>
 <!-- <el-button type="primary" round @click="sendpic">上传到服务器</el-button> -->
    {{srcBase}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
    methods:{
      //通过getFile方法获取文件信息
      getFile(file, fileList) {
        console.log("文件：",file,fileList)
        this.getBase64(file.raw).then(res => {
          const params = res
          this.proofImage = params
          // this.sendpic()
          console.log('编码：', res);
          axios.post('http://127.0.0.1:4523/mock/956336/api/general_ocr',{
            params: {//有参数时,若无参数时直接省略不写
                srcBase:this.params,
              }
          }).then((res) => {
            console.log('状态：', res);
          }) 
          
        })
      },

      //图片转base64编码：
      getBase64(file) {
        return new Promise(function (resolve, reject) {
          const reader = new FileReader()
          let imgResult = ''
          reader.readAsDataURL(file)
          reader.onload = function () {
            imgResult = reader.result
          }
          reader.onerror = function (error) {
            reject(error)
          }
          reader.onloadend = function () {
            // console.log("编码：",imgResult)
            this.srcBase=imgResult
            // console.log("编码：",this.srcBase)
            resolve(imgResult)
          }
        })
      },

      //预览和删除
        handleUploadRemove(file, fileList) {
          console.log(file,fileList)
          this.proofImage = ''
          this.ruleForm.message_img = ''
        },
        handlePictureCardPreview(file) {
          console.log(file)
          console.log(this.proofImage)
        },

      sendpic:function(){
        console.log('编码：', this.srcBase);
          axios.post('http://127.0.0.1:4523/mock/956336/api/general_ocr',{
            params: {//有参数时,若无参数时直接省略不写
                srcBase:this.srcBase,
              }
          }).then((res) => {
            console.log('状态：', res.status);
          }) 
      },

      // successUpload(response,file,fileList){
      //   this.sendpic();
      //   console.log("上传成功" + response,file,fileList)
      // },
      // submitUpload() {
      //   this.$refs.upload.submit();
      // },
      // handleRemove(file, fileList) {
      //   console.log(file, fileList);
      // },
      // handlePreview(file) {
      //   console.log(file);
      // },
      // File() {
      //   let file = this.$refs.upload.files[0];
      //   var reader = new FileReader();
      //   reader.readAsDataURL(file); //调用自带方法进行转换
      //   reader.onload = (e) => {
      //     console.log(e.target.result);
      //     this.srcBase=e.target.result
      //     console.log(this.srcBase);
      //   };
      // },

    },
    data() {
      return {
        fileList: [],
        srcBase:'',
      };
    },
}
</script>

<style>

</style>