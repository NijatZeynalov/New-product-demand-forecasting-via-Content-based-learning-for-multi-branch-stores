# New product demand forecasting via Content based learning for multi-branch stores: Ali and Nino Use Case

---
## 1. Overview and motivation

Forecasting sales is a challenging task when you’re forecasting sales of a new product because you have no past performance on which to base your estimates.

Classic demand forecasting methods assume the availability of sales data for a certain historical period, which is obviously not the case when concerning a new product. Most research papers and approaches are limited either to a specific category of goods or use sophisticated marketing methods.


The proposed work is based on Ali and Nino multi-branch book store's sales data. Dataset is contains 23.345 books with over 90k unique customers per month and more than 170 orders per day. Although sales dataset was generated artifically, the approach can be apply to real cases and even small improvement in forecast accuracy can lead to significant increase of company profit and customers can buy quicker and at lower price.

The general objective of this work is to propose a forecasting method based on machine learning models to forecast the demand of new products satisfying the following conditions:

* does not depend on the type of goods;

* can work without history of sales;

* can work with large data set;

* no need for marketing research.

__and most importantly, it will help to find answers to the following questions of the company:__

__* I have never sold this product before, how will the demand be?__

__* If I order this product, how many units should I send to which branch?__


## 2. Methodology

### 2.1. Problem statement

The proposed work satisfies initial conditions because it meets all the requirements – forecasting demand without any marketing research and to work independent of the type of goods and historical data, so the goal of the work has been achieved. Community can use this model for predicting software development which could successfully work with very complex problems of predicting new good demand. This work can be used by companies’ analysts for optimizing sales assortment, planning and logistic optimization, as well as, can be useful for increasing the accuracy of other prediction systems as part of committee.

### 2.2. Data

As mentioned early, as a train data, 23.345 books have been scraped from Ali and Nino book-store website. Then, sales data has been generated based on each branch's characteristics (location, possible most sold books, the number of potential customers and etc.). Holidays, weekend-weekdays, customer purchasing power that varies based on various influences (COVID 19 etc.) taken into account and the dataset was designed accordingly.

### 2.3. Techniques

The proposed work can be divided into two main parts:

__| Content-based filtering__

The goal behind content-based filtering is to classify products, learn what the product look likes, look up those products in the database, and then recommend similar things. When the representative add new book's characteristics (name, genre, author name, collection, language, publishing year and etc.) which has never been sold in the store, the system returns 3 most similiar book.  

__|| Sales forecasting__

Given similiar books are the input of the sales forecasting algorithm which is try to determines the number of sales by predicting consumer behavior with these books from past transactions. 


## 3. Implementation

### 3.1. High-level design

![arthitecture](https://user-images.githubusercontent.com/31247506/204340965-6ca7eba7-d12d-4f8b-9b58-b8e94a056269.jpg)

### 3.2 Technical implementation

1. After the user adds new book with its features, our content filtering model comes into play. It utilizes properties and the metadata of a particular book to suggest other items with similar characteristics.  We use the cosine function to compute the similarity score between books, where each book will have a similarity score with every other book in our dataset.

Cosine similarity architecture

![Cosine similarity](https://miro.medium.com/max/1518/1*LF62aNT2XqWioSu4Beoi5Q.png)

2. When we determine most similiar three books, we use Temporal Fusion Transformer demand forecasting algorithm in order to predict future 3 month sales of these books over the all branches. It is a large model and will therefore perform much better with more data. Bu ghe biggest advantages of TFT are versatility and interpretability. In other words, the model works with multiple time series, with all sorts of inputs (even categorical variables).

Top level architecture of TFT, along with its main components

![Top level architecture of TFT, along with its main components (Source)](https://miro.medium.com/max/4800/1*7rXe_MVn5QI9oLP2vrMdvQ.webp)


3. The last step is to build the Fast API. When the user sends a book features to the uvicorn server which interacts with the API to trigger the prediction model. As a result, the model returns the result that is shown to the user in a JSON format. After creating the API, I create a Docker Image in which the app will the running.


![Top level architecture of API (Source)](https://miro.medium.com/max/1400/1*GvRd2gpkuUkg_x78N4QqaA.webp)

Fast API provides a complete dashboard for interacting with our API.

![Result](https://user-images.githubusercontent.com/31247506/208299045-b89de2ca-5047-48fc-8174-e4e702c0a6e0.png)

By looking at the API Response body section, we can see its result as follow:

```
[{"filial_ad":"Əli və Nino-3","kitab_say":49}, {"filial_ad":"Əli və Nino-6","kitab_say":23}, {"filial_ad":"Əli və Nino-8","kitab_say":16}, {"filial_ad":"Əli və Nino-9","kitab_say":9}]

```
As we expected, it shows how many units predicted to sold in the next 3 months for each branch.


Now it is time to deploy it into a Docker container. The idea behind containerization is that it will make our API portable and able to run uniformly and consistently across AWS, in a more secured way.

### 3.3. Infra

I am hosting the system on AWS ECS which is one of the best tools to easily deploy containerized applications from the docker hub registry. Everything that I used in this project is supposed to be without any additional charge, so anyone can use AWS free tier to follow along. 


### 3.4. Performance (Throughput, Latency)

The system meet the throughput and latency requirements as much as possible. Content filtering module app. takes 0.1-0.2 seconds and sales forecasting module takes 7-8 seconds for per request.


## 4. Appendix


### 4.1. References

I am adding references that I have consulted for my methodology.

[Step-by-step Approach to Build Your Machine Learning API Using Fast API](https://towardsdatascience.com/step-by-step-approach-to-build-your-machine-learning-api-using-fast-api-21bd32f2bbdb)

[Fast API, Docker and AWS ECS to Deploy ML Model](https://www.analyticsvidhya.com/blog/2022/09/fast-api-docker-and-aws-ecs-to-deploy-machine-learning-model/)

[Time Series Made Easy in Python](https://unit8co.github.io/darts/)

[Content-Based Recommendation System](https://studymachinelearning.com/content-based-recommendation-system/)

[How to forecast sales of a new product](https://www.bdc.ca/en/articles-tools/marketing-sales-export/sales/forecasting-sales-of-new-products)
