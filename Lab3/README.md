# 实验3: 利用Glue做ETL和数据治理
## 场景
在实验3中，使用Glue数据目录在S3和DynamoDB中存储的数据上定义架构。参与者对数据执行ETL，以准备将其用于机器学习和可视化。

## 架构图
![1-arch](../images/3-arch.png)

## 代码清单
- 使用glue来做ETL工作
> glue_etl.py