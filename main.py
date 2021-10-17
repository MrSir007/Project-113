import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pgo
import plotly.figure_factory as pff
import statistics
import random
import seaborn as sns
import numpy as np

getData = pd.read_csv("savings_data.csv")
population = getData["quant_saved"].tolist()

scatter = px.scatter(getData, y="quant_saved",color="female")
# scatter.show()

meanPop = statistics.mean(population)
medianPop = statistics.median(population)
modePop = statistics.mode(population)
sdPop = statistics.stdev(population)

def findSample1 (counter) :
  sample1 = []
  for i in range (0,counter) :
    index = random.randint(0,len(population)-1)
    value = population[index]
    sample1.append(value)
  meanFind = statistics.mean(sample1)
  return meanFind

def findSample2 (counter) :
  sample2 = []
  for i in range (0,counter) :
    index = random.randint(0,len(population)-1)
    value = population[index]
    sample2.append(value)
  meanFind = statistics.mean(sample2)
  return meanFind

sampleList1 = []
sampleList2 = []
for i in range (0,100) :
  sample1 = findSample1(100)
  sample2 = findSample2(100)
  sampleList1.append(sample1)
  sampleList2.append(sample2)

meanSampleList1 = statistics.mean(sampleList1)
medianSampleList1 = statistics.median(sampleList1)
modeSampleList1 = statistics.mode(sampleList1)
sdSampleList1 = statistics.stdev(sampleList1)
meanSampleList2 = statistics.mean(sampleList2)
medianSampleList2 = statistics.median(sampleList2)
modeSampleList2 = statistics.mode(sampleList2)
sdSampleList2 = statistics.stdev(sampleList2)

correlation1a = meanPop - meanSampleList1
correlation2a = meanPop - meanSampleList2
correlation3a = meanSampleList1 - meanSampleList2

'''print("The first correlation is", correlation1a)
print("The second correlation is", correlation2a)
print("The third correlation is", correlation3a)'''

q1 = getData["quant_saved"].quantile(0.25)
q3 = getData["quant_saved"].quantile(0.75)
IQR = q3 - q1
lowerwhisker = q1 - 1.5 * IQR
upperwhisker = q3 + 1.5 * IQR

newData = getData[getData["quant_saved"]<upperwhisker]
newPop = newData["quant_saved"].tolist()

meanNew = statistics.mean(newPop)
sdNew = statistics.stdev(newPop)
medianNew = statistics.median(newPop)
modeNew = statistics.mode(newPop)

dis1 = pff.create_distplot([newPop],["Quantity Saved"],show_hist=False)
'''dis1.show()'''

def findSample3 (counter) :
  sample3 = []
  for i in range (0,counter) :
    index = random.randint(0,len(newPop)-1)
    value = newPop[index]
    sample3.append(value)
  meanFind = statistics.mean(sample3)
  return meanFind
sampleList3 = []
for i in range (0,100) :
  sample3 = findSample3(100)
  sampleList3.append(sample3)

meanSampleList3 = statistics.mean(sampleList3)
sdSampleList3 = statistics.stdev(sampleList3)

dis2 = pff.create_distplot([sampleList3],["Quantity Saved"],show_hist=False)
'''dis2.show()'''

correlation1b = newPop - meanSampleList3
correlation2b = meanSampleList1 - meanSampleList3
correlation3b = meanSampleList2 - meanSampleList3

'''print("The first correlation is", correlation1b)
print("The second correlation is", correlation2b)
print("The third correlation is", correlation3b)'''

zscore = (meanSampleList1 - meanSampleList3) / sdSampleList3