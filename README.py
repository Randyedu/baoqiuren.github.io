https://github.com/marcelobusico/groovy-github-changelog-generator

  
  import groovy.json.JsonSlurperClassic

  
  https://github.com/daos-stack/pipeline-lib/blob/c8bef179ab947b93f1ec612d62aab8a4a6823ee2/vars/stepResult.groovy
node {
    try {
        stage("Clone SeedJob Manager Repository") {
            git branch: "master", url: "https://github.com/Dkra/jenkins-job-dsl-example"
        }

        stage("Build ListView") {
            jobDsl ignoreMissingFiles: true, targets: "./listView/*.groovy"
        }

        stage("Build SeedJob from [projects.json]") {
            def json = readFile(file: "./project/projects.json")
            def jobArray = new JsonSlurperClassic().parseText(json)
            jobArray.each { app -> createProjectJobs(app) }
        }

    } catch (err) {
        throw err
    } finally {
        deleteDir()
    }
}


def createProjectJobs(app) {
    stage("Build [${app.name}] Seed Job") {
        sh """
            echo "------Start Building [${app.name}]------"
        """
        git branch: "${app.branch}", url: "${app.repo_url}"
        jobDsl ignoreMissingFiles: true, targets: "./jenkins/**/seedJob.groovy"
        sh """
            ls -al
            echo "----------------------------------------"
        """
    }
}

https://github.com/altairlage/sample-conan-lib-in-jenkins/blob/602cfc68bf5232f163bf2f5ea3a1230c0a3711f5/Build-Library/src/org/altabuild/json/JsonParser.groovy
// example of custom API
import groovy.json.JsonSlurperClassic 

@NonCPS
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}

def repo = "edwardviaene/jenkins-course"

def token = httpRequest authentication: 'bitbucket-oauth', contentType: 'APPLICATION_FORM', httpMode: 'POST', requestBody: 'grant_type=client_credentials', url: 'https://bitbucket.org/site/oauth2/access_token'
def accessToken = jsonParse(token.content).access_token
def pr = httpRequest customHeaders: [[maskValue: true, name: 'Authorization', value: 'Bearer ' + accessToken]], url: "https://api.bitbucket.org/2.0/repositories/${repo}/pullrequests"

for (p in jsonParse(pr.content).values) { 
    println(p.source.branch.name)
}


https://github.com/harkeshkumar/test-parameter/blob/cd21170866079f3ed9ef19a5612b6731959ac676/jenkins/FileHelper.groovy
