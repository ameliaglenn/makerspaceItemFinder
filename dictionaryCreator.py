import pandas as pd
#pulls in the excell sheet, separates out the location and synonym dictionary bases
inventory=pd.read_excel(r'C:\Users\ameli\Documents\GitHub\notJarvis\Alexa Skills Inventory.xlsx')
location=pd.DataFrame(inventory, columns=['Item Name','Location in G34'])
synonyms=pd.DataFrame(inventory, columns=['Alternative Names'])
totalRows=len(inventory.axes[0])
l=location.to_dict(orient='list')
s=synonyms.values.tolist()
#creates location and synonym dictionaries
loc={}
syn={}
for i in range(totalRows):
    #converts the single-string "list" of synonyms to an actual list
    specificSyn=''.join(s[i])
    synonymList=specificSyn.split(', ')
    totSyn=len(synonymList)
    #fills loc and syn dicts in lowercase
    loc[l['Item Name'][i].lower()]=l['Location in G34'][i]
    for k in range(totSyn):
        syn[synonymList[k].lower()]=l['Item Name'][i].lower()
    
print(syn)
print(loc)
