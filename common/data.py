import openpyxl
from common.path import GetPath
import json


def case_data(excel_name , sheet_name) :
	get_path = GetPath()
	file_path = get_path.get_case_path(excel_name)
	workbook = openpyxl.load_workbook(file_path)
	sheet = workbook[sheet_name]
	
	headers = [cell.value for cell in sheet[1]]
	data = []
	for row in sheet.iter_rows(min_row=2 , values_only=True) :
		if row[0] is None or row[0] == "" :
			continue
		row_dict = { headers[i] : row[i] for i in range(len(headers)) }
		for key , value in row_dict.items() :
			try :
				row_dict[key] = json.loads(value)
			except (TypeError , ValueError) :
				row_dict[key] = value
		data.append(row_dict)
	return data


if __name__ == '__main__' :
	act_cases = case_data("crm_activity.xlsx" , "delete")
	for act_case in act_cases :
		print(act_case['前置条件'] , type(act_case['前置条件']))