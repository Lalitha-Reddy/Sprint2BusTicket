from Library.config import Config
import xlrd
# path = r"C:\Users\Lalitha\OneDrive\Desktop\mongi.xlsx"


def read_locators():
    workbook = xlrd.open_workbook(Config.Data_path)
    worksheet = workbook.sheet_by_name('busbooking')
    rows = worksheet.nrows
    d = {}
    for i in range(1, rows):
        row = worksheet.row_values(i)
        print(row)
        d[row[0]] = (row[1], row[2])
    return d


# class ReadExcel:
#     def read_test_data(self,sheetname):
#         workbook = xlrd.open_workbook(Config.Data_path)
#         worksheet = workbook.sheet_by_name(sheetname)
#         columns = worksheet.ncols
#         print(columns)
#         rows = worksheet.get_rows()
#         header=next(rows)
#         data = []
#         for row in rows:
#             values = ()
#             for j in range(columns):
#                 values += (row[j].value,)
#             data.append(values)
#         return data
#     def read_locators(self,sheetname):
#         workbook = xlrd.open_workbook(Config.Data_path)
#         worksheet = workbook.sheet_by_name(sheetname)
#         rows = worksheet.get_rows()
#         header = next(rows)
#         d = {}
#
#         for row in rows:
#             d[row[0].value] = (row[1].value,row[2].value)
#         return d


def read_locators():
    workbook = xlrd.open_workbook(Config.Data_path)
    worksheet = workbook.sheet_by_name('busbooking')
    rows = worksheet.nrows
    d = {}
    for i in range(1, rows):
        row = worksheet.row_values(i)
        print(row)
        d[row[0]] = (row[1], row[2])
    return d
#

