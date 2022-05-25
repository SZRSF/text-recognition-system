<template>
  <div>
    <div class="search">
      <!-- 搜索区域 -->
      <div class="header">
         <el-input v-model="input" placeholder="请输入内容"></el-input>
         <el-button type="primary">搜索</el-button>
         <el-button type="primary">添加</el-button>
      </div>
    </div>
      <!--表格区域显示视图数据  -->
      <div class="wrapper">
        <el-table 
          :data="tableData" 
          border
          style="width: 100%" >
          <el-table-column type="selection" width="55"></el-table-column>
          <el-table-column prop="name" label="拥有者" width="180"> </el-table-column>
          <el-table-column prop="date" label="日期" width="180"></el-table-column>
          <el-table-column prop="address" label="设备ID"></el-table-column>
          <el-table-column prop="methods" label="识别方法"></el-table-column>
          <el-table-column prop="action" label="操作" width="180">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
          </el-table-column>
        </el-table>
      </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      input: '',
      tableData:[
        {
          date: '2016-05-02',
          name: '王小虎',
          address: 'HONOR V20',
          methods: '上传识别',
        }

      ]
    };
  },
  methods:{
    //编辑操作
    handleEdit(){
    },
    //删除操作
    handleDelete(){

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
.wrapper{
  margin: 20px 0; 
}
</style>
