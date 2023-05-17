#Auto:达实泽林
#Creat Time:2021/12/23 16:50
#Creat Function:
#Edit Auto:
#Edit Time:
#Edit Function:
from base.box import ExcelHelper

data = ExcelHelper().get_excel_data('add_user_data.xlsx','user_page')
print(data)