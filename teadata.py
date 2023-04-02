import csv, tea

blank_tea = tea.tea('No Tea Found', '?', '?', ['?'], ["?"], '?', "?", "?", '?')

def import_tea():

        tea_list = []

        with open('teadata.csv', newline='') as csvfile:
            teareader = csv.reader(csvfile, skipinitialspace=True)
            for Name, Category, Feeling, Diseases, Regions, Rare, Caffenie, Description, Link in teareader:
                # tea_list.append(str.split(row))
                # tea_list.append([Name, Category, Feeling, Diseases.split(','), Regions.split(','), Rare, Caffenie])
                next_tea = tea.tea(Name, Category, Feeling, Diseases.split(','), Regions.split(','), Rare, (Caffenie == 'checked'), Description, Link)
                tea_list.append(next_tea)
                # print(', '.join(row))
        
        return tea_list

class TeaData:

    # tea_names = ["Test Name 1", "Test Name 2", "Test Name 3"]
    # tea_conditions = [["Cold", "Stuffy Nose"], ["Cancer"], ["Lyme Disease"]]
    # tea_imagenames = ["img1.png", "img2.png", "img3.png"]
    # tea_description = ["this is a test description for tea type 1", 
    #     "this is a test description for tea type 2", 
    #     "this is a test description for tea type 3"]
    # tea_caffeine = [True, False, True]

    feelings = ["any", "calming", "energy", "warm", "detox", "sleep", "cognition", "immune"]
    conditions = ["any", "inflammation", "high blood pressure", "high cholesterol", "autoimmune"]
    regions = ["any", "asia", "europe", "africa", "south america", "north america", "australia"]

    

    def __init__(self):

        # tea_list = import_tea()
        # print(tea_list)

        
        

        pass




