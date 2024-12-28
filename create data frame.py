# Databricks notebook source
df=spark.range(1,100)
df.write.mode('overwrite').saveAsTable('uclearning_analysis.bronze.testing_123')
