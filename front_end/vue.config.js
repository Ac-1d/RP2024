// vue.config.js  
module.exports = {  
  devServer: {  
    proxy: {  
      '/api': {  
        target: 'http://127.0.0.1:8000', // 这里替换为你的后端服务器地址，例如：'http://localhost:3000'  
        ws: true, // 是否代理websockets  
        changeOrigin: false, // 如果设置为true，那么本地将不会虚拟一个域名，适合跨域请求 
      },  
      // 你可以添加更多的代理规则...  
    }  
  }  
};