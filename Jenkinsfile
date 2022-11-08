pipeline {
    agent {
        docker {
            image 'research/python-env:796206ff6753057d5053ada6bd12c673fd4188b4'
            registryUrl 'https://docker.big-xyt.com/'
            registryCredentialsId 'tu_nexus'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo ">> Building..."
            }
        }
        stage('Test') {
            steps {
                sh 'tox'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Publish') {
            steps {
                echo ">> Publishing..."
            }
        }
    }
}
