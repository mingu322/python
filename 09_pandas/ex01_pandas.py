import pandas as pd

# 시리즈 선언
Series1 = pd.Series([2, 4, 6, 8, 10])
print(Series1)

# index를 지정
Series2 = pd.Series([2, 4, 6, 8, 10], index=[1,2,3,4,5])
print(Series2)

#range로 index 지정
Serie3 = pd.Series([2,4,6,8,10], index=range(1,6))
print(Serie3)

#index용 리스트
index_value = [10,11,12,13,14]
series4 = pd.Series([2,4,6,8,10], index=index_value)

# 데이터, index를 따로 선언 후 활용 
data_value = [1,34,45,6,324]
index__value = [10,11,12,13,14]
series5 = pd.Series(data_value, index=index__value)
print(series5)