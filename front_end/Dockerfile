# 使用官方Node.js镜像作为基础镜像
FROM node:16

# 创建和设置工作目录
WORKDIR /app

# 将package.json和package-lock.json复制到工作目录
COPY package*.json ./

# 安装项目依赖
RUN npm install

# 将项目文件复制到工作目录
COPY . .

# 构建Vue项目
RUN npm run build

# 使用nginx作为生产环境的Web服务器
FROM nginx:alpine

# 将构建好的项目文件复制到nginx的默认静态文件目录
COPY --from=0 /app/dist /usr/share/nginx/html

# 暴露nginx的默认端口
EXPOSE 80

# 启动nginx
CMD ["nginx", "-g", "daemon off;"]
