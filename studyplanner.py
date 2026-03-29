import datetime

class Subject:
    def __init__(self, name, difficulty, importance, days_left):
        self.name = name
        self.difficulty = difficulty
        self.importance = importance
        self.days_left = days_left
        self.priority = self.calculate_priority()

    def calculate_priority(self):
        return (self.difficulty * 0.4) + (self.importance * 0.4) + ((1 / self.days_left) * 0.2)


def get_subjects():
    subjects = []
    n = int(input("Enter number of subjects: "))

    for _ in range(n):
        name = input("Subject name: ")
        difficulty = int(input("Difficulty (1-5): "))
        importance = int(input("Importance (1-5): "))
        days_left = int(input("Days until exam: "))

        subjects.append(Subject(name, difficulty, importance, days_left))

    return subjects


def generate_schedule(subjects, hours_per_day):
    subjects.sort(key=lambda x: x.priority, reverse=True)

    total_priority = sum(sub.priority for sub in subjects)

    schedule = []
    for sub in subjects:
        allocated_time = (sub.priority / total_priority) * hours_per_day
        schedule.append((sub.name, round(allocated_time, 2)))

    return schedule


def display_schedule(schedule):
    print("\n📅 Today's Study Plan:\n")
    for subject, hours in schedule:
        print(f"👉 {subject}: {hours} hours")


def main():
    print("=== AI Study Planner ===")

    subjects = get_subjects()
    hours_per_day = float(input("Total study hours per day: "))

    schedule = generate_schedule(subjects, hours_per_day)
    display_schedule(schedule)


if __name__ == "__main__":
    main()