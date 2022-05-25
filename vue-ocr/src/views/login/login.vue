<template>
<div class="login_container">
    <div class="login_box">
    <div class="title">
      <h1>登录</h1>
    </div>
    <!-- 登陆表单区域 -->
    <el-form ref="loginFormRef" :model="loginFrom" :rules="LoginfromRules"   label-width="0px" class="login_form">
        <!-- 用戶名 -->
      <el-form-item prop="username">
         <el-input  v-model="loginFrom.username">
         </el-input>
      </el-form-item>
      <!-- 密碼 -->
        <el-form-item prop="password">
         <el-input v-model="loginFrom.password">
         </el-input>
      </el-form-item>
      <!-- 按鈕 -->
        <el-form-item  class="btns">
         <el-button type="primary" @click="doLogin()" >登录</el-button>
         <el-button type="info"><el-link @click="gotoRegister()">立即注册</el-link></el-button>
      </el-form-item>
    </el-form>
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            loginFrom:{
                username:'',
                password:'',
                userdata:[],
            },
             LoginfromRules:{
                   // 验证用户名是否合法
              username: [
                { required: true, message: '请输入登录名称', trigger: 'blur' },
                { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
              ],
              // 验证密码是否合法
              password: [
                { required: true, message: '请输入登录密码', trigger: 'blur' },
                { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
              ]

            }
        }
    },
    methods:{
        gotoRegister:function(){
          this.$router.push({
            name:'Register'
          });
        },
        doLogin:function(){
            axios.post('http://127.0.0.1:4523/mock/956336/api/login', {
              params: {//有参数时,若无参数时直接省略不写
                username:this.username,
                password:this.password,
              }
            }).then((res) => {
              console.log('数据：', res);
              if(res.status == '200'){
                this.userdata=res.data
                // console.info(this.userdata)
                this.$router.push({  
                    name:'Home',
                    params:{
                      userdata:this.userdata
                    }
                  });
                }else{
                  this.$router.push('/login')
                }
            })
            
        },
      
    }
}
</script>

<style lang="less" scoped>
.login_container{
    background: #2b4b6b;
    height:100%;

}
.login_box{
    width: 450px;
    height: 350px;
    background-color: rgba(255, 255, 255, 0.418);
    border-radius:5px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
         background: url('../../assets/images/04.png') no-repeat;
    background-size: cover; 
}
.login_form{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    margin-bottom: 50px;
    // 元素指定宽度和高度包括了 padding 和 border 
    box-sizing: border-box;

}
.btns{
    display: flex;
    justify-content: center;
}
.title{
  margin-top: 20px;
  margin-bottom: 30px;
  text-align: center;
}
</style>
