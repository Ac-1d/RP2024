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
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
