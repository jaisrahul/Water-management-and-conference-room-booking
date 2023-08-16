class WaterManagement:
    def __init__(self):
        self.corporation_rate = 1.0
        self.borewell_rate = 1.5
        self.tanker_slabs = [(0, 500, 2), (501, 1500, 3), (1501, 3000, 5), (3001, float('inf'), 8)]
        self.apartment_data = {}
        self.total_guests = 0

    # Allot water ratio to a given apartment type
    def allot_water(self, apartment_type, ratio):
        self.apartment_data[apartment_type] = ratio

    # Add guests to the total guest count
    def add_guests(self, guests):
        self.total_guests += guests

    # Calculate the total water consumption and cost for the month
    def calculate_bill(self):
        total_water_allotted, corporation_ratio, borewell_ratio = self.calculate_water_allotment()
        corporation_consumption, borewell_consumption = self.split_water(total_water_allotted, corporation_ratio, borewell_ratio)
        tanker_consumption = max(0, total_water_allotted - (corporation_consumption + borewell_consumption))

        corporation_cost = corporation_consumption * self.corporation_rate
        borewell_cost = borewell_consumption * self.borewell_rate
        tanker_cost = self.calculate_tanker_cost(tanker_consumption)
        
        total_cost = corporation_cost + borewell_cost + tanker_cost
        total_water_consumed = total_water_allotted + tanker_consumption
        
        return total_water_consumed, int(total_cost)

    # Calculate total water allotted based on apartment type and guests
    def calculate_water_allotment(self):
        apartment_type, ratio = self.apartment_data.popitem()
        corporation_ratio, borewell_ratio = ratio
        base_allotment = 900 if apartment_type == 2 else 1500
        total_water_allotted = base_allotment + (self.total_guests * 10 * 30)
        return total_water_allotted, corporation_ratio, borewell_ratio

    # Split total water into corporation and borewell based on ratios
    def split_water(self, total_water, corporation_ratio, borewell_ratio):
        total_ratio = corporation_ratio + borewell_ratio
        corporation_consumption = total_water * (corporation_ratio / total_ratio)
        borewell_consumption = total_water * (borewell_ratio / total_ratio)
        return corporation_consumption, borewell_consumption

    # Calculate cost of tanker water consumption using slab rates
    def calculate_tanker_cost(self, consumption):
        cost = 0
        for slab in self.tanker_slabs:
            lower, upper, rate = slab
            if consumption <= lower:
                break
            slab_consumption = min(consumption, upper) - lower
            cost += slab_consumption * rate
        return cost
    
# This is main function for output
def main():
    water_manager = WaterManagement()
    while True:
        command = input().split()
        action = command[0]
        if action == "ALLOT_WATER":
            apartment_type = int(command[1])
            ratio = tuple(map(int, command[2].split(':')))
            water_manager.allot_water(apartment_type, ratio)
        elif action == "ADD_GUESTS":
            guests = int(command[1])
            water_manager.add_guests(guests)
        elif action == "BILL":
            total_water, total_cost = water_manager.calculate_bill()
            print(f"{total_water} {total_cost}")
            break
        else:
            print("Invalid command")
if __name__ == "__main__":
    main()









# def main():
#     water_manager = WaterManagement()
#     apartment_data = {}
#     input_commands = [
#         "ALLOT_WATER 3 2:1",
#         "ADD_GUESTS 4",
#         "ADD_GUESTS 1",
#         "BILL"
#     ]

#     for command in input_commands:
#         action, *args = command.split()
        
#         if action == "ALLOT_WATER":
#             apartment_type = int(args[0])
#             ratio = tuple(map(int, args[1].split(':')))
#             apartment_data[apartment_type] = ratio

#         elif action == "ADD_GUESTS":
#             apartment_type = int(args[0])
#             guests = int(args[1])
#             if apartment_type in apartment_data:
#                 apartment_data[apartment_type] = (apartment_data[apartment_type][0], apartment_data[apartment_type][1] + guests)
#             else:
#                 print("Apartment type not allotted yet.")

#         elif action == "BILL":
#             bill_2bhk = water_manager.calculate_bill(2, apartment_data.get(2, (0, 0)), apartment_data.get(2, (0, 0))[1])
#             bill_3bhk = water_manager.calculate_bill(3, apartment_data.get(3, (0, 0)), apartment_data.get(3, (0, 0))[1])
#             print(f"{int(bill_2bhk)} {int(bill_3bhk)}")

#         else:
#             print("Invalid command")

# if __name__ == "__main__":
#     main()