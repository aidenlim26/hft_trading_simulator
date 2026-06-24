class WarehouseTracker:
    def __init__(self):
        self.inventory_data = {
            "A1" : {"product_name" : "Golf Clubs", "starting_quantity" : "15" },
            "B2" : {"product_name" : "Baseball Bats", "starting_quantity" : "55" },
            "C3" : {"product_name" : "Hockey Sticks", "starting_quantity" : "21" },
            "D4" : {"product_name" : "Pickleballs", "starting_quantity" : "3" },
            "E5" : {"product_name" : "Footballs", "starting_quantity" : "67" },
        }

        self.floor_map = [
            ['A1','Empty','Empty','Empty','Empty'],
            ['Empty','B2','Empty','Empty','Empty'],
            ['Empty','Empty','C3','Empty','Empty'],
            ['Empty','Empty','Empty','D4','Empty'],
            ['Empty','Empty','Empty','Empty','E5']
        ]

    def display_inventory(self):
        for i in range(len(self.floor_map)):
            for c in range(len(self.floor_map[i])):
                print(self.floor_map[i][c], end = " ")
            print()
    
    def shipment_processor(self,order_batch):
        print("Processing Order Shipments")
        for item_id,qty,row,col in order_batch:
            print(f"Checking Row: {row}, Column: {col} for Item: {item_id}")
            if row < 0 or row >= len(self.floor_map) or col < 0 or col >= len(self.floor_map[0]):
                print("This floor coordinate does not exist")
                continue
            
            if self.floor_map[row][col] != item_id:
                print(f"Mismatch error! {item_id} is not stored at this location")
                continue
            
            item_info = self.inventory_data[item_id]

            current_stock = int(item_info["starting_quantity"])

            if current_stock >= qty:
                new_stock = current_stock - qty
                item_info["starting_quantity"] = str(new_stock)

                print(f"Success! Shipped {qty} x {item_info['product_name']}")
                print(f"Updated Stock: {item_info['starting_quantity']}")
            else:
                print(f"Failed! Insufficient stock for {item_info['product_name']}")


warehouse_tracker = WarehouseTracker()

orders = [
    ("A1", 5, 0, 0),    
    ("B2", 100, 1, 1),  
    ("C3", 2, 0, 4),    
    ("E5", 1, 4, 4) 
]
            
warehouse_tracker.shipment_processor(orders)
                


