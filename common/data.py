import openpyxl
from common.path import GetPath

def case_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data_list = []
    for i in range(2, sheet.max_row + 1):
        data_list.append({})
        for j in range(1, sheet.max_column + 1):
            data_list[i - 2][sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
    return data_list

if __name__ == '__main__':
    get_path = GetPath()
    file_path = get_path.get_case_path("brand_case.xlsx")
    print(case_data(file_path, "edit_brand")[0]["操作"])
