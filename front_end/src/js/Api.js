import axios from 'axios';  
// 跨域问题暂时通过代理解决了，但是部署之后还要用其他方法

const replyLimitTime = 5000;// 5秒响应时间

// 查找小说类别
export function category() {
  console.log('category');
  return axios.get('/novels/category_all');
}

// 查找某一类的小说
export function categoryNovels(category_id) {
  console.log('category novels');
  return axios.get('/novels/category?id=' + category_id);
}

// 查找所有小说
export function novels() {
  console.log('novels');
  return axios.get('/novels/novel');
}

// 查找小说详细信息
export function novelDetail(novel_id) {
  console.log('novel detail');
  return axios.get('/novels/detail?id=' + novel_id );
}

// 查询全部章节
export function novelChapter(novel_id) {
  return axios.get('/novels/chapter_list?id=' + novel_id);
}

// 查询某章某节内容
export function novelContent(novel_id, chapter_id) {
  return axios.get('/novels/chapter?id=' + novel_id + 
  '&chapter_id=' + chapter_id);
}