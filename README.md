# New product demand forecasting via Content based learning for multi-branch stores: Ali and Nino Use Case

---
## 1. Overview and motivation

Forecasting sales is always a challenging task because of the many variables and unknown factors involved. The job becomes all the more difficult when you’re forecasting sales of a new product because you have no past performance on which to base your estimates.

Classic demand forecasting methods assume the availability of sales data for a certain historical period, which is obviously not the case when concerning a new product. Most research papers and approaches are limited either to a specific category of goods or use sophisticated marketing methods.

Despite the difficulties, sales forecasts are necessary for planning the resources you will need to meet actual demand, including inventory, staff and cash flow. A sales forecast is also an important tool in measuring the performance of your sales, marketing and operations.  In production, forecasting is also needed to decide what types of goods to produce. In management, decision makers can optimize processes based on accurate forecasts.


The proposed work is based on Ali and Nino multi-branch book store's sales data. Dataset is contains 23.345 books with over 90k unique customers per month and more than 170 orders per day. Although, sales dataset was generated artifically based on human So, even small improvement in forecast accuracy can lead to significant increase of company profit and customers can buy quicker and at lower price.

The general objective of this work is to propose a forecasting method based on machine learning models to forecast the demand of new products satisfying the following conditions:
 does not depend on the type of goods;
 can work without history of sales;
 can work with large data set;
 no need for marketing research.

## 3. Success metrics
Usually framed as business goals, such as increased customer engagement (e.g., CTR, DAU), revenue, or reduced cost.

## 4. Requirements & Constraints
Functional requirements are those that must be met to deliver the project. Describe them from the customer’s point of view—how will the customer experience it and/or benefit? Specific to machine learning, we’ll have specific requirements for each application, such as:

Recommendations: Proportion of items or customers with >5 recommended items
Fraud detection: Upper bound on the proportion or count of false positives
Automated classification: Threshold on proportion or count of low-confidence predictions that require human review and approval

Non-functional/technical requirements define the quality of your system and determine how the system should be implemented. Usually, customers won’t notice them unless they’re not met (e.g., exceptionally high latency). Most systems will consider a similar set of requirements such as throughput, latency, security, data privacy, costs, etc.


## 5. Methodology

### 5.1. Problem statement

How will you frame the problem? For example, fraud detection can be framed as an unsupervised (outlier detection, graph cluster) or supervised problem (e.g., classification).

### 5.2. Data

What data will you use to train your model? What input data is needed during serving?

### 5.3. Techniques

What machine learning techniques will you use? How will you clean and prepare the data (e.g., excluding outliers) and create features?


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



