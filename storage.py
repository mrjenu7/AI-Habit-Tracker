def save_habit(entry):
    with open("habits.txt", "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def get_habits():
    try:
        with open("habits.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""