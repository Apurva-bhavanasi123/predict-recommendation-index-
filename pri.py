# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:40:36 2019

@author: Apoorva
"""
import pandas as pd
userItemData = pd.read_csv('ratings.csv')#data downloaded through web
userItemData.head()#display initial row 
itemList=list(set(userItemData["ItemId"].tolist()))
#get unique item  count 
userCount=len(set(userItemData["userId"].tolist()))
#get user count
#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount=0

#For each item in the list, compare with other items.
for i in range(len(itemList)):
    
    item1Users = userItemData[userItemData.ItemId==itemList[i]]["userId"].tolist()
    
    for ind2 in range(i, len(itemList)):
        
        if ( i == ind2):
            continue
       
        #Get list of users who bought item 2
        item2Users=userItemData[userItemData.ItemId==itemList[ind2]]["userId"].tolist()
        #print("Item 2",item2Users)
        
        #Find score. Find the common list of users and divide it by the total users.
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=commonUsers / userCount

        #Add a score for item 1, item 2
        itemAffinity.loc[rowCount] = [itemList[i],itemList[ind2],score]
        rowCount +=1
        #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
        itemAffinity.loc[rowCount] = [itemList[ind2],itemList[i],score]
        rowCount +=1
        
#Check final result
itemAffinity.head()
for i in itemList:
    searchItem=i
    recoList=itemAffinity[itemAffinity.item1==searchItem]\[["item2","score"]]\.sort_values("score", ascending=[0])
        
    print("Recommendations for item",i, recoList,sep=' ')
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure
    plt.rc('figure', figsize=(10, 5))
    plt.ylim(0,1)
    plt.plot(recoList)
    plt.ylabel("Affinity scores")
    plt.show()
    
