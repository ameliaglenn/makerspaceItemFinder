import pandas as pd
inventory=pd.read_excel(r'C:\Users\ameli\Downloads\Alexa Skills Inventory.xlsx')
location=pd.DataFrame(inventory, columns=['Item Name','Location in G34'])
synonyms=pd.DataFrame(inventory, columns=['Alternative Names','Item Name'])
