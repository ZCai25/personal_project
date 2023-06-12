# Projects
## A list of personal and group projects in data science and data engineering
- Data Science
    - Machine learning
        - Feature importance
        - Clustering methods
        - Random Forest model on Non-profit demographic data (blog post link https://blog.candid.org/post/who-is-sharing-nonprofit-demographic-data-with-candid/)
- Data Engineering
    - Reddit sentiment analysis pipeline
        - The project aims to develop an automated scalable machine-learning pipeline to perform
clustering and sentiment analysis of world news on Reddit. The main objective is to apply the
concepts learned from Distributed Data Systems to collect, preprocess, and transform data into
useful information. The project will produce word clouds and sentiment analysis, which will help
understand the sentiment of the news.
    - Startup project pipeline
        - The Tabletop Roleplaying Game (TTRPG) industry has seen rapid growth over the last five years and is expected to grow even further in the coming years. In 2021 the industry was worth $2.5 Billion and is estimated to grow at a CAGR of 5.3% until 2031. This large market is one of the fastest growing spaces for creative content creators to turn their imaginations into dollars. The creative process is a both long and highly skilled process, which makes it a perfect candidate for automation through a Large Language Model (LLM). Rather than relying on the imagination of a creative person, the idea is to use a LLM to take the place of the creative process and generate content rapidly and without a subject matter expert in the loop. 
        - Our data collection process involves gathering data from various sources such as pdf books, Reddit, and Discord using Python Reddit PRAW, AWS Glue. We then clean and preprocess the data to ensure it is ready for analysis.To store and manage our data, we use AWS S3 (Simple Storage Service). S3 provides us with scalable, durable, and secure object storage for our data. This allows us to easily store and retrieve large volumes of data, and ensures that our data is always available when we need it. Next, we use AWS Sagemaker to train our data. Sagemaker is a fully-managed service that provides developers and data scientists with the ability to build, train, and deploy machine learning models at scale. With Sagemaker, we can easily create and train machine learning models using a variety of algorithms and frameworks.Once our model is trained, we send the model endpoint to AWS Lambda. Lambda is a serverless compute service that allows us to run code without provisioning or managing servers. By using Lambda, we can easily and quickly deploy our model without worrying about managing infrastructure.To expose our model to the outside world, we use AWS API Gateway. API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. With API Gateway, we can easily create RESTful APIs that allow us to interact with our model.Finally, we host our webapp on AWS Elastic Beanstalk.  With  Elastic Beanstalk, we can easily deploy and manage our webapp, and ensure that it is always available to our users.Overall, our AWS pipeline provides us with a scalable, secure, and cost-effective way to manage our data, train our machine learning models, and deploy our webapp. By leveraging the power of AWS, we are able to focus on building our business, while AWS handles the infrastructure and operations.
        ![AWS_diagram](https://github.com/matthewmarwedel/Startup_Team/assets/108997562/d263f65d-5d85-4a95-8ff5-b01c0c242d09)
Link to presentation https://docs.google.com/presentation/d/10pUPVi3k8sdEuwAYxStoJ8-PmPd3O2wUz2fwJEJEeHA/edit?usp=sharing
