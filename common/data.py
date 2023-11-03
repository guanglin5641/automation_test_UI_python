import openpyxl
from common.path import GetPath
import ast

def case_data(excel_name, sheet_name):
    get_path = GetPath()
    file_path = get_path.get_case_path(excel_name)
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    row = sum(1 for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row) if any(cell.data_type == 's' and cell.value for cell in row))
    column = sum(1 for column in sheet.iter_cols(min_col=1, max_col=sheet.max_column) if any(cell.data_type == 's' and cell.value for cell in column))
    data_list = []
    for i in range(2, row + 1):
        data = {}
        for j in range(1, column + 1):
            data[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        data['操作'] = eval(data['操作'])
        data_list.append(data)
    return data_list

if __name__ == '__main__':
    get_path = GetPath()
    file_path = get_path.get_case_path("brand_case.xlsx")
    a = (case_data(file_path, "add_brand")[0]["操作"])
    # print(a)
