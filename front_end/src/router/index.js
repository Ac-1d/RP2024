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
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Comments from "../views/Comments.vue"; // 调试用，合并的时候可以删掉
import CategoriesDetail from "../views/CategoriesDetail.vue"; // 引入新的详细分类页面组件

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
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
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/register",
    name: "Register",
    component: Register
  },
  {
    path: "/comments",
    name: "Comments",
    component: Comments
  },
  {
    path: "/center",
    name: "Center",
    // route level code-splitting
    // this generates a separate chunk (center.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "center" */ "../views/centre.vue")
  },
  {
    path: "/categories-detail",
    name: "CategoriesDetail",
    component: CategoriesDetail
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
