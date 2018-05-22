import xlsxwriter
workbook = xlsxwriter.Workbook('d:\\test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Test data')

workbook.close()
