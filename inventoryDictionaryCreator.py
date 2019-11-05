inventory={}
workbook=xlrd.open_workbook('makerspaceInventory.xlsx')
sh=workbook.sheet_by_index(0)
lastRow=0
while True:
    if sh.cell(lastRow,0).value is not None:
        lastRow+=1
    else:
        break
for i in range(lastRow):
    cell_value_class=sh.cell(i,0).value
    cell_value_id=sh.cell(i,1).value
    d[cell_value_class]=cell_value_id
    print(cell_value_class,'=',d[cell_value_class])
