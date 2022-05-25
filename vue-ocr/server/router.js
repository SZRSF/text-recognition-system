const express = require('express')
const router = express.Router()
//导入数据库sqlFun( 'sql',[],res=>{})
const sqlFun = require( './mysql')


//路由接口
router.get('/',(req,res)=>{
res.send('hello')
})

router.get('/projectList',(req,res) =>{
    const page = req.query.page ||1;
    const sqlLen = "select* from project where id";
    sqlFun(sqlLen, null, data=>{
        let len = data.length;
        const sql = "select * from project order by id desc limit 8 offset " +(page- 1)*8;
        sqlFun(sql, null, result=>{
                if(result.length > 0){
                res.send({
                status: 200,
                data: result,
                pageSize: 8,
                total: len
                })
            }else {
            res.send({
            status: 500,msg: "暂无数据"})
            }
        })
    })
})

router.get("/search", (req, res)=> {
    var search = req.query.search;
    const sql = "select * from project where concat(`title` ,`sellPoint`, `descs`)-like'%' " + any ;
    sqlFun(sql, null,(result)=>{
        if (result.length > 0) {
        res.send({
            status :200,
            result
        })
        }else {
            res.send({
            status: 500,
            msg:"暂无数据"
        })
      }
    })
})

    



module.exports = router
