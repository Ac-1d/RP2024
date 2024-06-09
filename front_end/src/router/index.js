import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import BookDetail from "../views/BookDetail.vue";
import Bookshelf from "../views/Bookshelf.vue";
import Ebooks from "../views/Ebooks.vue";
import Rankings from "../views/Rankings.vue";
import Reports from "../views/Reports.vue";
import Search from "../views/Search.vue";
import About from "../views/About.vue";
import Reader from "../views/Reader.vue";
import Comments from "../views/Comments.vue";
import Mail from "../views/Mail/Mail.vue";
import Creation from "../views/Creation/Creation.vue";
import CategoriesDetail from '@/views/CategoriesDetail.vue';

import store from '@/store';
import { MessageBox } from 'element-ui';
Vue.use(MessageBox);

Vue.use(VueRouter);


const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: '/categories-detail',
    name: 'CategoriesDetail',
    component: CategoriesDetail
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/reader",
    name: "Reader",
    component: Reader
  },
  {
    path: "/bookshelf",
    name: "Bookshelf",
    component: Bookshelf
  },
  {
    path: "/ebooks",
    name: "Ebooks",
    component: Ebooks
  },
  {
    path: "/rankings",
    name: "Rankings",
    component: Rankings
  },
  {
    path: "/reports",
    name: "Reports",
    component: Reports
  },
  {
    path: "/search",
    name: "Search",
    component: Search
  },
  {
    path: "/book/:bookId",
    name: "BookDetail",
    component: BookDetail,
    props: true
  },

  {// mail站内信页面
    path:'/mail',
    name:'Mail',
    component: Mail
  },// lzy
  {// comments评论页面
    path:'/book/:bookId/comments',
    name: 'Comments',
    component: Comments,
  },// lzy
  {// 创作
    path:'/creation',
    name: 'Creation',
    component: Creation,
    meta: { requiresAuth: true }, // 标记需要验证
  },// lzy
  {
    path: "/Center",
    name: "Center",
    component: () =>
       import(/* webpackChunkName: "center" */ "@/views/centre.vue"),
       meta: { requiresAuth: true }, // 标记需要验证
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

// 定义一个显示登录弹窗的函数
function showLoginPopup() {
  MessageBox.alert('请先登录',  {
    confirmButtonText: '确定',
    closeOnClickModal: true, // 点击遮罩层也可以关闭对话框
    callback:() => {
    },
  });
}

// 全局前置守卫
router.beforeEach((to, from, next) => {
  console.log("1");
  // 判断目标路由是否需要登录验证
  if (to.meta.requiresAuth) {
    // 检查Vuex中的登录状态
    console.log("2");
    if (!store.getters.loggedIn) {
      console.log("3");
      // 如果未登录，则先返回首页，然后显示登录弹窗
      showLoginPopup(); // 显示登录弹窗
    } else {
      console.log("5");
      next(); // 已登录，继续到目标页面
    }
  } else {
    console.log("6");
    next(); // 不需要验证的页面直接访问
  }
});



export default router;
