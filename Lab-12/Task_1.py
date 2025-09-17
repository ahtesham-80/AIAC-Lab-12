import random
import time
class Student:
    """Represents a student record with name, roll number, and CGPA."""
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa
    def __repr__(self):
        return f"Student(Name='{self.name}', RollNo='{self.roll_no}', CGPA={self.cgpa})"
def generate_large_dataset(size):
    """Generates a large list of student records."""
    dataset = []
    for i in range(size):
        name = f"Student_{i}"
        roll_no = f"R{i}"
        cgpa = round(random.uniform(7.0, 10.0), 2)
        dataset.append(Student(name, roll_no, cgpa))
    return dataset
# --- Quick Sort Implementation ---
def quick_sort(students):
    """Sorts a list of students by CGPA in descending order using Quick Sort."""
    if len(students) <= 1:
        return students
    else:
        pivot = students[len(students) // 2]
        less = [s for s in students if s.cgpa > pivot.cgpa]
        equal = [s for s in students if s.cgpa == pivot.cgpa]
        greater = [s for s in students if s.cgpa < pivot.cgpa]
        return quick_sort(less) + equal + quick_sort(greater)
# --- Merge Sort Implementation ---
def merge(left, right):
    """Merges two sorted lists of students."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].cgpa >= right[j].cgpa:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(students):
    """Sorts a list of students by CGPA in descending order using Merge Sort."""
    if len(students) <= 1:
        return students
    mid = len(students) // 2
    left_half = students[:mid]
    right_half = students[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)
# --- Top 10 Students Function ---
def get_top_10_students(students):
    """Returns the top 10 students with the highest CGPA."""
    sorted_students = sorted(students, key=lambda s: s.cgpa, reverse=True)
    return sorted_students[:10]
if __name__ == "__main__":
    DATASET_SIZE = 50000
    print(f"Generating a dataset of {DATASET_SIZE} student records...")
    students_for_quick = generate_large_dataset(DATASET_SIZE)
    students_for_merge = list(students_for_quick) # Create a copy for the other algorithm
    # --- Performance Comparison ---
    print("\n--- Performance Comparison ---")
    # Quick Sort
    start_time_quick = time.time()
    quick_sorted_list = quick_sort(students_for_quick)
    end_time_quick = time.time()
    quick_sort_duration = end_time_quick - start_time_quick
    print(f"Quick Sort completed in: {quick_sort_duration:.4f} seconds.")
    # Merge Sort
    start_time_merge = time.time()
    merge_sorted_list = merge_sort(students_for_merge)
    end_time_merge = time.time()
    merge_sort_duration = end_time_merge - start_time_merge
    print(f"Merge Sort completed in: {merge_sort_duration:.4f} seconds.")
    # --- Output Top 10 Students ---
    print("\n--- Top 10 Students for Placement Drive (by CGPA) ---")
    top_10 = get_top_10_students(quick_sorted_list) # Use the sorted list from Quick Sort
    for i, student in enumerate(top_10):
        print(f"{i+1}. {student}")



















        