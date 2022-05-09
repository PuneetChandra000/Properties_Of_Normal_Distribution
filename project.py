import pandas as pd
import statistics as st
import plotly.figure_factory as pf

# -----------------------------------------------------------------------------------

data = pd.read_csv("project.csv")

reading_Score = data["reading score"].tolist()

mean = st.mean(reading_Score)
median = st.median(reading_Score)
mode = st.mode(reading_Score)
stdev = st.stdev(reading_Score)

print("--------------------------------------------------------------------------------------------")

print("Mean of data : " , mean)
print("Median of data : " , median)
print("Mode of data  : " , mode)
print("Standard Deviation of data  : " , stdev)

print("----------------------------------------------------------------------------------------")

graph = pf.create_distplot([reading_Score], ["reading_Score"], show_hist = False)

# graph.show()

# ----------------------------------------------------------------------------------------

firstStdevStart , firstStdevEnd = (mean - stdev) , (mean + stdev)

secondStdevStart , secondStdevEnd = (mean - (2 * stdev)) , (mean + (2 * stdev))

thirdStdevStart , thirdStdevEnd = (mean - (3 * stdev)) , (mean + (3 * stdev))

# -----------------------------------------------------------------------------------------------------------------------

list_Of_Stdev_Within_1 = [i for i in reading_Score if i > firstStdevStart and i < firstStdevEnd]

list_Of_Stdev_Within_2 = [i for i in reading_Score if i > secondStdevStart and i < secondStdevEnd]

list_Of_Stdev_Within_3 = [i for i in reading_Score if i > thirdStdevStart and i < thirdStdevEnd]

#-------------------------------------------------------------------------------------------------

total_reading_Score = len(reading_Score)

total_1 = len(list_Of_Stdev_Within_1)

p1 = (total_1 * 100) / total_reading_Score

total_2 = len(list_Of_Stdev_Within_2)

p2 = (total_2 * 100) / total_reading_Score

total_3 = len(list_Of_Stdev_Within_3)

p3 = (total_3 * 100) / total_reading_Score

#----------------------------------------------------------------------------------------------

print("Percentage lying within stdev 1 : " , p1)

print("Percentage lying within stdev 2 : " , p2)

print("Percentage lying within stdev 3 : " , p3)
