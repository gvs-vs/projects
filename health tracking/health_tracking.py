import datetime

#defining function to store data in text file

def log_data(file_name,data):
    with open(file_name,'a') as f:
        f.write(data + '\n')

#function to record today's weight:
def record_weight():
    weight = input("Enter your weight (in kg):")

    log_data('weight_log.txt', f"{datetime.date.today()}: {weight}kg")
    print("Weight recorded succesfully")

#function to record calories

def record_calories():

    calories = input("Enter the numner of calories consumed today: ")
    log_data('calories_log.txt',f"{datetime.date.today()}:{calories} calories")
    print("Calories recorded")

#Function to record exercise details

def record_exercise():
    exercise = input("Enter the type of exercise: ")
    duration = input("Enter the duration of exercise (in minutes): ")
    log_data('exercise_log.txt', f"{datetime.date.today()}: {exercise} for {duration} minutes")
    print("Exercise recorded successfully")

#function to view recorded data

def view_data():
    choice = input("What would you like to view? (1) Weight (2)Calories (3) Exercise:")
    file_dict ={'1': 'weight_log.txt', '2': 'calories_log.txt', '3': 'exercise_log.txt'}

    if choice in file_dict:
        try:
            with open(file_dict[choice], 'r') as f:
                print(f.read())
        
        except FileNotFoundError:
            print("No data recorded yet. ")
    

    else:
        print("Invalid choice")


#creating user interaction

def main():
    print("Welcome to the health tracking App!")

    while True:
        print("\nWhat would you like to do? ")
        print("1: Record weight")
        print("2: Record calories consumed")
        print("3: Record exercise")
        print("4: View your data")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice =='1':
            record_weight()

        elif choice=='2':
            record_calories()

        elif choice =='3':
            record_exercise()
        
        elif choice=='4':
            view_data()

        elif choice=='5':
            print("Thanks")
            break

if __name__=="__main__":
    main()

        




