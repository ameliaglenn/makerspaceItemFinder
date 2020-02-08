import pandas as pd
inventory=pd.read_excel(r'C:\Users\ameli\Documents\GitHub\notJarvis\Alexa Skills Inventory.xlsx')
location=pd.DataFrame(inventory, columns=['Item Name','Location in G34'])
synonyms=pd.DataFrame(inventory, columns=['Alternative Names'])
#items=pd.DataFrame(inventory, columns=['Item Name'])
location.to_dict()
print(type(location))
print(location)
#print(location['0'])
