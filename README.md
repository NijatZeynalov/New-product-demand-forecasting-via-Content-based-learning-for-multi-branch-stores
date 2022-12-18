# New product demand forecasting via Content based learning for multi-branch stores: Ali and Nino Use Case

---
## 1. Overview and motivation

Forecasting sales is always a challenging task because of the many variables and unknown factors involved. The job becomes all the more difficult when you’re forecasting sales of a new product because you have no past performance on which to base your estimates.

Classic demand forecasting methods assume the availability of sales data for a certain historical period, which is obviously not the case when concerning a new product. Most research papers and approaches are limited either to a specific category of goods or use sophisticated marketing methods.


The proposed work is based on Ali and Nino multi-branch book store's sales data. Dataset is contains 23.345 books with over 90k unique customers per month and more than 170 orders per day. Although sales dataset was generated artifically, the approach can be apply to real cases and even small improvement in forecast accuracy can lead to significant increase of company profit and customers can buy quicker and at lower price.

The general objective of this work is to propose a forecasting method based on machine learning models to forecast the demand of new products satisfying the following conditions:

* does not depend on the type of goods;

* can work without history of sales;

* can work with large data set;

* no need for marketing research.


## 2. Methodology

### 2.1. Problem statement

The proposed work satisfies initial conditions because it meets all the requirements – forecasting demand without any marketing research and to work independent of the type of goods and historical data, so the goal of the work has been achieved. Community can use this model for predicting software development which could successfully work with very complex problems of predicting new good demand. This work can be used by companies’ analysts for optimizing sales assortment, planning and logistic optimization, as well as, can be useful for increasing the accuracy of other prediction systems as part of committee.

### 5.2. Data

As mentioned early, as a train data, 23.345 books have been scraped from Ali and Nino book-store website. Then, sales data has been generated based on each branch's characteristics (location, possible most sold books, the number of potential customers and etc.). Holidays, weekend-weekdays, customer purchasing power that varies based on various influences (COVID 19 etc.) taken into account and the dataset was designed accordingly.

### 5.3. Techniques

The proposed work can be divided into two main parts

__| Content-based filtering__

The goal behind content-based filtering is to classify products, learn what the product look likes, look up those products in the database, and then recommend similar things.

|| Sales forecasting


## 6. Implementation

### 6.1. High-level design

![arthitecture](https://user-images.githubusercontent.com/31247506/204340965-6ca7eba7-d12d-4f8b-9b58-b8e94a056269.jpg)

### 6.2 Technical implementation


### 6.3. Infra

How will you host your system? On-premise, cloud, or hybrid? This will define the rest of this section

### 6.4. Performance (Throughput, Latency)

How will your system meet the throughput and latency requirements? Will it scale vertically or horizontally?


### 6.5. Cost
How much will it cost to build and operate your system? Share estimated monthly costs (e.g., EC2 instances, Lambda, etc.)


## 7. Appendix

### 7.1. Experiment Results

Share any results of offline experiments that you conducted.



### 7.2. References

Add references that you might have consulted for your methodology.



