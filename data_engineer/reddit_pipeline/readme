## Problem / Motivation Statement
The project aims to develop an automated scalable machine-learning pipeline to perform
clustering and sentiment analysis of world news on Reddit. The main objective is to apply the
concepts learned from Distributed Data Systems to collect, preprocess, and transform data into
useful information. The project will produce word clouds and sentiment analysis, which will help
understand the sentiment of the news.

## Dataset
Data source: Reddit API https://www.reddit.com/dev/api
● Size of dataset: 113,000 comments in 12 files (1 MB each), 1,100 posts in 12 files (50 KB
each)
● Data format: .csv files in GCP, JSON in MongoDB
● Data types: String, DateTime, integer
● Missing values: None
● Time range: 2/25/23 - 3/8/23

## Analytic Goals
With the posts data set, the goal was to cluster posts by topics and analyze the sentiment of the
comments. In order to do this, we had to tokenize the post titles, remove stop words, and vectorize
post titles. Then we clustered the posts using k-means. We wanted to create word clouds for each
cluster if they have distinct topics with relevant phrases.
With the comments dataset, we aimed to analyze the sentiments of select topics into positive,
negative, or neutral. We would also alter the thresholds for sentiment to better align with
comment sentiment. Overall, we hope to uncover some insights through clustering and sentiment
analysis. For example, we want to find out if some subreddits are more positive or negative and
what is the sentiment of trending posts. To communicate our findings, we want to visualize output
using a word cloud to highlight frequent words or topics in the subreddits and how the sentiment
changes over time.

## Data Engineering Pipeline
The first few steps of the pipeline were all performed via a Directed Acyclic Graph (DAG) file that
we pushed through Apache Airflow. The DAG file began the pipeline by extracting the relevant
data from the selected subreddits using PRAW, or Python Reddit API Wrapper, a special tool we
used to facilitate interacting with the Reddit API. The data we scraped included posts, titles,
related comments, and associated features such as karma, the subreddit of origin, and the publish
date and time.
Once we had the relevant data, we aggregated them into a DataFrame format and wrote it as a
CSV file into Google Cloud Platform, where we stored it in buckets for posts and comments,
respectively. This was followed by using a Spark Submit Operator in the DAG file to reformat the
data as JSON aggregates to move the data to MongoDB Atlas. This was all handled by the DAG file
daily at midnight UTC (4 pm PST).
Once the automated portion of the pipeline was established, we imported the data into Databricks
using an Apache Spark and MongoDB connector to import it from MongoDB Atlas. Here we have
reached the final stage of the pipeline, where we cleaned the data wherever necessary and
processed it to be input into our Word2Vec model.
