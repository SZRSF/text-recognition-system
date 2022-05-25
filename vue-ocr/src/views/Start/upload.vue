<template>
  <div class="upload">
      <!-- 上传区域 -->
      <div><uploadImg/></div>
      <div>
        <span class="btn"><el-button type="primary" round @click="getText()">开始识别</el-button></span>
      </div>
      <div class="text">
        <h1>识别文字</h1>
        <!-- <p>{{message}}</p> -->
        <el-card class="box-card">
          <div v-for="o in message" :key="o" class="text item">
                {{ o }}
           </div>
        </el-card>
      </div>
    <!-- <div>
      <div>
        <input type="file" ref="upFile"  @change="File()"/>
        <img :src="Bsieks" alt="" style="wigth:500px;height:500px">
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import uploadImg from "./uploadImg.vue"
  export default {
    components:{
        uploadImg
    },
  data:function(){
      return{
         message:[],
    }
  },
  methods:{
    getText:function(){
            axios.get('http://127.0.0.1:4523/mock/956336/api/putTxt').then((res) => {
              // console.log('数据：', res);
              this.message = res.data
              console.info(this.message)
            }) 
        },
    File() {
      let file = this.$refs.upFile.files[0];
      var reader = new FileReader();
      reader.readAsDataURL(file); //调用自带方法进行转换
      reader.onload = (e) => {
        console.log(e.target.result);
      };
    },
  },
}

</script>

<style>
.upload{
    margin: 120px;
    /* display: flex; */
}
.btn{
  margin: 130px;

}
.text{
  margin-top: 30px;
}
</style>