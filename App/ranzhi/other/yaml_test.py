#Auto:达实泽林
#Creat Time:2021/12/23 10:43
#Creat Function:
#Edit Auto:
#Edit Time:
#Edit Function:
from base.box import YamlHelper

yaml_data = YamlHelper().get_yaml_data('page.yaml')
print(yaml_data['Person']['name'])