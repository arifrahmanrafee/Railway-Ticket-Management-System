
class Train:
    def __init__(self, train_name, source, destination, time, num_passengers, train_code):
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.time = time
        self.num_passengers = num_passengers
        self.train_code = train_code
    
    def __repr__(self):
        return f"Train({self.train_name}, {self.source}, {self.destination}, {self.time}, {self.num_passengers}, {self.train_code})"


class Train_route:    
    all_trains=[]

    def __init__(self,source,destination):
        self.source=source.capitalize()
        self.destination=destination.capitalize()
        self.train_routes = {
        "Dhaka": {
            "Chittagong": [
                {"train_name": "Subarna Express", "train_number": 705, "category": "Intercity Express", "time": "710", "train_code": 705},
                {"train_name": "Turna Express", "train_number": 741, "category": "Intercity Express", "time": "800", "train_code": 741},
                {"train_name": "Mahanagar Provati", "train_number": 704, "category": "Intercity Express", "time": "830", "train_code": 704}
            ],
            "Rajshahi": [
                {"train_name": "Silkcity Express", "train_number": 754, "category": "Intercity Express", "time": "900", "train_code": 754},
                {"train_name": "Padma Express", "train_number": 760, "category": "Intercity Express", "time": "1000", "train_code": 760},
                {"train_name": "Madhumati Express", "train_number": 756, "category": "Intercity Express", "time": "1030", "train_code": 756}
            ],
            "Khulna": [
                {"train_name": "Chitra Express", "train_number": 763, "category": "Intercity Express", "time": "1919", "train_code": 763},
                {"train_name": "Kapotaksha Express", "train_number": 716, "category": "Intercity Express", "time": "2020", "train_code": 716},
                {"train_name": "Mohananda Express", "train_number": 16, "category": "Intercity Express", "time": "2005", "train_code": 16}
            ],
            "Barishal": [
                {"train_name": "Sundarban Express", "train_number": 725, "category": "Intercity Express", "time": "1920", "train_code": 725},
                {"train_name": "Rocket Express", "train_number": 23, "category": "Intercity Express", "time": "1810", "train_code": 23}
            ],
            "Rangpur": [
                {"train_name": "Rangpur Express", "train_number": 771, "category": "Intercity Express", "time": "1630", "train_code": 771},
                {"train_name": "Uttara Express", "train_number": 31, "category": "Intercity Express", "time": "1610", "train_code": 31}
            ],
            "Sylhet": [
                {"train_name": "Parabat Express", "train_number": 709, "category": "Intercity Express", "time": "800", "train_code": 709},
                {"train_name": "Upaban Express", "train_number": 739, "category": "Intercity Express", "time": "1000", "train_code": 739},
                {"train_name": "Jayantika Express", "train_number": 717, "category": "Intercity Express", "time": "900", "train_code": 717}
            ]
        },
        "Chittagong": {
            "Dhaka": [
                {"train_name": "Subarna Express", "train_number": 705, "category": "Intercity Express", "time": "1800", "train_code": 705},
                {"train_name": "Turna Express", "train_number": 741, "category": "Intercity Express", "time": "1900", "train_code": 741},
                {"train_name": "Mahanagar Provati", "train_number": 704, "category": "Intercity Express", "time": "2000", "train_code": 704}
            ],
            "Rajshahi": [
                {"train_name": "Silkcity Express", "train_number": 754, "category": "Intercity Express", "time": "900", "train_code": 754},
                {"train_name": "Padma Express", "train_number": 760, "category": "Intercity Express", "time": "1000", "train_code": 760},
                {"train_name": "Madhumati Express", "train_number": 756, "category": "Intercity Express", "time": "1100", "train_code": 756}
            ],
            "Khulna": [
                {"train_name": "Chitra Express", "train_number": 763, "category": "Intercity Express", "time": "1830", "train_code": 763},
                {"train_name": "Kapotaksha Express", "train_number": 716, "category": "Intercity Express", "time": "1820", "train_code": 716},
                {"train_name": "Mohananda Express", "train_number": 16, "category": "Intercity Express", "time": "1930", "train_code": 16}
            ],
            "Barishal": [
                {"train_name": "Sundarban Express", "train_number": 725, "category": "Intercity Express", "time": "1300", "train_code": 725},
                {"train_name": "Rocket Express", "train_number": 23, "category": "Intercity Express", "time": "1530", "train_code": 23}
            ],
            "Rangpur": [
                {"train_name": "Rangpur Express", "train_number": 771, "category": "Intercity Express", "time": "1225", "train_code": 771},
                {"train_name": "Uttara Express", "train_number": 31, "category": "Intercity Express", "time": "1730", "train_code": 31}
            ],
            "Sylhet": [
                {"train_name": "Parabat Express", "train_number": 709, "category": "Intercity Express", "time": "0800", "train_code": 709},
                {"train_name": "Upaban Express", "train_number": 739, "category": "Intercity Express", "time": "830", "train_code": 739},
                {"train_name": "Jayantika Express", "train_number": 717, "category": "Intercity Express", "time": "930", "train_code": 717}
            ]
        },
        "Khulna": {
            "Dhaka": [
                {"train_name": "Chitra Express", "train_number": 763, "category": "Intercity Express", "time": "1000", "train_code": 763},
                {"train_name": "Kapotaksha Express", "train_number": 716, "category": "Intercity Express", "time": "1420", "train_code": 716},
                {"train_name": "Mohananda Express", "train_number": 16, "category": "Intercity Express", "time": "1750", "train_code": 16}
            ],
            "Chittagong": [
                {"train_name": "Chitra Express", "train_number": 763, "category": "Intercity Express", "time": "1840", "train_code": 763},
                {"train_name": "Kapotaksha Express", "train_number": 716, "category": "Intercity Express", "time": "1940","train_code": 716},
                {"train_name": "Mohananda Express", "train_number": 16, "category": "Intercity Express", "time": "2030", "train_code": 16}
            ],
            "Rajshahi": [
                {"train_name": "Silkcity Express", "train_number": 754, "category": "Intercity Express", "time": "730", "train_code": 754},
                {"train_name": "Padma Express", "train_number": 760, "category": "Intercity Express", "time": "830", "train_code": 760},
                {"train_name": "Madhumati Express", "train_number": 756, "category": "Intercity Express", "time": "930", "train_code": 756}
            ],
            "Barishal": [
                {"train_name": "Sundarban Express", "train_number": 725, "category": "Intercity Express", "time": "1230", "train_code": 725},
                {"train_name": "Rocket Express", "train_number": 23, "category": "Intercity Express", "time": "1830", "train_code": 23}
            ],
            "Rangpur": [
                {"train_name": "Rangpur Express", "train_number": 771, "category": "Intercity Express", "time": "1505", "train_code": 771},
                {"train_name": "Uttara Express", "train_number": 31, "category": "Intercity Express", "time": "1630", "train_code": 31}
            ],
            "Sylhet": [
                {"train_name": "Parabat Express", "train_number": 709, "category": "Intercity Express", "time": "1230", "train_code": 709},
                {"train_name": "Upaban Express", "train_number": 739, "category": "Intercity Express", "time": "1130", "train_code": 739},
                {"train_name": "Jayantika Express", "train_number": 717, "category": "Intercity Express", "time": "1245", "train_code": 717}
            ]}
        }
        
        num_passengers = 100

        for source, destinations in self.train_routes.items():
            for destination, trains in destinations.items():
                for train in trains:
                
                    train_obj = Train(
                        train_name=train["train_name"],
                        source=source,
                        destination=destination,
                        time=train["time"],
                        num_passengers=num_passengers,
                        train_code=train["train_code"]
                    )
                    self.all_trains.append(train_obj)
   
       
        self.desired_train=[]
        for train in self.all_trains:
            if self.source ==train.source and self.destination==train.destination:
                self.desired_train.append(train)
            


class train_time(Train_route):
    def __init__(self,source,destination,timing1,timing2):
        y=super().__init__(source,destination)
        for all in self.desired_train:
            if int(all.time)>=timing1 and int(all.time)<=timing2:
                print(all)
        
# train_time("Dhaka","Chittagong",900,1600)