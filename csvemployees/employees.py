######################################################################################
#                             Quick Code                                             #
######################################################################################
# import csv

# with open('employees.csv', 'r') as file:
#   csv_reader = csv.reader(file)
  
#   next(csv_reader)
   
#   with open('employee_report', 'w') as new_file:
#     csv_writer = csv.writer(new_file)
    
#     for line in csv_reader:
#       csv_writer.writerow(line)



######################################################################################
#                             Online Code                                            #
######################################################################################
# import csv
# import os

# def read_employees(csv_file_location):
#     # Open the file
#     with open(csv_file_location,'r') as f:
#         csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#         # Read the rows of the file into a dictionary
#         employee_file = csv.DictReader(f, dialect='empDialect')
#         employee_list = []
#         for data in employee_file:
#             employee_list.append(data)

#     return employee_list


# def process_data(employee_list):
#     department_list = []
#     for employee_data in employee_list:
#        department_list.append(employee_data['Department'])

#     department_data = {}
#     for department_name in set(department_list):
#         department_data[department_name] = department_list.count(department_name)
    
#     return department_data


# def write_report(dictionary, report_file):
#     with open(report_file, "w+") as f:
#         for k in sorted(dictionary):
#             f.write(str(k)+':'+str(dictionary[k])+'\n')
#         f.close()

# if __name__ == "__main__":
#   # Variables
#   cwd       = os.getcwd()
#   file_path = os.path.join(cwd, 'employees.csv')
 
#   # Read employees.csv file 
#   employee_list = read_employees(file_path)
#   print(employee_list)

  # dictionary = process_data(employee_list)
  # print(dictionary)

  # write_report(dictionary,os.path.join(os.path.dirname(__file__),'report.txt'))

######################################################################################
#                             Code to Execute                                        #
######################################################################################
# Import modules
import csv
import os

def ReadCsvFile(csv_file):
  with open(csv_file, 'r') as f:
    data = csv.DictReader(f)
    for row in data:
      print(row)
    return data

def count_department_members(csv_file):
  # Variables
  department_counts = {}
  field_header      = ' Department' 
  
  # Create department counts dictionary
  reader = ReadCsvFile(csv_file)
  print("\tC")
  # Get each record in the csv file
  for row in reader:
    print("\tD")
    # Get the current department name from the record
    department_name = row[field_header]
    # If department name exists in the dictionary, add 1 to count 
    if department_name in department_counts:
      department_counts[department_name] += 1
    # If department not yet in dictionary, start the count at 1
    else:
      department_counts[department_name] = 1

  # Return diciontary of department name as key, and counts as value            
  return department_counts

def ListDepartmentMembers(csv_file, department_name):
  # Vars
  department_members = {}
  return department_name, department_members

def write_department_counts_to_file(department_counts, output_file):
  with open(output_file, 'w') as file:
    for department, count in department_counts.items():
      file.write(f"{department}: {count}\n")


if __name__ == "__main__":
    cwd         = os.getcwd()
    csv_file    = os.path.join(cwd,'employees.csv')
    output_file = 'report.txt'  
    
    # Run Main Code
    print("\tA")
    department_counts = count_department_members(csv_file)
    print("\tE")
    write_department_counts_to_file(department_counts, output_file)

    print("Report written successfully!")





