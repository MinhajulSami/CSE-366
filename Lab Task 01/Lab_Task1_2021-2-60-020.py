import random as pick
import os
from time import sleep
from typing import List

def get_students_from_file(student_file: str) -> List[str]:
    try:
        if not os.path.exists(student_file):
            print(f"Oops! Can't find {student_file}!")
            return []
            
        with open(student_file) as f:
            class_list = []
            for roll in f:
                if roll.strip():
                    class_list.append(roll.strip())
            
        if not class_list:
            print("File is empty!")
            return []
            
        return class_list
        
    except Exception as oops:
        print(f"Something went wrong: {oops}")
        return []

def do_viva_selection(class_list: List[str]) -> None:
    not_done = class_list[:]  
    done = []
    viva_count = 1
    round_num = 1
    
    print("\n🎲 Let's pick students for viva!")
    
    while True:
        print(f"\n📋 Round {round_num}")
        print("-" * 30)
        
        print(f"Students in class: {len(class_list)}")
        print(f"Still waiting: {len(not_done)}")
        
        while not_done:
            lucky_student = pick.choice(not_done)
            not_done.remove(lucky_student)
            done.append(lucky_student)
          
            print(f"\nViva #{viva_count}")
            print(f"→ {lucky_student}")
            print(f"({len(not_done)} students left)")
            
            viva_count += 1
            sleep(0.5)  # Quick pause
            
        print("\n Viva Session Done!")
      
        print("\nStart over? (y/n)")
        if input("> ").lower().strip() != 'y':
            print("\n Everything Completed")
            break
        not_done = class_list[:]
        done.clear()
        round_num += 1
        print("\n🔄 Starting fresh...")

def run():
    students = get_students_from_file("student.txt")
    if students:
        do_viva_selection(students)
    
if __name__ == "__main__":
    run()