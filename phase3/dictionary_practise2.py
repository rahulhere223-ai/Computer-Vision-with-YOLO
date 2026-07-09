objects = [
    "car",
    "person",
    "car",
    "truck",
    "car",
    "person",
    "bus",
    "bus",
    "car"
]
count_obj={}

for obj in objects:
    
    if obj in count_obj:
        count_obj[obj]+=1
    else:
        count_obj[obj] =1

print(count_obj)