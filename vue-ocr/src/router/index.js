import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '../views/layout/index.vue'
import Login from '../views/login/login.vue'
import Register from '../views/Register/register.vue'
import Home from '../views/Home/index.vue'
// import store from '../store'

//异步
const Manage = ()=>import('../views/user/manage.vue')
const Start = ()=>import('../views/Start/index.vue')
const Immediate = ()=>import('../views/Start/immediate.vue')
const Upload = ()=>import('../views/Start/upload.vue')
const Others = ()=>import('../views/Others/index.vue')

Vue.use(VueRouter)

const routes = [
    {
        path: '',
        component: Layout,
        //路由元组件
        meta:{
            isLogin:true,
        },
        children:[
            {
                path: '/',
                name: 'Home',
                component: Home
            },
            {
                path: '/others',
                name: 'Others',
                component: Others
            },
            {
                path: '/manage',
                name: 'Manage',
                component: Manage
            },
            {
                path: '/start',
                name: 'Start',
                component: Start,
                children:[
                    {
                        path: '/immediate',
                        name: 'Immediate',
                        component: Immediate
                    },
                    {
                        path: '/upload',
                        name: 'Upload',
                        component: Upload
                    },
                ]
            },
            

        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    }

]

const router = new VueRouter({
    routes
})

//路由拦截
// router.beforeEach((to,from,next)=>{
//     console.log('---to---',to);
//     //判断是否要登录
//     if(to.matched.some(ele=>ele.meta.isLogin)){
//         //判断当前用户是否已经登录
//         // let token="";
//         if(store.state.Authorization){
//             next();
//         }else{
//             next('/login')
//         }
//     }else{//不需要登录
//         next();
//     }
//     next();
// })
export default router
