pipeline {
    agent any
    
    stages {
        stage('Clear') {
            steps {
                bat 'kubectl delete deployment novel-service'
                bat 'kubectl delete deployment user-service'
                bat 'kubectl delete deployment reader-service'
                bat 'kubectl delete deployment frontend'
                
                bat 'kubectl delete svc novel-service'
                bat 'kubectl delete svc user-service'
                bat 'kubectl delete svc reader-service'
                bat 'kubectl delete svc frontend-service'
            }
        }
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                bat 'ping github.com'
                git(
                    branch: 'master',
                    credentialsId: '5d76cd9f-c6fe-4d87-97c0-3c1b35f067b5',
                    url: 'http://github.com/Ac-1d/RP2024.git'
                )
            }
        }
        stage('Build') {
            steps {
                echo 'build stage'

                // 构建后端微服务
                bat 'docker build -t novel-service-image ./RP_Novel_Service'
                bat 'docker build -t reader-service-image ./RP_Reader_Service'
                bat 'docker build -t user-service-image ./RP_User_Service'
                
                // 构建前端服务
                bat 'docker build -t frontend-image ./front_end'
            }
        }
        stage('Test') {
            steps {
                // 压力测试等
                echo 'test novel-service'
                bat 'conda activate WWW'
                bat 'python ./RP_Novel_Service/manage.py test'
                
                echo 'test reader-service'
                bat 'python ./RP_Reader_Service/manage.py test'
                
                echo 'test user-service'
                bat 'python ./RP_User_Service/manage.py test'
                
                bat 'conda deactivate'
            }
        }
        stage('Deploy') {
            steps {
                echo 'start deploy'
                
                // 部署微服务数据库
                bat 'kubectl apply -f ./k8s/db-deploy/novel.yaml'
                bat 'kubectl apply -f ./k8s/db-deploy/user.yaml'
                bat 'kubectl apply -f ./k8s/db-deploy/reader.yaml'
                
                // 后端微服务
                bat 'kubectl apply -f ./k8s/user-service.yaml'
                bat 'kubectl apply -f ./k8s/reader-service.yaml'
                bat 'kubectl apply -f ./k8s/novel-service.yaml'
                
                // 前端服务
                bat 'kubectl apply -f ./k8s/frontend-deployment.yaml'
                
                bat 'kubectl apply -f ./k8s/components.yaml'

                // HPA VPA
                bat 'kubectl apply -f ./k8s/frontend-hpa.yaml'
                bat 'kubectl apply -f ./k8s/novel-hpa.yaml'
                bat 'kubectl apply -f ./k8s/user-hpa.yaml'
                bat 'kubectl apply -f ./k8s/reader-hpa.yaml'
                
                bat 'kubectl apply -f ./k8s/frontend-vpa.yaml'
                bat 'kubectl apply -f ./k8s/novel-vpa.yaml'
                bat 'kubectl apply -f ./k8s/user-vpa.yaml'
                bat 'kubectl apply -f ./k8s/reader-vpa.yaml'
                
                // bat 'kubectl delete -f .'
            }
        }
    }
}
