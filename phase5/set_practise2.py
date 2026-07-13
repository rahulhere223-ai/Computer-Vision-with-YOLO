unique_id=set()

unique_id.add(17)
unique_id.add(22)
unique_id.add(17)
unique_id.add(31)
unique_id.add(22)
unique_id.add(45)

print("unique_id",unique_id)
print("Total unique_id",len(unique_id))

print(17 in unique_id)
print(100 in unique_id)