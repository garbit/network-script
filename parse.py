input_string = """
object-group network TEST-GROUP1
 network-object object SERVER1
 network-object object SERVER2
 network-object object SERVER3
 network-object object SERVER4
"""

lines = input_string.splitlines()
object_groups = {}

servers = {}

current_group = ''

for i in lines:
  line = i.split(' ')
  object_group_name = line[-1]
  item = line[0]
  
  if len(line) > 1:
      if item == 'object-group':
        if object_group_name not in object_groups:
          object_groups[object_group_name] = []
          current_group = object_group_name
      else:
        server_name = line[-1]      
        object_groups[current_group].append(server_name)
        if server_name not in servers:
            servers[server_name] = []
        
        servers[server_name].append(current_group)
        

print(object_groups)
print(servers)

  