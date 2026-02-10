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

plt.plot(df["word_freq_telnet"], df["word_freq_mail"])
plt.savefig("data/plot1.png")


