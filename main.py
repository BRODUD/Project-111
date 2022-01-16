from random import randint
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics as ss
import random
import plotly.graph_objects as go

df = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 111\medium_data.csv')
data = df['claps'].tolist()
fig = ff.create_distplot([data],["claps"],show_hist=False)



mean = ss.mean(data)
std_deviation = ss.stdev(data)
print("Mean of sampling distribution: ", mean)
print("Standard Deviation of sampling distribution: ", std_deviation)



def random_set_of_mean(counter):
    dataset =[]
    for i in range(0,counter):
        random_index= random.randint(0,6507)
        value = data[random_index]
        dataset.append(value)

    mean_sample = ss.mean(dataset)
    return mean_sample

mean_list=[]
for i in range(0,1000):
   set_of_means = random_set_of_mean(100)
   mean_list.append(set_of_means)

## calculating mean and standard_deviation of the sampling distribution.
std_deviation = ss.stdev(mean_list)
mean = ss.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)
   
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)


# finding the mean of the first group(Students with Ipad) and plot it on the existing sampling distribution plot
df_data1 = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 111\medium_data.csv')
data1 = df_data1['claps'].tolist()
mean_sample1 = ss.mean(data1)
print("Mean of Sample 1 : ",mean_sample1)


 # finding the mean of the second group(2 extra hours of daily classes) and plot it on the existing sampling distribution plot
df_data2 = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 111\medium_data.csv')
data2 = df_data2['claps'].tolist()
mean_sample2 = ss.mean(data2)
print("Mean of Sample 2 : ",mean_sample2)


 # finding the mean of the third group(fun math worksheets) and plot it on the existing sampling distribution plot
df_data3 = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 111\medium_data.csv')
data3 = df_data3['claps'].tolist()
mean_sample3 = ss.mean(data3)
print("Mean of Sample 3 : ",mean_sample3)


# #plotting the mean of the sampling
fig = ff.create_distplot([mean_list], ["claps"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[mean_sample3, mean_sample3], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE 3"))

fig.show()

#finding the z score using the formula
z_score = (mean - mean_sample3)/std_deviation
print("The z score is = ",z_score)

# z score - (New Sample Mean - Sampling Distribution Mean) / standard deviation 
