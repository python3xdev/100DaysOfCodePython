import pandas

student_dict = {
    'student': ['Angela', 'James', 'Daniel'],
    'score': [56, 76, 97],
}
# Looping through dict's
# for k,v in student_dict.items():
#     print(k)

students_data_frame = pandas.DataFrame(student_dict)
# print(students_data_frame)

# Loop through a data frame
# for k, v in students_data_frame.items():
#     print(v)

# Loop through rows
for index, row in students_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == 'Daniel':
        print(row.score)
