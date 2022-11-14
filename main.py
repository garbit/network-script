from pathlib import Path

public_ip = input()
print('... searching for public object')

print('Config file path')
config_file = input()

config_file_txt = Path(config_file).open("r").readlines()

line_counter = 0

for line in config_file_txt:
  line_index = line.find(public_ip)
  if line_index != -1:
    line_to_search = config_file_txt[line_index - 1]
    object_name = line_to_search[line_to_search.find('object network'):-1].split(' ')[2]
    
  
  line_counter = line_counter + 1
