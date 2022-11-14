input_string = """
object-group network TEST-GROUP1
 network-object object SERVER1
 network-object object SERVER2
 network-object object SERVER3
 network-object object SERVER4
"""

lines = input_string.splitlines()

object_groups = {}

for i in lines:
  line = i.split(' ')
  object_group_name = line[-1]
  item = line[0]

  if item == 'object-group':
    if object_group_name not in object_groups.keys():
      object_groups[object_group_name] = []
  else:
    object_groups[object_group_name].append(object_group_name)

print(object_groups)

  