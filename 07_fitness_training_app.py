class User:
    def __init__(self, name, age, weight, height, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.workout_history = []

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_goal(self, new_goal):
        self.goal = new_goal

    def log_workout(self, workout):
        self.workout_history.append(workout)

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}cm, Goal: {self.goal}"


class Exercise:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_exercise(self):
        return f"{self.name} ({self.difficulty}): \n{self.description}\n"


class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise, sets, reps, rest_time):
        self.exercises.append({'exercise': exercise, 'sets': sets, 'reps': reps, 'rest_time': rest_time})

    def remove_exercise(self, exercise_name):
        self.exercises = [ex for ex in self.exercises if ex['exercise'] != exercise_name]

    def view_workout(self):
        print(f"Workout: {self.name}")
        for ex in self.exercises:
            print(f"{ex['exercise']}: {ex['sets']} sets, {ex['reps']} reps, {ex['rest_time']} seconds rest")


class ProgressTracker:
    def __init__(self, user):
        self.user = user

    def log_workout(self, workout):
        self.user.log_workout(workout)

    def generate_report(self):
        total_workouts = len(self.user.workout_history)
        return f"{self.user.name} has completed {total_workouts} workouts."


print("Welcome to FitnesTracker2000")
people = []
exercises = []
workout_plans = []

squats = Exercise("Squats", "Strength exercise in which the trainee lowers their hips from a standing position and then stands back up", "Medium")
push_ups = Exercise("Push-ups", "Raising and lowering the body using the arms", "Medium")
lunges = Exercise("Lunges", "Lower body exercise that involves stepping one leg in front of your body and bending both knees while keeping your torso in an upright position", "Low")
crunches = Exercise("Crunches", "Abdominal exercise that works the rectus abdominis muscle", "Medium")
running = Exercise("Tredmill running", "Running on a tredmill machine", "Low")
exercises.append(squats)
exercises.append(push_ups)
exercises.append(lunges)
exercises.append(crunches)
exercises.append(running)



while True:
    print("Please pick one of the following options: "
          "\n1. Create a new user profile."
          "\n2. Update existing profile "
          "\n3. See available excercises"
          "\n4. Create or Modify Workout Plans"
          "\n5. View Workout Plans"
          "\n6. Log a Completed Workout"
          "\n7. View Personal Workout History"
          "\n8. Exit")


    command = int(input())
    if command == 8:
        for person in people:
            print(person.display_info())
        break
    if command == 1:
        name = input("What is your name: ")
        someone = next((person for person in people if person.name == name), None)
        if not someone:
            age = int(input("How old are you: "))
            weight = int(input("What is your current weight: "))
            height =  int(input("What is your current height: "))
            goal = input("What is your fitness goal: ")

            person = User(name, age,weight, height, goal)
            people.append(person)
        else:
            print('Name already existing')

    elif command == 2:
        user = input("Which user do you want to update: ")
        for person in people:
            if user == person.name:
                change = input("What do you want to update (weight/goal): ")
                while change != 'weight' or change != 'goal':
                    if change == 'weight':
                        update = input("What is your current weight: ")
                        person.update_weight(update)
                        break
                    elif change == 'goal':
                        update = input("What is your current goal: ")
                        person.update_goal(update)
                        break
                    else:
                        print("Please pick either wight or goal")
                        change = input("What do you want to update (weight/goal): ")
            else:
                print('Name not existing in database')

    elif command == 3:
        for exercise in exercises:
            print(exercise.display_exercise())

    elif command == 4:
        operation = input('Do you want to create a new workout plan or modify an already existing one? (new/modify) ')
        if operation == 'new':
            name = input('What do you want to call the workout plan? ')

            if any(plan.name == name for plan in workout_plans):
                print("Workout plan already exists. Please modify the existing plan or create a new one.")

            else:
                workout = Workout(name)
                exercise_name = input("What exercise do you want to add in the workout plan? ")
                sets = int(input(f"How many sets do you want to do of {exercise_name}? "))
                reps = int(input(f"How many reps do you want to do by set of {exercise_name}? "))
                reps_time = int(input("How much time should you have for a rep? "))

                workout.add_exercise(exercise_name, sets, reps, reps_time)
                workout_plans.append(workout)


        elif operation == 'modify':

            name = input("Which workout plan do you want to modify? ")

            workout = next((plan for plan in workout_plans if plan.name == name), None)

            if workout:
                new_operation = input("Do you want to add or remove an exercise from the workout plan? (add/remove) ")

                if new_operation == 'add':
                    exercise_name = input("What exercise do you want to add in the workout plan? ")
                    sets = int(input(f"How many sets do you want to do of {exercise_name}? "))
                    reps = int(input(f"How many reps do you want to do per set of {exercise_name}? "))
                    rest_time = int(input("How much rest time between sets (in seconds)? "))


                    workout.add_exercise(exercise_name, sets, reps, rest_time)
                    print(f"{exercise_name} has been added to workout '{name}'.")



                elif new_operation == 'remove':
                    exercise_name = input("What exercise do you want to remove from the workout plan? ")
                    workout.remove_exercise(exercise_name)
                    print(f"{exercise_name} has been removed from workout '{name}'.")

            else:
                print("Workout plan not found.")

    elif command == 5:
        for workout in workout_plans:
            workout.view_workout()


    elif command == 6:
        name = input("Enter the user's name who completed the workout: ")
        user = next((person for person in people if person.name == name), None)

        if user:
            workout_name = input("Enter the name of the workout completed: ")
            workout = next((w for w in workout_plans if w.name == workout_name), None)

            if workout:
                tracker = ProgressTracker(user)
                tracker.log_workout(workout)
                print(f"Logged {workout.name} for {user.name}.")

            else:
                print("Workout not found.")

        else:
            print("User not found.")


    elif command == 7:
        name = input("Enter the user's name to view workout history: ")
        user = next((person for person in people if person.name == name), None)

        if user:
            tracker = ProgressTracker(user)
            print(tracker.generate_report())

        else:
            print("User not found.")