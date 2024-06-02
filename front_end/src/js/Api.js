import axios from 'axios';  


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
    });  
  }
  else return 'failed!';
}  

export function novels() {
  console.log('novels');
  return axios.get('/novels/novel');
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