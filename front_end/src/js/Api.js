import axios from 'axios';  

// 登录
// 注意，这里如果会返回400错误，先看看用户名密码是否正确
// 400并不是因为请求没发出去，而是验证失败
// 只要请求的端口是8000,（后端的端口）应该就没问题

// 跨域问题暂时通过代理解决了，但是部署之后还要用其他方法
export function login(username, password) {
  console.log('log in');
  if (username && password) {
    console.log({
      username: username,  
      password: password  
    });
    return axios.post("/users/login", {  
      "username": username,  
      "password": password  
    })
    .catch(function (error) {  
      if (error.code === 'ECONNABORTED') {  
        // 请求因超时而被中断  
        console.error('请求超时！');  
      } else {  
        // 处理其他类型的错误  
        console.error(error);  
      }  
    });  
  }
  else return 'failed!';
}  

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



// export function login2() {
//   let baseURL = 'http://127.0.0.1:8000';
//   let ruleForm = {"username":"A", "password":"123"};
//   console.log('log in');
//   fetch(baseURL + '/users/login', {
//     method: 'post',
//     headers: {'content-type':'application/json'},
//     body: JSON.stringify(ruleForm)
//   }).then(async Response => {
//     // loading = false;
//     if (Response.ok) {
//       return Response.json();
//     } else {
//       const r = await Response.json();
//       return await Promise.reject(r);
//     }
//   }).then(data => {
//     console.log('success');
//     console.log(data);
//   }).catch(error => {
//     this.$message({
//       type: 'error',
//       message: error && error.message,
//       showClose: true
//     });
//     // loading = false;
//   })
// }