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
    stage('Deploy') {
      steps {
          withCredentials([usernamePassword(credentialsId: 'DOCKER_REGISTRY_CREDS', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
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
