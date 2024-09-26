class HomeAutomation:
    def __init__(self):
        self.devices= {
            "lights":{"state": "off"},
            "thermostat": {"temperature ": 70},
        }

     #now we will define method to "turn on/off lights


    def toggle_lights(self):
        if self.devices['lights']['state']=='off':
            self.devices['lights']['state']='on'
            print('Lights turned on ')
        else:
            self.devices['lights']['state']='off'
            print("Lights turned off ")

    
    #we define temperature method

    def adjust_temperature(self,temperature):
        self.devices['thermostat']['temperature']=temperature
        print(f"Temperature set to {temperature} degrees")

    


    # we define method to show status of all devices 
    
    def show_status(self):
        print("Current status: ")
        for device,status in self.devices.items():
            print(f"{device}:{status}")

#now defining our "main" function for user interfernce

def main():
    home= HomeAutomation()
    print("Welcome to Home Interaction")

        #adding user interfernce commands

    while True:
        print("\n What would you like to do? ")
        print("1.  Toggle lights")
        print("2. Adjust thermostat temperature ")
        print("3. Show current status")
        print("4. Exit")

       #asking user for their choice of command

        choice = input("Enter your choice (1-4): ")

        #now responding according to choice

        if choice == "1":
            home.toggle_lights()
        elif choice=="2":
            temperature= int(input("Enter the desire temperatue: "))
            home.adjust_temperature(temperature)
        
        elif choice== "3":
            home.show_status()
        elif choice=="4":
            print("Exiting the Home automation app . Goodbye")
            break
        else:
            print("Invalid choice. Please enter correct number")
        
        #now adding logic to run app
if __name__ == "__main__" :
    main()





       