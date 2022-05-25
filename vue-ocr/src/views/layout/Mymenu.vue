<template>
  <div>
    <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router
      :collapse='isCollapse'
      >
      <el-menu-item index="/">
        <i class="el-icon-menu"></i>
        <span slot="title">首页</span>
      </el-menu-item>

      <el-menu-item index="/others">
        <i class="el-icon-setting"></i>
        <span slot="title">其他功能</span>
      </el-menu-item>

      <el-menu-item index="/manage" >
        <i class="el-icon-document"></i>
        <span slot="title">个人中心</span>
      </el-menu-item>


      <!-- 分组下拉 -->
        <el-submenu index="/start">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>开始</span>
        </template>
        <el-menu-item-group>
          <template slot="title">识别</template>
          <el-menu-item index="/upload">上传识别</el-menu-item>
          <el-menu-item index="/immediate">即时识别</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

    </el-menu>

  </div>
</template>

<script>
export default {
  props:['isCollapse'],
  data(){
    return{
      // isCollapse:false
    }
  }
};
</script>

<style>

</style>