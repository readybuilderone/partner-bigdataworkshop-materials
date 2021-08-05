# 概述

​    AWS合作伙伴数据分析动手训练营，面向AWS中国区合作伙伴，赋能合作伙伴架构师通过使用AWS的数据分析服务，进行结构化和非结构化数据的摄取、存储、转换、分析。为合作伙伴的解决方案架构师提供了一天的动手实验，包括了Amazon Kinesis，AWS Glue，Amazon Athena和Amazon SageMake等服务。详情可参看：http://bigdata.awspsa.com/0-introduction.html 。

​    本代码仓库包含了动手训练营动手的相关代码。

# 数据分析动手训练营大纲

​     训练营分为基础和进阶两个部分。

​     在基础模块，通过5个动手实验，帮助参与者构建一个完整电影推荐方案，包含数据爬取，存储，分析，处理，展现 以及利用机器学习做智能推荐的完整流程。架构图如下：

![image-20210806003002404](./images/arch.png)

### 以数据分析负载的不同环节拆分成以下5个实验：

#### 实验1

从互联网上的外部来源获取电影数据集，将其存放在S3作为原始数据层，然后将其加载到Dynamo DB。在企业中，类似的数据可能已经存在于某些RDS，NoSQL或数据仓库系统中。可以一次性将数据作为批处理或实时数据流摄取。

#### 实验2

根据具体的需求用例，可能需要同时进行批处理和流处理，或者仅需要进行批处理或流处理。本实验将使用DMS一次性将一个完整的数据加载到Dynamo DB中，然后使用Lamda函数作为源数据生成模拟器将新记录传输到Kinesis流中以模拟流数据加载。

#### 实验3

在本实验中，您将使用Glue数据目录在S3和DynamoDB中存储的数据上定义架构。参与者对数据执行ETL，以准备将其用于机器学习和可视化。

#### 实验4

结合不同的行业或业务，会在实际需求中定义不同的举足轻重的业务指标，将他们可视化为业务报表以遍业务人员，决策人员进行优化业务的判断，在这里，我们实验superset和Athena搭建可视化报表。

#### 实验5

本实验将使用Amazon Sagemaker进行模型训练和推理。



## 架构图

pass

## 模块

pass



# References





