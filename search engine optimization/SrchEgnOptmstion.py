def webpageparser():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    a=input('enter the url with out http: ')
    url = 'http://'+a
    file_handle = urlopen(url)
    soup = BeautifulSoup(file_handle,'html.parser')
    for script in soup(['script','style']):
        script.extract()

    text=soup.get_text()
#    print(text)




    from pyexcel_xls import save_data
    import xlsxwriter

    wor=['hari','haran']
    count=[2,4]
    
    workbook=xlsxwriter.Workbook('sam.xlsx')                  
    worksheet=workbook.add_worksheet(a)
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'Words', bold)
    worksheet.write('B1', 'Count', bold)
    # Start from the first cell. Rows and columns are zero indexed.                                                
    row=1
    col=0
    # Iterate over the data and write it out row by row.
    for i in range(2):                                       
        worksheet.write(row,col,wor[i])
        worksheet.write_number(row,col+1, count[i])
        row+=1
    chart=workbook.add_chart({'type':'bar'})                   # Create a new Chart object.
    chart.add_series({'categories':'='+a+'!$A$2:$A$6','values':'='+a+'!$B$2:$B$6'})   # Configure the chart. In simplest case we add one or more data series.
    worksheet.insert_chart('D2',chart)
    chart=workbook.add_chart({'type':'pie'})                   # Create a new Chart object.
    chart.add_series({'categories':'='+a+'!$A$2:$A$6','values':'='+a+'!$B$2:$B$6'})   # Configure the chart. In simplest case we add one or more data series.
    worksheet.insert_chart('D20',chart)
    chart=workbook.add_chart({'type':'column'})                   # Create a new Chart object.
    chart.add_series({'categories':'='+a+'!$A$2:$A$6','values':'='+a+'!$B$2:$B$6'})   # Configure the chart. In simplest case we add one or more data series.
    worksheet.insert_chart('L2',chart)

    import os
    file = r"C:\Users\admin\Desktop\SathyaM\search engine optimization\sam.xlsx"
    os.startfile(file)


webpageparser()     
    
