import tkinter.filedialog
a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename,'r')

def read_grades(gradefile):
    '''(file open for reading)-> dict of{float:list of str}
    
    Read the grades from gradefile and return a dictionary where each key is a grade and
    each value is list ids of students who earned that grade.

    Precondition: gradefile starts with a header that contains no blank lines, then has a blabk line and then lines containing a student number and grade.
        
    '''

    #Skip over the header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    #Read the grades, accumlating them into a dict
    grade_to_ids = {}
    line = gradefile.readline()
    while line !='':
        student_id = line[:3]
        grade = float(line[3:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
            grade_to_ids[grade].append(student_id)
        line = gradefile.readline()

    return grade_to_ids

result = read_grades(a1_file)
print(result)