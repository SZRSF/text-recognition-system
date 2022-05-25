<template>
  <div class = "layout">
      <!-- 左侧导航栏 -->
        <Mymenu class="menu" :isCollapse='isCollapse'/>
        <!-- <Foldmenu class="menu"/> -->
      <!-- 右侧内容显示 -->
        <Content class="content" @changeCollapse='changeCollapse'/>
        <!-- <Content class="content"/> -->
  </div>
</template>

<script>
import Content from './Content.vue'
// import Foldmenu from './Foldmenu.vue'
import Mymenu from './Mymenu.vue'
export default {
  components:{
      Mymenu,
      // Foldmenu,
      Content,
  },
  data(){
    return{
      isCollapse:false
    }
  },
  methods:{
    changeCollapse(){
      this.isCollapse = !this.isCollapse;
    }
  }
}
</script>


<style lang="less" scoped>
.layout{
  .menu{
      width:200px;
      min-height:500px;
      background:#a1b6be;
      position: fixed;
      top:0;
      bottom:0;
  }
  .content{
    // background-color: #1cbbb4;
    margin-left: 200px;

  }
}
</style>