import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import BookDetail from "../views/BookDetail.vue";
import Bookshelf from "../views/Bookshelf.vue";
import Ebooks from "../views/Ebooks.vue";
import Rankings from "../views/Rankings.vue";
import Reports from "../views/Reports.vue";
import Search from "../views/Search.vue";
import Reader from "../views/Reader.vue";
import Comments from "../views/Comments.vue";
import Mail from "../views/Mail/Mail.vue";
import Creation from "../views/Creation/Creation.vue";
import CategoriesDetail from '@/views/CategoriesDetail.vue';


//import { MessageBox } from 'element-ui';

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
    path: "/reader",
    name: "Reader",
    component: Reader
  },
  {
    path: "/bookshelf",
    name: "Bookshelf",
    component: Bookshelf,

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
    component: Comments
  },// lzy
  {// 创作
    path:'/creation',
    name: 'Creation',
    component: Creation,
  },// lzy
  {
    path: "/Center",
    name: "Center",
    component: () =>
       import(/* webpackChunkName: "center" */ "@/views/centre.vue"),
    //meta: { requiresAuth: true }, // 标记需要验证
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});




export default router;
