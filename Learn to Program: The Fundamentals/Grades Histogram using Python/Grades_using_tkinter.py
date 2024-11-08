import tkinter.filedialog
a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename,'r')

a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_histfile = open(a1_histfilename,'w')
#for line in a1_file:
#   print(line)


def read_grades(gradefile):
    '''(file open for reading) ->list of float

    Read and return the list of grades in gradefile.

    Precondition: gradefile starts witha header that contains
    no blank lines, then has a blank line, and then lines containing a student number and a grade.
    '''

    #Skip over the header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    
    #Read the grades, accumlating them into a list.
    grades=[]

    line = gradefile.readline()
    while line!='':
        #Now we have s string containing the info for a
        #single student.
        #Find the last space and take everything after that space.
        grade = line[line.rfind(' ') +1: ]
        grades.append(float(grade))
        line = gradefile.readline()
    return grades

grades =  read_grades(a1_file)


def count_grade_range(grades):
    '''
    (list of float)->(list of int)

    Returns a list on int where each index indicates how many were in these ranges:
    0-9: index 0
    10-19: index 1
    20-29: index 2
    :
    90-99: index 9
    100: index 10

    >>> count_grade_range([80.0, 50.0, 45.0, 90.0, 94.0, 52.0, 25.0, 100.0, 43.0, 10.0])
    [2,0,0,1,1,1,1,0,1,0]
    '''
    #print(len(grades))
    range_counts = [0] * (len(grades)+1)
    #print(range_counts)
    for grade in grades:
        which_range = int(grade//10)
        #print(which_range)
        range_counts[ which_range ] = range_counts[ which_range ] + 1
    return range_counts


range_counts = count_grade_range(grades)

print(range_counts)

def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing)->NoneType

    Write a histogram of *'s based on the number of grades in file

    The output format:
    0-9: *
    10-19: ***
    :
    :
    90-99: **
    100: *
    '''
    histfile.write('0-9:  ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    #Write the 2 digit ranges.
    for i in range(1,10):
        low = i* 10
        high = i* 10+9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        histfile.write('\n')

    histfile.write('100:  ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')

write_histogram(range_counts, a1_histfile)
a1_file.close()
a1_histfile()
