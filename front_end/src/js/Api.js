import axios from 'axios';  
 
export function login(username, password) {
  if (username & password)
    return axios.post('/users/login', {  
      username,  
      password  
    });  
  else return 'failed!';
}  