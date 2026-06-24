class ParkingGarage:
    def __init__(self):
        self.members = {
            "SGP123" : {"name" : "Aiden", "type" : "VIP"},
            "GBR456" : {"name" : "Boris", "type" : "Regular"},
            "GB2015" : {"name" : "David", "type" : "VIP"},
            "USA679" : {"name" : "Kier", "type" : "Regular"}
        }

        self.garage_floor = [
            ["Empty","SGP123","USA679"],
            ["GBR456","Empty","Empty"],
            ["Empty","Empty","GB2015"]
        ]

    def display_garage(self):
        for i in range(len(self.garage_floor)):
            for c in range(len(self.garage_floor[0])):
                print(self.garage_floor[i][c], end=" ")
            print()
    
    def parking_processor(self,arrival_list):
        print("Processing Parking")
        for member_id,row,col in arrival_list:
            print(f"Checking Row: {row}, Column: {col}, for MemberID: {member_id}")
            if row < 0 or row >= len(self.garage_floor) or col < 0 or col >= len(self.garage_floor[0]):
                print(f"Error! The coordinate entered does not exist.")
                continue
            if self.garage_floor[row][col] != member_id:
                print(f"Mismatch Error! {member_id} is not parked at this location!")
                continue
            
            else:
                member_info = self.members[member_id]
                print(f"Success! Driver's name: {member_info["name"]}, Membership type: {member_info["type"]}")

parking_garage = ParkingGarage()

arrival_list = [
    ("SGP123",0,1),
    ("GBR456",1,0),
    ("GB2015",2,2),
    ("USA679",0,2)
]

parking_garage.display_garage()

parking_garage.parking_processor(arrival_list)


