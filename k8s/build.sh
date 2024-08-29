#build.sh
# 构建镜像
# 上传docker hub仓库

docker build -t backend-image ../back_end
docker tag backend-image lizhy462/backend:dev
docker push lizhy462/backend:dev

docker build -t mysql-image ../db
docker tag mysql-image lizhy462/db:dev
docker push lizhy462/db:dev

# 使用k8s部署
kubectl apply -f frontend-deployment.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f mysql-deployment.yaml
kubectl apply -f frontend-hpa.yaml
kubectl apply -f backend-hpa.yaml
kubectl apply -f frontend-vpa.yaml
kubectl apply -f backend-vpa.yaml

### 微服务

kubectl apply -f frontend-deployment.yaml
kubectl apply -f novel-service.yaml
kubectl apply -f user-service.yaml
kubectl apply -f reader-service.yaml
kubectl apply -f mysql-deployment.yaml

kubectl apply -f frontend-hpa.yaml
kubectl apply -f novel-hpa.yaml
kubectl apply -f user-hpa.yaml
kubectl apply -f reader-hpa.yaml

kubectl apply -f frontend-vpa.yaml
kubectl apply -f novel-vpa.yaml
kubectl apply -f user-vpa.yaml
kubectl apply -f reader-vpa.yaml

### 删除
kubectl delete -f .


