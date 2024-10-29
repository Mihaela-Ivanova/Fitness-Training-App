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
        self.exercises = [ex for ex in self.exercises if ex['exercise'].name != exercise_name]

    def view_workout(self):
        print(f"Workout: {self.name}")
        for ex in self.exercises:
            print(f"{ex['exercise'].name}: {ex['sets']} sets, {ex['reps']} reps, {ex['rest_time']} seconds rest")


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
          "\n3. See available excercises")

    command = int(input())
    if command == 5:
        for person in people:
            print(person.display_info())
        break
    if command == 1:
        name = input("What is your name: ")
        age = int(input("How old are you: "))
        weight = int(input("What is your current weight: "))
        height =  int(input("What is your current height: "))
        goal = input("What is your fitness goal: ")

        person = User(name, age,weight, height, goal)
        people.append(person)

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



