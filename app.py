from flask import Flask, render_template, jsonify
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your NewsAPI key
API_KEY = os.getenv('NEWS_API_KEY')
if not API_KEY:
    raise ValueError("No NEWS_API_KEY found in environment variables. Please add it to your .env file.")

newsapi = NewsApiClient(api_key=API_KEY)

app = Flask(__name__)

PROFILE = {
    'name': 'Abiola Shittu',
    'bio': 'Abiola Shittu is an experienced Cloud Engineer with over 10 years of expertise in information technology. Throughout his career, he has worked extensively with key DevOps tools to facilitate seamless web application deployments, showcasing his proficiency in cloud infrastructure and deployment automation. His dedication and technical skills have made him a valuable asset in the IT field.',
    'email': 'abiola.shiba@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/abiola-shittu/',
    'github': 'https://github.com/shittuay',
    'resume': 'images/Docs/resume.docx',
    'picture': 'images/Abiola.jpeg',
    'profile': 'images/Docs/Profile.pdf'
}

ACCOMPLISHMENTS = [
    {'title': 'Project 1', 'description': 'Web-application project deployment on AWS Cloud using Terraform and Jenkins'},
    {'title': 'Project 2', 'description': 'Iam key rotation automation using AWS Lambda and CloudWatch Events'},
    {'title': 'Project 3', 'description': 'Creating bulk EC2 instances using Terraform'},
    {'title': 'Project 4', 'description': 'creating a VPC with public and private subnets using cloudformation '},
    {'title': 'Project 5', 'description': 'used aws security hub to monitor security compliance of aws resources'},
    {'title': 'Project 6', 'description': 'created mysql database on aws rds and connected to an ec2 instance using terraform'},
    {'title': 'Project 7', 'description': 'work on several migration projects from on-premises to aws cloud using aws server migration service'},
    {'title': 'Project 8', 'description': 'created control tower and landing zone using aws organizations and service catalog'},
    {'title': 'Project 9', 'description': 'created auto scaling, target groups and load balancers using terraform and attaching a waf to the load balancer'},
    {'title': 'Project 10', 'description': 'creating a blue-green deployment using Aws ecs and code commit, code deploy and code pipeline'},
    {'title': 'Project 11', 'description': 'Python-flask web application deployment on Kubernetes cluster using Helm and Kustomize'},
    {'title': 'Project 12', 'description': 'created a CI/CD pipeline using Jenkins, sonarqube, nexus and Github'},
    {'title': 'Project 13', 'description': 'created s3 bucket and enabled versioning and lifecycle policy using terraform'},
    {'title': 'Award', 'description': 'AWS Cloud Practitioner Certification'},
    {'title': 'Award', 'description': 'AWS Cloud Quest Certification'},
    {'title': 'Award', 'description': 'AWS DevOps Engineer Certification'},
    {'title': 'Award', 'description': 'ITIL Foundation Certification'},
]

BLOG_POSTS = [
    {
        'title': 'The Importance of Cloud Technology with the Addition of AI',
        'content': '''
            <p>The integration of Artificial Intelligence (AI) into cloud technology is transforming the landscape of IT and business operations. Cloud technology has already revolutionized the way organizations manage and deploy their applications, providing scalable, flexible, and cost-effective solutions. With the addition of AI, the cloud environment is set to become even more powerful and efficient.</p>

            <p>AI enhances cloud technology by offering advanced data analytics, machine learning, and automation capabilities. This integration allows for more intelligent data processing, improved decision-making, and streamlined operations. For instance, AI-powered analytics can process vast amounts of data quickly, providing insights that were previously unattainable.</p>

            <p>Moreover, AI-driven automation in the cloud can optimize resource management, reduce operational costs, and improve service delivery. Tasks that used to require manual intervention can now be automated, leading to increased efficiency and reduced risk of human error.</p>

            <p>The combination of AI and cloud technology also supports the development and deployment of intelligent applications. These applications can learn from user interactions, adapt to changing environments, and provide personalized experiences. This capability is particularly beneficial in industries such as healthcare, finance, and retail, where real-time data analysis and adaptive responses are crucial.</p>

            <p>In summary, the addition of AI to cloud technology is set to transform the cloud environment by enhancing data analytics, automation, and the development of intelligent applications. This transformation promises to drive innovation, improve operational efficiency, and deliver better user experiences across various industries.</p>
        '''
    },
    {
        'title': 'Harnessing the Power of Kubernetes for Deployments',
        'content': '''
            <p>Kubernetes has become a cornerstone in modern application deployments due to its powerful orchestration capabilities and ability to manage containerized applications at scale. It automates deployment, scaling, and operations of application containers across clusters of hosts, providing a resilient and efficient system.</p>

            <p>One of the key benefits of using Kubernetes is its ability to provide a consistent and reproducible deployment environment. This ensures that applications run the same way in development, testing, and production environments, reducing the risk of environment-related issues.</p>

            <p>Users can take full advantage of Kubernetes by integrating it with various DevOps tools to create a robust tech stack. Tools such as Jenkins for CI/CD, Prometheus for monitoring, and Helm for package management work seamlessly with Kubernetes to enhance its capabilities. Jenkins pipelines can automate the build, test, and deployment process, ensuring that new code changes are continuously integrated and deployed with minimal human intervention.</p>

            <p>Prometheus, combined with Grafana, provides powerful monitoring and visualization, allowing users to gain insights into their applications and infrastructure. This helps in proactively identifying and resolving issues before they impact end users.</p>

            <p>Helm simplifies the deployment of complex applications by using Helm charts, which are packages of pre-configured Kubernetes resources. This makes it easier to deploy and manage applications on Kubernetes clusters, saving time and reducing complexity.</p>

            <p>By leveraging Kubernetes alongside these DevOps tools, users can build a tech stack that is not only powerful and scalable but also resilient and future-proof. This combination supports rapid development cycles, improved reliability, and efficient operations, ensuring that the tech stack can withstand the test of time.</p>

            <p>In summary, Kubernetes, when used with complementary DevOps tools, provides a robust foundation for modern application deployments. Its ability to automate and manage containerized applications, combined with the power of CI/CD, monitoring, and package management tools, enables organizations to build a resilient and enduring tech stack.</p>
        '''
    },
    {
        'title': 'Deploying a Flask App on Render',
        'content': '''
            <h3>Steps to Deploy a Flask App on Render</h3>
            <ol>
                <li>
                    <strong>Create a Render Account:</strong>
                    <p>Sign up for a free account on <a href="https://render.com/">Render</a>.</p>
                </li>
                <li>
                    <strong>Prepare Your Flask App for Deployment:</strong>
                    <p>Ensure your Flask app is structured properly. Your project directory should include all necessary files and dependencies.</p>
                    <p>Create a <code>requirements.txt</code> file to list all the Python dependencies. You can generate this file by running:</p>
                    <pre><code>pip freeze > requirements.txt</code></pre>
                    <p>Create a <code>Procfile</code> to specify the command to run your application. The <code>Procfile</code> should contain:</p>
                    <pre><code>web: gunicorn app:app</code></pre>
                    <p>Replace <code>app</code> with the name of your main Python file, without the <code>.py</code> extension.</p>
                </li>
                <li>
                    <strong>Initialize a Git Repository:</strong>
                    <p>If you haven't already, initialize a Git repository in your project directory:</p>
                    <pre><code>git init</code></pre>
                    <p>Commit your files:</p>
                    <pre><code>git add .\ngit commit -m "Initial commit"</code></pre>
                </li>
                <li>
                    <strong>Push Your Code to GitHub:</strong>
                    <p>Create a new repository on GitHub and push your local repository to GitHub:</p>
                    <pre><code>git remote add origin https://github.com/yourusername/your-repo-name.git\ngit branch -M main\ngit push -u origin main</code></pre>
                </li>
                <li>
                    <strong>Create a New Web Service on Render:</strong>
                    <p>Log in to your Render account.</p>
                    <p>Click on the "New" button and select "Web Service".</p>
                    <p>Connect your GitHub account and select the repository you want to deploy.</p>
                    <p>Render will automatically detect the Flask app. Configure the following settings:</p>
                    <ul>
                        <li><strong>Environment:</strong> Python 3</li>
                        <li><strong>Build Command:</strong> (Render will use the default <code>pip install -r requirements.txt</code>)</li>
                        <li><strong>Start Command:</strong> <code>gunicorn app:app</code> (Replace <code>app</code> with your main Python file name)</li>
                    </ul>
                </li>
                <li>
                    <strong>Deploy Your App:</strong>
                    <p>Click "Create Web Service".</p>
                    <p>Render will start the deployment process, which includes building the environment, installing dependencies, and starting your Flask app.</p>
                    <p>Once the deployment is complete, Render will provide you with a URL to access your live Flask app.</p>
                </li>
            </ol>
            <h3>Summary</h3>
            <p>Deploying a Flask app on Render is a user-friendly process, ideal for developers working on projects like a profile page website with Python, HTML, and CSS. Render takes care of the infrastructure, allowing you to focus on building your application without worrying about server management. The integration with GitHub makes it easy to update your app by simply pushing new commits to your repository.</p>
        '''
    },
    {
        'title': 'Managing Single Sign-On with Temporary Access Keys and Automating Key Rotation with AWS Lambda',
        'content': '''
            <h3>Introduction</h3>
            <p>In the world of cloud computing, securing access to resources is paramount. One common approach is using Single Sign-On (SSO) with temporary access keys. However, for workloads that cannot be terminated if the temporary keys expire, a different strategy is needed to avoid disruptions. In such cases, creating an IAM user with permanent access keys is a viable solution. As a DevOps engineer, it's crucial to implement an automation process to reissue these keys regularly to maintain security and compliance. This post will walk you through how to set up this automation using AWS Lambda, Secrets Manager, and EventBridge.</p>

            <h3>Why Use Single Sign-On with Temporary Access Keys?</h3>
            <p>SSO with temporary access keys is a widely used method for providing secure, time-limited access to AWS resources. It reduces the risk of long-term credentials being compromised since the keys are short-lived and automatically expire. However, some workloads require uninterrupted access and cannot afford the disruption caused by expiring keys.</p>

            <h3>The Challenge of Expiring Keys</h3>
            <p>For workloads that cannot tolerate interruptions, relying solely on temporary keys can be problematic. When these keys expire, the workload loses access until new keys are issued. To avoid this, we can create an IAM user with permanent access keys, ensuring continuous access. However, permanent keys come with their own risks if not managed properly.</p>

            <h3>Solution: Automating Key Rotation</h3>
            <p>To mitigate the risks associated with permanent keys, it is essential to rotate them regularly. AWS Lambda, combined with Secrets Manager and EventBridge, provides a powerful automation framework to achieve this.</p>

            <h3>Step-by-Step Guide</h3>
            <ol>
                <li><strong>Create an IAM User with Permanent Access Keys</strong>
                <p>First, create an IAM user and generate access keys for it. These keys will be used by the workload that requires uninterrupted access.</p>
                </li>
                <li><strong>Store the Keys in AWS Secrets Manager</strong>
                <p>Store the generated access keys in AWS Secrets Manager to keep them secure and easily retrievable. Create a new secret and add the access key ID and secret access key.</p>
                <pre><code>aws secretsmanager create-secret --name myAccessKeys --secret-string '{"AccessKeyId":"AKIA...", "SecretAccessKey":"wJal..."}'</code></pre>
                </li>
                <li><strong>Set Up AWS Lambda Function for Key Rotation</strong>
                <p>Create an AWS Lambda function that will rotate the access keys every three months. The function will generate new keys, update the secret in Secrets Manager, and deactivate the old keys.</p>
                <pre><code>import boto3
import json
from datetime import datetime

iam_client = boto3.client('iam')
secretsmanager_client = boto3.client('secretsmanager')

def rotate_access_keys(event, context):
    user_name = 'your-iam-user-name'
    secret_name = 'myAccessKeys'
    
    # Create new access key
    response = iam_client.create_access_key(UserName=user_name)
    new_access_key = response['AccessKey']
    
    # Update the secret with new access keys
    new_secret_string = json.dumps({
        "AccessKeyId": new_access_key['AccessKeyId'],
        "SecretAccessKey": new_access_key['SecretAccessKey']
    })
    secretsmanager_client.update_secret(SecretId=secret_name, SecretString=new_secret_string)
    
    # List all access keys and delete the oldest one if there are more than two
    response = iam_client.list_access_keys(UserName=user_name)
    access_keys = sorted(response['AccessKeyMetadata'], key=lambda x: x['CreateDate'])
    if len(access_keys) > 2:
        iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_keys[0]['AccessKeyId'])
    
    print(f"Access keys rotated at {datetime.now()}")

# Example event to test the function locally
if __name__ == "__main__":
    rotate_access_keys({}, {})</code></pre>
                </li>
                <li><strong>Deploy the Lambda Function</strong>
                <p>Deploy the Lambda function and configure it to have the necessary IAM roles and permissions to manage IAM users and access keys, as well as Secrets Manager.</p>
                </li>
                <li><strong>Set Up EventBridge to Trigger Lambda Function</strong>
                <p>Use EventBridge (formerly CloudWatch Events) to schedule the Lambda function to run every three months.</p>
                <pre><code>aws events put-rule --schedule-expression "rate(90 days)" --name RotateAccessKeysRule
aws events put-targets --rule RotateAccessKeysRule --targets "Id"="1","Arn"="arn:aws:lambda:region:account-id:function:function-name"</code></pre>
                </li>
            </ol>

            <h3>Conclusion</h3>
            <p>By automating the rotation of IAM user access keys using AWS Lambda, Secrets Manager, and EventBridge, you can ensure your workloads have continuous access to AWS resources without the risk of key expiration. This approach enhances security by regularly updating access keys and minimizes the potential for disruptions in your operations. Implementing this solution demonstrates the proactive measures a DevOps engineer can take to maintain a secure and resilient infrastructure.</p>

            <h3>Further Reading</h3>
            <ul>
                <li><a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html">AWS IAM Best Practices</a></li>
                <li><a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">Using AWS Secrets Manager</a></li>
                <li><a href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html">AWS Lambda Documentation</a></li>
                <li><a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html">Amazon EventBridge Documentation</a></li>
            </ul>

            <p>Feel free to reach out if you have any questions or need further assistance with setting up this automation!</p>
        '''
    }
]

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/profile")
def profile():
    return render_template('profile.html', profile=PROFILE, accomplishments=ACCOMPLISHMENTS)

@app.route("/blog")
def blog():
    return render_template('blog.html', blog_posts=BLOG_POSTS)

@app.route("/tech_news")
def tech_news():
    top_headlines = newsapi.get_top_headlines(category='technology', country='us')
    articles = top_headlines['articles']
    return render_template('news.html', articles=articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
