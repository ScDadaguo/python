import pandas as pd
a = [1,2,3]
b = [4,5,6]
dataframe = pd.DataFrame({'a_name':a,'b_name':b})
dataframe.to_csv("test.csv",index=False,sep=',')