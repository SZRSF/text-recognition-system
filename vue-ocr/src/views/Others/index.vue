<template>
  <div class="search">
      <!-- 搜索区域 -->
      <div class="header">
         <el-input v-model="input" placeholder="请输入内容"></el-input>
         <el-button type="primary">搜索</el-button>
         <el-button type="primary">添加</el-button>
      </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      input: ''
    }
  }
}
</script>

<style lang="less" scoped>
.search{
    margin: 20px;
}
.header{
    display: flex;
    button{
        margin-left: 20px;
    }
}
</style>
