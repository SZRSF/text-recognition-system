<template>
  <div>
      <div class="header">
        <i @click="changeMenu" class="iconfont icon-list"></i>
        <i @click="exit" class="iconfont icon-user"></i>
        顶部区域</div>
      <!-- 内容区域，路由出口 -->
      <div class="content">
          <router-view/>
      </div>
  </div>
</template>

<script>
export default {
  methods:{
    changeMenu(){
      // 点击切换按钮的时候 修改父组件的数据
      this.$emit('changeCollapse')
      
      
    },
    exit(){
      // 点击切换按钮的时候 修改父组件的数据
      this.$router.push('/login');
    }
  }
}
</script>

<style lang="less" scoped>
.header{
  height: 50px;
  line-height: 50px;
  color: #fff;
  background-color: #1e78bf;
  .iconfont{
    font-size: 24px;
  }
  .iconfont icon-user{
    font-size: 24px;
    right: auto;
  }
}
.content{
  // background-color: #8799a3;
  // top: 0;
  // bottom:0;
}

</style>