//搭建express服务
const express = require( 'express' )
const app = express()

//路由
const router = require('./router')

app.use('/api',router)

app.listen(8989,()=>{
console.log(8989);
})
