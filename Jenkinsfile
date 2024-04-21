pipeline {
    agent {label 'packer'}
  
    stages {
        stage('Checkout') {
            steps {
                    // Checkout the code from your private Git repository
                git "https://github.com/Shraddhaw4/dockertest.git"
            }
        }
      
        //stage('Build') {
          //  steps {
                // Activate a virtual environment (if needed)
            //    sh 'sudo yum -y install python3-pip'
              //  sh 'python -m venv venv'
                //sh 'source venv/bin/activate'
               // sh 'pip install flask'
              
                // Build the Python script
               // sh 'nohup python app.py'
               // sh 'echo curl localhost:3000'
           // }
       // }
    //}
        
    stage('Build') {
      steps {
        sh 'docker build -t my-flask-app .'
        sh 'docker tag my-flask-app $DOCKER_BFLASK_IMAGE'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run my-flask-app python -m pytest'
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
          sh 'docker push $DOCKER_BFLASK_IMAGE'
        }
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
