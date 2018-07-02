# -*- coding: utf-8 -*-
"""
Created on Thu May 10 23:49:14 2018

@author: Administrator
"""

import pandas as pd
import numpy as np

store=pd.read_csv("E:\python\Python Assignments\DataSets\Store.csv",sep=",",header=0,encoding="Latin")
list(store)
store.columns
###•	How many unique cities are the orders being delivered to
len(pd.unique(store.City))
###•	What is the total quantity sold in the East Region?
len(store.query("Region == 'East'").Quantity)
###•	Find the sum of the quantity sold in the East Region
store.query("Region == 'East'").Quantity.sum()
###•	In the south region sort the sales in decreasing order
store[store.Region == "South"].sort_values('Sales',ascending=False)
###•	Find the mean of quantity for every region
store.groupby('Region').Quantity.mean()
###•	Find the mean of sales for every category
store.groupby("Category").Sales.mean()
###•	Find the max, min, sum of sales and profit for every category
store.groupby("Category")["Sales","Profit"].min()
store.groupby("Category")["Sales","Profit"].max()
store.groupby("Category")["Sales","Profit"].sum()
store.groupby("Category")[['Sales','Profit']].agg(['min','max','sum'])
###•	Find sum of sales and max profit for every segment
store.groupby("Segment").Sales.sum()
store.groupby("Segment").Profit.max()
###•	For every segment find the mean of the discount
store.groupby("Segment").Discount.mean()
###•	For every segment find the most profitable customers
def get_cid(pro):
    pro = pro.max()
    return store[store.Profit == pro]['Customer Name']
group_seg = store.groupby('Segment').agg({'Profit': [get_cid,'max']})
print(group_seg)

a=[store.groupby("Segment").max().Profit]
a
b=[store.Profit]
b
store[["Customer Name","Segment"]][np.in1d(b,a)]
###•	What are the top 5 sub-categories that give maximum profit?
store.groupby("Sub-Category").Profit.max().sort_values(ascending=False).head(5)
###•	What is the Total Sales, Quantity, Discount, Profit across Total US.
np.sum(store[["Sales","Quantity","Discount","Profit"]])
store[["Sales","Quantity","Discount","Profit"]].sum()
###•	How many times has it taken more than 5 days from placing an order to shipping
store["Order Date"]=pd.to_datetime(store["Order Date"])
store["Ship Date"]=pd.to_datetime(store["Ship Date"])
d=store["Ship Date"]-store["Order Date"]
sum(d>'5 days')
###•	Find the total number of orders in every category which has been 
###shipped with a duration > 5 days
store["d"]=store["Ship Date"]-store["Order Date"]
store[store.d>'5 days'].groupby("Category")["Order ID"].count()
###•	What’s the percentage of items which has been shipped within 5 days
s=len(store)
s1=len(store[store.d<='5 days'])
s1/s*100
###•	What’s the percentage of items which has been shipped after 5 days
f=len(store)
f1=len(store[store.d>'5 days'])
f1/f*100


