#This will be for getting our data
import pandas as pd
import matplotlib.pyplot as plt
# The following was copied from the uciml docs: https://archive.ics.uci.edu/dataset/94/spambase
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
spambase = fetch_ucirepo(id=94) 
  
# data (as pandas dataframes) 
x = spambase.data.features 
y = spambase.data.targets 
  
# metadata 
#print(spambase.metadata) 
  
# variable information 
#print(spambase.variables)


#For "getting started" section of project:
df = pd.concat([x, y], axis=1)

#Plot 1
plt.scatter(df["word_freq_your"], df["word_freq_internet"], c=df["Class"])
plt.colorbar(ticks=[0, 1]) 
plt.xlabel("Word count of word: your")
plt.ylabel("Word count of word: internet")
plt.savefig("data/plot1.png")
#Plot 2
plt.scatter(df["word_freq_original"], df["word_freq_re"], c=df["Class"])
plt.xlabel("Word count of word: original")
plt.ylabel("Word count of word: re")
plt.savefig("data/plot2.png")
#PLot 3:
plt.scatter(df["word_freq_technology"], df["word_freq_money"], c=df["Class"])
plt.xlabel("Word count of word: technology")
plt.ylabel("Word count of word: money")
plt.savefig("data/plot3.png")


