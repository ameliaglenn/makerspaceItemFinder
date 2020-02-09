import pandas as pd
inventory=pd.read_excel(r'C:\Users\ameli\Documents\GitHub\notJarvis\Alexa Skills Inventory.xlsx')
location=pd.DataFrame(inventory, columns=['Item Name','Location in G34'])
synonyms=pd.DataFrame(inventory, columns=['Alternative Names'])
totalRows=len(inventory.axes[0])
l=location.to_dict(orient='list')
s=synonyms.values.tolist()
print(s[0])
loc={}
syn={}
for i in range(totalRows):
    specificSyn=''.join(s[i])
    synonymList=specificSyn.split(', ')
    totSyn=len(synonymList)
    print(synonymList)
    print(totSyn)
    loc[l['Item Name'][i]]=l['Location in G34'][i]
    for k in range(totSyn):
        syn[synonymList[k]]=l['Item Name'][i]
