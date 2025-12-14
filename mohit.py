#TASK 1=>
def main():
    student_marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 65,
        "Eve": 95
    }


    print("Students in record:", ", ".join(student_marks.keys()))


    name = input("Enter the student's name to check their marks: ").strip()


    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print(f"Error: Student '{name}' not found in the records.")

if __name__ == "__main__":
    main()

#TASK 2=>
def main():
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        extracted_list = numbers[:5]
        reversed_list = extracted_list[::-1]

        print(f"Original List:  {numbers}")
        print(f"Extracted List: {extracted_list}")
        print(f"Reversed List:  {reversed_list}")
if __name__ == "__main__":

        main()
