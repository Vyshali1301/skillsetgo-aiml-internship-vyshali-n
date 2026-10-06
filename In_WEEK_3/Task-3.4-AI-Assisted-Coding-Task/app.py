"""
Student Grade Manager - a small CLI app (Task 3.4, AI-assisted coding).

Built with AI assistance (Claude). This file is the AI-generated starting point - see audit_notes.md
for the human review: what was checked, what was wrong or missing, and what was fixed.

Features:
- add a student with a list of scores
- compute each student's average and a letter grade
- list all students sorted by average
- save/load records to a JSON file so data isn't lost between runs
"""
import json
import os

DATA_FILE = "students.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def add_student(data, name, scores):
    data[name] = scores
    save_data(data)


def average(scores):
    return sum(scores) / len(scores)


def list_students(data):
    if not data:
        print("No students recorded yet.")
        return
    ranked = sorted(data.items(), key=lambda item: average(item[1]), reverse=True)
    print(f"{'Name':15s} {'Average':>8s} {'Grade':>6s} {'Scores'}")
    for name, scores in ranked:
        avg = average(scores)
        print(f"{name:15s} {avg:8.1f} {letter_grade(avg):>6s} {scores}")


def main():
    data = load_data()
    while True:
        print("\n1) Add student  2) List students  3) Quit")
        choice = input("> ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            raw = input("Scores (comma separated, e.g. 85,90,78): ").strip()
            scores = [float(s) for s in raw.split(",")]
            add_student(data, name, scores)
            print(f"Added {name}.")
        elif choice == "2":
            list_students(data)
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
