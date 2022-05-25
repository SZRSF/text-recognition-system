<template>
  <div>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
    <el-radio-button :label="false">展开</el-radio-button>
    <el-radio-button :label="true">收起</el-radio-button>
</el-radio-group>
<el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
    
  <el-menu-item index="/">
    <i class="el-icon-location"></i>
    <span slot="title">首页</span>
  </el-menu-item>

  <el-submenu index="/start">
    <template slot="title">
      <i class="el-icon-location"></i>
      <span slot="title">开始</span>
    </template>

    <el-menu-item-group>
      <span slot="title">识别</span>
      <el-menu-item index="/immediate">上传识别</el-menu-item>
      <el-menu-item index="/upload">及时识别</el-menu-item>
    </el-menu-item-group>
    </el-submenu>

  <el-menu-item index="2">
    <i class="el-icon-menu"></i>
    <span slot="title">其他功能</span>
  </el-menu-item>

  <el-menu-item index="3">
    <i class="el-icon-document"></i>
    <span slot="title">历史记录</span>
  </el-menu-item>
  <el-menu-item index="/manage">
    <i class="el-icon-setting"></i>
    <span slot="title">设置</span>
  </el-menu-item>
</el-menu>
  </div>
</template>

<script>
export default {
    data() {
      return {
        isCollapse: true
      };
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
</style>