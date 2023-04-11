
import csv
import pandas as pd
import numpy as np
csvFile=pd.read_csv("some.csv")
#s1=csvFile.max(axis=0)
print(type(csvFile))

def Running_hours(value):
    if(value=="prod"):
        return 720
    elif (value=="dev" or value=="preprod" or value=="stage"):
        return 308
    


csvFile['Running_hours']=csvFile['ENV'].map(Running_hours)
print(csvFile)
# d1=s1.reset_index()
# #print(d1)
# # #print(type(dcsv1))
# d1 = d1.rename(columns={0:'MAX_MEM','index':'INSTANCE_NAME'})
# d1 = d1.iloc[1:]
# #print(d1)


# s2=csvFile.min(axis=0)
# #print(s1)
# d2=s2.reset_index()
# #print(d1)
# # #print(type(d1))
# d2 = d2.rename(columns={0:'MIN_MEM','index':'INSTANCE_NAME'})
# d2 = d2.iloc[1:]
# #print(d2)


# s3=csvFile.mean(axis=0)
# #print(s1)
# d3=s3.reset_index()
# #print(d1)
# # #print(type(d1))
# d3 = d3.rename(columns={0:'AVG_MEM','index':'INSTANCE_NAME'})
# #print(d3)

# # s2=csvFile.min(axis=0)
# # d2=s2.reset_index()
# # #print(type(d1))
# # d2 = d2.rename(columns={0:'MIN','index':'instance_name'})
# # d2 = d2.iloc[1:]

# # #print(d2)

# d1=d1.merge(d2)

# # s3=csvFile.mean(axis=0);
# # d3=s3.reset_index()
# # #print(type(d1))
# # d3 = d3.rename(columns={0:'AVG','index':'instance_name'})

# #print(d3)

# d1 = d1.merge(d3)
# print(d1)

csvFile.to_csv('AllComputeActual.csv',index = False)