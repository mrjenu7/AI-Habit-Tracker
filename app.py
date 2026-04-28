from storage import save_habit, get_habits
from llm_service import analyze_habits

print("🤖 AI Habit Tracker & Coach")

while True:

    print("\n1. Add Habit")
    print("2. Analyze Progress")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        habit = input("Enter today's habit: ")
        save_habit(habit)
        print("✅ Saved!")

    elif choice == "2":
        data = get_habits()
        result = analyze_habits(data)
        print("\n📊 AI Feedback:\n", result)

    elif choice == "3":
        break