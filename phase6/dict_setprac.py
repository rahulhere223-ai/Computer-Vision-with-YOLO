vehicle_count={
    "cars":set(),
    "truck":set(),
    "bus":set()
}

vehicle_count["cars"].add(17)
vehicle_count["cars"].add(27)
vehicle_count["cars"].add(17)
vehicle_count["bus"].add(17)
vehicle_count["bus"].add(18)

print(len(vehicle_count["cars"]))
