#websracping
def chart(wor,count,a,workbook):
  try:  
                
    worksheet=workbook.add_worksheet(a)
    worksheet.write('A1', 'Words')
    worksheet.write('B1', 'Count')
                                                      # Start from the first cell. Rows and columns are zero indexed.
    row=1
    col=0
    for i in range(5):                                       # Iterate over the data and write it out row by row.
        worksheet.write(row,col,wor[i])
        worksheet.write_number(row,col+1, count[i])
        row+=1

    
    chart=workbook.add_chart({'type':'bar'})# Create a new Chart object.
    value={'categories':'='+a+'!$A$2:$A$6','values':'='+a+'!$B$2:$B$6'}
    chart.add_series(value)   # Configure the chart. In simplest case we add one or more data series.
    worksheet.insert_chart('D2',chart)
    print('-------------------------------------------------------------------------')
    print(' ***********************Thank you for using SEO TOOL ********************')
    print(' ******************** find the chart in Program folder ******************')
    print('-------------------------------------------------------------------------')
  except Exception as n:print(n)
      
      

def project(workbook):
 try:
    a=input('enter your url')
    url='http://'+a
    value=BeautifulSoup(urlopen(url),'html.parser')
    for script in value(["script","style"]):
        script.extract()
    text=value.get_text().strip()
    text=text.split('\n')
    text=' '.join(text)
    te=text.split(' ')
    fil=open('nege.txt','r').read()
    fe=fil.split(' ')
    k=[' ','']
    ori=[]
    for f in te:
        if f not in k:
         if f not in fe:
          ori.append(f)
    ge=[]
    oe={}
    for ef in ori:
        if ef not in ge:
            ge.append(ef)
            count=ori.count(ef)
            oe[ef]=count
    sort=sorted(oe.items(),key=lambda t:t[1],reverse=True)
    wor=[]
    count=[]
    v=sort[0:5]
    xy=0
    print('******************The top 5 key words Used in the website****************')
    print('-------------------------------------------------------------------------')
    print(v)
    print('-------------------------------------------------------------------------')
    for r in range(5):
        for y in range(1):
            wor.append(v[r][y])
            count.append(v[r][y+1])
    chart(wor,count,a,workbook)
 except Exception as n:print(n)





print('********************************SEO*************************************')
print('------------------------------------------------------------------------')
try:
 from urllib.request import urlopen
 from bs4 import BeautifulSoup
 import json
 import re
 import itertools
 import xlsxwriter
 workbook=xlsxwriter.Workbook("Data.xlsx")     
 while(1):
    project(workbook)
    con=input('Do you want to Search again yes,no:')
    print('---------------------------------------')
    if(con=='yes' or con=='YES'):
        continue
    elif(con=='no'or con=='NO'):
        print('Thank you Happy Searching !!! ')
        break
    else:
        print('wrong Entry')
        continue
except Exception as n:
    print(n, 'check and run again')
    
