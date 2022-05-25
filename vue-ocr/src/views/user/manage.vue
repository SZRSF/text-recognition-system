<template>
  <div class="info">
    <div>
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-select v-model="form.sex" placeholder="未知">
            <el-option label="秘密" value="unkown"></el-option>
            <el-option label="男孩子" value="man"></el-option>
            <el-option label="女孩子" value="woman"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="电话号码">
          <el-input v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item label="出生日期">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 150%;"></el-date-picker>
          </el-col>
        </el-form-item>

        <!-- <el-form-item label="活动性质">
          <el-checkbox-group v-model="form.type">
            <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
            <el-checkbox label="地推活动" name="type"></el-checkbox>
            <el-checkbox label="线下主题活动" name="type"></el-checkbox>
            <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
          </el-checkbox-group>
        </el-form-item> -->

        <!-- <el-form-item label="特殊资源">
          <el-radio-group v-model="form.resource">
            <el-radio label="线上品牌商赞助"></el-radio>
            <el-radio label="线下场地免费"></el-radio>
          </el-radio-group>
        </el-form-item> -->

        <el-form-item label="个人简介" >
          <el-input type="textarea" v-model="form.desc"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">保存</el-button>
          <el-button @click="clear">取消</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
 export default {
    data() {
      return {
        form: {
          name: '',
          sex: '',
          email:'',
          date: '',
        },
        userdata:[],
      }
    },
      watch:{
        "$route":{
          handler(route){
            const that = this
            if(route.name==='Manage'){
              that.findAll();
            }
          },
          deep:true
        }
      },      
      created:function() {
        console.log("查询数据");
        this.findAll();
      },
    methods: {
      clear(){
        this.form.name='';
        this.form.email='';
        this.form.date='';
      },
      onSubmit() {
        console.log('submit!');
      },

      findAll(){
        axios.get('http://127.0.0.1:4523/mock/956336/api/show', {    
        }).then(res=>{
        this.userdata=res.data;
        this.form.name=res.data.username;
        this.form.email=res.data.phone;
        this.form.date=res.data.logintime;
        console.log("用户信息："+res.status);
      })
    },

    }
 }
</script>

<style>
.info{
  margin: 80px;
  display: flex;
}
</style>