import argparse
import sys
import getpass
import pymongo
from datetime import datetime
from pprint import pprint


#Initialize client
myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['mydatabase']
#<User that ran script> <Machine> <Name of User on file> <Date of file> <submitted date>
col1 = mydb['collection1']
#<Name of User on file> <Date of file> <Frames to fix>
col2 = mydb['collection2']

#set up argparse
parser = argparse.ArgumentParser()
parser.add_argument('--files', dest='bl_flames', nargs='*')
parser.add_argument('--xytech', dest='xytech')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--output', action='store_true')

args = parser.parse_args()

#RUN AS python project_2.py FOR DATABASE CALLS
if args.bl_flames is None:
    #Answering database calls here
    print("No BL/Flames files selected")
    print('Database calls/answers ')

    #Question 1
    print('1) List all work done by user TDanza: ')
    find_work = {"Name of User on file": 'TDanza'}
    docs  = col2.find(find_work)
    for i in docs:
        pprint(i, width=100)

    #Question 2
    print('\n2) All work done before 3-25-2023 date on a Flame')
    find_flame = {'Machine': 'Flame'}
    test = []
    for i in col1.find(find_flame):
        name = i['Name of User on File']
        date = i['Date of file']
        if int(date) < 20230325:
            query = col2.find_one({'Name of User on file':name, 'Date of file':date})
            pprint(query)
        else:
            continue

    #Question 3
    print('\n3) What work done on hpsans13 on date 3-26-2023')
    q3 = col2.find({'Date of file':'20230326'})
    work_done = []
    for i in q3:
        for j in i['Frames to fix']:
            if 'hpsans13' in j:
                work_done.append(j)
    if len(work_done) == 0:
        print('No work done')
    else:
        for i in work_done:
            print(i)

    #Question 4
    print('\n4) Name of all Autodesk Flame users')
    q4 = col1.find({'Machine':'Flame'})
    name_dupe_check = []
    for i in q4:
        if i['Name of User on File'] in name_dupe_check:
            continue
        else:
            name_dupe_check.append(i['Name of User on File'])
            print(i['Name of User on File'])
    sys.exit(2)

#main code
else:
    job = args.bl_flames
    xytech = args.xytech

jobs_list = []

xytech_file = open(xytech, 'r')
xytech_folders = []

for line in xytech_file:
    if '/' in line:
        xytech_folders.append(line)

#parse baselight and flame files
for i in job:
    #parse the name of file
    file_info = i.replace('.\\import_files\\', "").replace('.txt', "")
    file_parse = file_info.split("_")
    machine = file_parse[0]
    user = file_parse[1]
    date = file_parse[2]

    current_file = open(i, 'r')
    bl = '/images1/Avatar'
    ftf_list = []
    if machine == 'Flame':
        lf_str = ''
        print('---------------Flame File: -------------------')
        for line in current_file:
            line_parse = line.split(' ')
            current_folder = line_parse.pop(1)
            new_loc = ""
            for xytech_line in xytech_folders:
                if current_folder in xytech_line:
                    new_loc = xytech_line.strip()
            first = ""
            pointer = ""
            last = ""
            for num in line_parse:
                #Skip <err> and <null>
                if not num.strip().isnumeric():
                    continue
                #Assign first number
                if first == "":
                    first = int(num)
                    pointer = first
                    continue
                #Keeping to range if succession
                if int(num) == (pointer+1):
                    pointer = int(num)
                    continue
                else:
                    #Range ends or no sucession, output
                    last = pointer
                    if first == last:
                        lf_str += "%s %s\n" % (new_loc, first)
                         
                    else:
                        lf_str += "%s %s-%s\n" % (new_loc, first, last)
                        
                    first= int(num)
                    pointer=first
                    last=""
            #Working with last number each line 
            last = pointer
            if first != "":
                if first == last:
                    lf_str += "%s %s\n" % (new_loc, first)
                    
                else:
                    lf_str += "%s %s-%s\n" % (new_loc, first, last)
                    
        #code for if verbose/output flagged    
        if args.verbose:
            print(lf_str)
        if args.output:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            loc_frames = []
            for i in lf_str.splitlines():
                loc_frames.append(i)
            col1.insert_one({
                'User Running Script': getpass.getuser(),
                'Machine': machine,
                'Name of User on File': user,
                'Date of file': date,
                'Submitted Date': dt_string
            })

            col2.insert_one({
                'Name of User on file': user,
                'Date of file': date,
                'Frames to fix': loc_frames    
            })
    elif machine == 'Baselight':
        lf_str = ''
    #read lines from current file
        print('---------------Baselight File: -------------------')
        for line in current_file:
            line_parse = line.split(' ')
            current_folder = line_parse.pop(0)
            sub_folder = current_folder.replace(bl, "")
            new_loc = ""
            for xytech_line in xytech_folders:
                if sub_folder in xytech_line:
                    new_loc = xytech_line.strip()
            first = ""
            pointer = ""
            last = ""
            
            for num in line_parse:
                #Skip <err> and <null>
                if not num.strip().isnumeric():
                    continue
                #Assign first number
                if first == "":
                    first = int(num)
                    pointer = first
                    continue
                #Keeping to range if succession
                if int(num) == (pointer+1):
                    pointer = int(num)
                    continue
                else:
                    #Range ends or no sucession, output
                    last = pointer
                    if first == last:
                        #print ("%s %s" % (new_loc, first))
                        lf_str += "%s %s\n" % (new_loc, first)
                    else:
                        #print ("%s %s-%s" % (new_loc, first, last))
                        lf_str += "%s %s-%s\n" % (new_loc, first, last)
                    first= int(num)
                    pointer=first
                    last=""
            #Working with last number each line 
            last = pointer
            if first != "":
                if first == last:
                    #print ("%s %s" % (new_loc, first))
                    lf_str += "%s %s\n" % (new_loc, first)
                else:
                    #print ("%s %s-%s" % (new_loc, first, last))
                    lf_str += "%s %s-%s\n" % (new_loc, first, last)
        
        #code for if verbose/output flagged
        if args.verbose:
            print(lf_str)
        if args.output:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            loc_frames = []
            for i in lf_str.splitlines():
                loc_frames.append(i)
            col1.insert_one({
                'User Running Script': getpass.getuser(),
                'Machine': machine,
                'Name of User on File': user,
                'Date of file': date,
                'Submitted Date': dt_string
            })

            col2.insert_one({
                'Name of User on file': user,
                'Date of file': date,
                'Frames to fix': loc_frames   
            })