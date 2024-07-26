pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('GPT Review') {
            steps {

                
                script {

                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']], // Specify branch if needed
                        userRemoteConfigs: [[
                            url: 'https://github.com/techmaharaj/AICodeReviewer.git'
                        ]]
                    ])

                    withCredentials([string(credentialsId: 'OPENAI_API_KEY', variable: 'OPENAI_API_KEY')]){
                        withCredentials([string(credentialsId: 'GH_TOKEN', variable: 'GH_TOKEN')]) {
                            // Let GPTReview review the code and store the review commetns
                            REVIEW = sh(script: "gptscript codereview.gpt --PR_URL=${PR_URL}", returnStdout: true).trim()
                            
                            // Prepare the markdown formatted review comment
                            def markdownReview = REVIEW.replaceAll('"', '\\"').replaceAll("'", "\\'").replaceAll("`", "\\`")
                            
                            // Post the review comment to the GitHub PR
                            sh "curl -H \"Authorization: token ${GH_TOKEN}\" -X POST -d '{\"body\": \"${markdownReview}\"}' '${PR_COMMENTS_URL}'"
                    }
                    }
                }
            }
        }

        stage('Check PR Status') {
            steps {
                script {
                    // Check if REVIEW contains 'Require Changes'
                    if (REVIEW.contains('Require Changes')) {
                        echo 'Code Requires Changes'
                        currentBuild.result = 'FAILURE' // Mark the build as failed
                        error 'Code Requires Changes' // Terminate the build with an error
                    }
                    
                    // Check if REVIEW contains 'Approved'
                    if (REVIEW.contains('Approved')) {
                        echo 'Code Approved'
                        // Additional steps if needed for approval
                    }
                }
            }
        }
    }

}
