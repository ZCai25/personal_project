# Data Collection Process
- Our data collection process involves gathering data from various sources such as pdf books, Reddit, and Discord using Python Reddit PRAW and AWS Glue. We then clean and preprocess the data to ensure it is ready for analysis. To store and manage our data, we use AWS S3 (Simple Storage Service). S3 provides scalable, durable, and secure object storage for our data. This allows us to store and retrieve large volumes of data easily and ensures that our data is always available when needed. Next, we use AWS Sagemaker to train our data. Sagemaker is a fully-managed service that provides developers and data scientists with the ability to build, train, and deploy machine learning models at scale. With Sagemaker, we can easily create and train machine learning models using a variety of algorithms and frameworks. Once our model is trained, we send the model endpoint to AWS Lambda. Lambda is a serverless computing service that allows us to run code without provisioning or managing servers. Using Lambda, we can easily and quickly deploy our model without worrying about managing infrastructure. To expose our model to the outside world, we use AWS API Gateway. API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. With API Gateway, we can easily create RESTful APIs that allow us to interact with our model. Finally, we host our web app on AWS Elastic Beanstalk.  With  Elastic Beanstalk, we can easily deploy and manage our web app and ensure it is always available to our users.
# Conclusion
 - Overall, our AWS pipeline provides a scalable, secure, and cost-effective way to manage our data, train our machine learning models, and deploy our web app. By leveraging the power of AWS, we can focus on building our business while AWS handles the infrastructure and operations.
        ![AWS_diagram](https://github.com/matthewmarwedel/Startup_Team/assets/108997562/d263f65d-5d85-4a95-8ff5-b01c0c242d09)

# Presenation
- Link to presentation https://docs.google.com/presentation/d/10pUPVi3k8sdEuwAYxStoJ8-PmPd3O2wUz2fwJEJEeHA/edit?usp=sharing