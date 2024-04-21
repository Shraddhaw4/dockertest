pipeline {
    agent {label 'packer'}
  
    stages {
        stage('Checkout') {
            steps {
                    // Checkout the code from your private Git repository
                git "https://github.com/Shraddhaw4/dockertest.git"
            }
        }
      
        stage('Build') {
            steps {
                // Activate a virtual environment (if needed)
                sh 'sudo yum -y install python3-pip'
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install flask'
              
                // Build the Python script
                sh 'nohup python app.py'
                sh 'echo curl localhost:3000'
            }
        }
    }

    post {
        success {
            // This block is executed when the build is successful
            echo 'Build successful!'
        }
        failure {
            // This block is executed when the build fails
            echo 'Build failed!'
        }
    }
}
