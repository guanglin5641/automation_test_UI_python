import openpyxl
from common.path import GetPath
import ast

def case_data(excel_name, sheet_name):
    get_path = GetPath()
    file_path = get_path.get_case_path(excel_name)
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data_list = []
    for i in range(2, sheet.max_row + 1):
        data = {}
        for j in range(1, sheet.max_column + 1):
            data[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        data['操作'] = eval(data['操作'])
        data_list.append(data)
    return data_list

if __name__ == '__main__':
    get_path = GetPath()
    file_path = get_path.get_case_path("brand_case.xlsx")
    print(case_data(file_path, "edit_brand")[0]["操作"])
    a = [
        {
            '测试模块': '供应商管理',
            '测试功能': '添加供应商',
            '前置条件': '进入添加供应商页面',
            '测试标题': '编辑供应商供应商名称为空',
            '操作': {'name': '', 'type': '1688', 'resource_type': ['CPS', 'CPA'], 'balance_warning': '', 'account': '',
                     'password': '', 'company_info': {'company': '', 'contact': '', 'contact_content': ''},
                     'status': '',
                     'remark': ''},
            '预期结果': '请输入供应商名称'
        },
        {
            '测试模块': '供应商管理',
            '测试功能': '添加供应商',
            '前置条件': '进入添加供应商页面',
            '测试标题': '编辑供应商供应商名称为空',
            '操作': {'name': '', 'type': '1688', 'resource_type': ['CPS', 'CPA'], 'balance_warning': '', 'account': '',
                     'password': '', 'company_info': {'company': '', 'contact': '', 'contact_content': ''},
                     'status': '',
                     'remark': ''},
            '预期结果': '请输入供应商名称'
        }
    ]
