import pandas

#https://www.kaggle.com/noriuk/us-education-datasets-unification-project

data=pandas.read_csv('edu.csv')
import timeit

#iloc vs iterrows
#iloc: each row is stored as series
%%timeit
profit_per_state=[]
for i,row in data.iterrows():
    profit=row['TOTAL_REVENUE']-row['TOTAL_EXPENDITURE']
    profit_per_state.append(profit)
print (profit_per_state)

#iterrows vs itertuples
#itertuples: each row is represented as a namedtuple
%%timeit
profit_per_state=[]
for row in data.itertuples():
    index=row.Index
    profit=row.TOTAL_REVENUE-row.TOTAL_EXPENDITURE
    profit_per_state.append(profit)
print (profit_per_state)

#apply() vs itertuples
#always best to avoid looping
%%timeit
profits=data.apply(
                    lambda row: row['TOTAL_REVENUE']-row['TOTAL_EXPENDITURE'],
                    axis=1
                    )
data['profit']=profits

#numpy arrays vs .apply
#numpy arrays are orders of magnitude more efficient
#use series.array to vectorize
%%timeit
profits=data['TOTAL_REVENUE'].values-data['TOTAL_EXPENDITURE'].values
data['profit']=profits