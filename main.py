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
    print(config_file_txt[line_index - 1].find('object network'))
  
  line_counter = line_counter + 1
