# -*- coding: utf-8 -*-
"""Diwali Sales Analysis Report

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AhEJQYC3ExXT4-9XbIcdd5DnCnXazm61

**Diwali Sales Analysis Report**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

dataset = '/content/drive/MyDrive/Diwali Sales Data.csv'

dataset = pd.read_csv('/content/drive/MyDrive/Diwali Sales Data.csv', encoding= 'unicode_escape')
# to avoid encoding error, use 'unicode_escape'

dataset.shape
#row and column find

dataset.head(5)

dataset.info()

#drop uncrelated/Bank column
dataset.drop(['Status', 'unnamed1'], axis=1, inplace=True)

dataset.info()

pd.isnull(dataset).sum()

dataset.dropna(inplace=True)

pd.isnull(dataset).sum()

dataset['Amount'].dtypes

#change datatypes
dataset['Amount'] = dataset['Amount'].astype('int')

dataset['Amount'].dtypes

#Use describe() for specific columns
dataset[['Age', 'Orders', 'Amount']].describe()

"""#**Exploratory Data Analysis**

# **Gender**
"""

dataset.columns

ax = sns.countplot(x = 'Gender', data = dataset, palette='Set3')
sns.set(rc={'figure.figsize': (10,5)})
for bars in ax.containers:
  ax.bar_label(bars)

dataset.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

Sales_gen = dataset.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize': (5,3)})
sns.barplot(x = 'Gender', y = 'Amount' , data = Sales_gen)

Sales_gen = dataset.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize': (5,3)})
sns.barplot(x='Gender', y='Amount', data=Sales_gen, palette='Set2')

"""***From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men.***

#**Age**
"""

ax = sns.countplot(data = dataset, x = 'Age Group', hue = 'Gender')
for bars in ax.containers:
  ax.bar_label(bars)

"""***Total Amount vs Age Group***


"""

sales_age = dataset.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by= 'Amount', ascending=False)

sns.barplot(x ='Age Group', y = 'Amount', data = sales_age, palette='Set2')

"""***From above graphs we can see that most of the buyers are of age group between 26-35 yrs female.***

#**State**
"""

dataset.columns

# Total number of orders from top 10 states
sales_state = dataset.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(18,5)})
sns.barplot(data = sales_state, x = 'State' ,y='Orders', palette='Set3')

# Total number of Amount from top 10 states
sales_state = dataset.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize': (18,5)})
sns.barplot(data = sales_state, x = 'State', y='Amount', palette= 'Set2')

"""***From above graphs we can see that most of the orders & total sales/amount are from Utter Pradesh, Maharashtra, Karnataka respectively***

# **Marital Status**
"""

ax = sns.countplot(data = dataset, x = 'Marital_Status', palette= 'Set2')
sns.set(rc={'figure.figsize':(8,5)})
for bars in ax.containers:
  ax.bar_label(bars)

sales_state = dataset.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender', palette= 'Set2')

"""***From above graphs we can see that most of the buyers are married (women) and they have high purchasing power***

# **Occupation**
"""

sns.set(rc={'figure.figsize': (20,5)})
ax = sns.countplot(data = dataset, x = 'Occupation', palette='Set3')

for bars in ax.containers:
  ax.bar_label(bars)

sales_state = dataset.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x = 'Occupation', y = 'Amount', palette='Set1')

"""***From above graphs we can see that most of the buyers are working in IT, Healyhcare and Avistion sector***

# **Product Category**
"""

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = dataset, x = 'Product_Category', palette='Set3')

for bars in ax.containers:
  ax.bar_label(bars)

sales_state = dataset.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x = 'Product_Category', y = 'Amount', palette='Set1')

"""***From Above graphs we can see that most of the sold products are from food, clothing and Electronics category***"""

# Top 10 most sold product (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,5))
dataset.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

"""# **Conclusion**

***Married women age group 26-35 yrs from UP, Maharashtra ans Karnataka working inIT, Heathcare and Aviation are more likely to buy product from Food, Cloting and Electronics category***
"""