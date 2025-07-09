#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

#Defining a function to perform a z-test
def ZTest(a, b):
    #Calculating the z-score
    z_score = ((a.mean() - b.mean()) - 0) / np.sqrt(((a.std())**2 / len(a)) + ((b.std())**2 / len(b)))
    #Outputting the z-score and p-value
    print("Z-Score:", z_score)
    print("P-value:",1-stats.norm.cdf(z_score))

#Reading in average queue time data and maximum queue time data
AverageQueueData = pd.read_csv("https://docs.google.com/spreadsheets/d/1Bd9XJM_8LDhWSUePkIjbKMBtPtvoW8DLv80apQvsQtk/export?format=csv&gid=0")
MaxQueueData = pd.read_csv("https://docs.google.com/spreadsheets/d/1Bd9XJM_8LDhWSUePkIjbKMBtPtvoW8DLv80apQvsQtk/export?format=csv&gid=1798807588")

#Showing the number of parks in each dataset by country
AverageQueuesNumberOfParksCountry = AverageQueueData[AverageQueueData["Continent"] == "Europe"].groupby(by="Country")["Park"].agg([pd.unique]).agg([len])
print(AverageQueuesNumberOfParksCountry)

MaxQueuesNumberOfParksCountry = MaxQueueData[MaxQueueData["Continent"] == "Europe"].groupby(by="Country")["Park"].agg([pd.unique]).agg([len])
print(MaxQueuesNumberOfParksCountry)

#Showing the average queue time in each dataset by country
AverageQueuesAggregatedCountry = AverageQueueData[AverageQueueData["Continent"] == "Europe"].groupby(by="Country")["Queue Time"].agg([len, "mean", "median"])
print(AverageQueuesAggregatedCountry)

MaxQueuesAggregatedCountry = MaxQueueData[MaxQueueData["Continent"] == "Europe"].groupby(by="Country")["Queue Time"].agg([len, "mean", "median"])
print(MaxQueuesAggregatedCountry)

#Showing the number of parks in each dataset by operator
AverageQueuesNumberOfParksOperator = AverageQueueData[AverageQueueData["Continent"] == "Europe"].groupby(by="Operator")["Park"].agg([pd.unique]).agg([len])
print(AverageQueuesNumberOfParksOperator)

MaxQueuesNumberOfParksOperator = MaxQueueData[MaxQueueData["Continent"] == "Europe"].groupby(by="Operator")["Park"].agg([pd.unique]).agg([len])
print(MaxQueuesNumberOfParksOperator)

#Showing the average queue time in each dataset by operator
AverageQueuesAggregatedOperator = AverageQueueData[AverageQueueData["Continent"] == "Europe"].groupby(by="Operator")["Queue Time"].agg([len, "mean", "median"])
print(AverageQueuesAggregatedOperator)

MaxQueuesAggregatedOperator = MaxQueueData[MaxQueueData["Continent"] == "Europe"].groupby(by="Operator")["Queue Time"].agg([len, "mean", "median"])
print(MaxQueuesAggregatedOperator)

#Showing a boxplot of average queue times by country
sns.boxplot(x="Country", y="Queue Time", data=AverageQueueData[AverageQueueData["Continent"] == "Europe"]).set(title="Average queue times by country")
plt.show()

#Showing a boxplot of average maximum queue times by country
sns.boxplot(x="Country", y="Queue Time", data=MaxQueueData[MaxQueueData["Continent"] == "Europe"]).set(title="Average maximum queue times by country")
plt.show()

#Showing a boxplot of average queue times by operator
sns.boxplot(x="Operator", y="Queue Time", data=AverageQueueData[AverageQueueData["Continent"] == "Europe"]).set(title="Average queue times by operator")
plt.show()

#Showing a boxplot of average maximum queue times by operator
sns.boxplot(x="Operator", y="Queue Time", data=MaxQueueData[MaxQueueData["Continent"] == "Europe"]).set(title="Average maximum queue times by operator")
plt.show()

#Splitting the datasets into UK and European subsets
UKAverageQueues = AverageQueueData[AverageQueueData["Country"] == "United Kingdom"]
EuropeAverageQueues = AverageQueueData[(AverageQueueData["Continent"] == "Europe") & (AverageQueueData["Country"] != "United Kingdom")]

UKMaxQueues = MaxQueueData[MaxQueueData["Country"] == "United Kingdom"]
EuropeMaxQueues = MaxQueueData[(MaxQueueData["Continent"] == "Europe") & (MaxQueueData["Country"] != "United Kingdom")]

#Splitting the datasets into Merlin and non-Merlin subsets
MerlinAverageQueues = AverageQueueData[(AverageQueueData["Continent"] == "Europe") & (AverageQueueData["Operator"] == "Merlin")]
NonMerlinAverageQueues = AverageQueueData[(AverageQueueData["Continent"] == "Europe") & (AverageQueueData["Operator"] != "Merlin")]

MerlinMaxQueues = MaxQueueData[(MaxQueueData["Continent"] == "Europe") & (MaxQueueData["Operator"] == "Merlin")]
NonMerlinMaxQueues = MaxQueueData[(MaxQueueData["Continent"] == "Europe") & (MaxQueueData["Operator"] != "Merlin")]

#Displaying mean queue times for the UK and European subsets of each dataset
print(UKAverageQueues)
print(EuropeAverageQueues)
print(UKAverageQueues["Queue Time"].mean())
print(EuropeAverageQueues["Queue Time"].mean())
print(UKMaxQueues["Queue Time"].mean())
print(EuropeMaxQueues["Queue Time"].mean())

#Displaying mean queue times for the Merlin and non-Merlin subsets of each dataset
print(MerlinAverageQueues)
print(NonMerlinAverageQueues)
print(MerlinAverageQueues["Queue Time"].mean())
print(NonMerlinAverageQueues["Queue Time"].mean())
print(MerlinMaxQueues["Queue Time"].mean())
print(NonMerlinMaxQueues["Queue Time"].mean())

#Performing four z-tests to determine whether UK queue times are longer than those in the rest of Europe on average, as well as whether Merlin queue times are longer than non-Merlin queue times on average
ZTest(UKAverageQueues["Queue Time"], EuropeAverageQueues["Queue Time"])
ZTest(UKMaxQueues["Queue Time"], EuropeMaxQueues["Queue Time"])
ZTest(MerlinAverageQueues["Queue Time"], NonMerlinAverageQueues["Queue Time"])
ZTest(MerlinMaxQueues["Queue Time"], NonMerlinMaxQueues["Queue Time"])
