import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"


#This function prompts the user to input a file name to open and keeps prompting until a valid name is entered. Return the file pointer
def open_file():
    loop= True
    while loop == True: # here I made a loop so the user will be asked many times until they enter a valid file name
        try:
            promot= input("Enter file name: ")
            filename= promot 
            fp= open(filename,'r')# i opened the file in reading mode
            loop = False
        except FileNotFoundError: # I made an except if the file wasn't found an error message wil be printed and the user will be asked again
            print("\nError opening file. Please try again.")
    return fp



    
#This function reads the file using file pointer fp. The file has one header line.Then Create a list of tuples and each tuple represents a character and has the following format: (name, element, weapon, rarity, region)
def read_file(fp):
    reader = csv.reader(fp)
    next(reader,None) # i wrote this line so I can skip the first line
    list_of_tuples= []
    for line in reader: # I wrote this line so i will be able to get each tuple spreate 
        Name= line[0]
        Rarity= int(line[1])
        Element= line[2]
        Weapon= line[3]
        if line[4] >"": # I wrote this if statement so that if the there wasn't a region it will assign it to None but if there was one, it will assign Region to the region 
            Region= line[4]
        else:
            Region= None
        tup=(Name,Element,Weapon,Rarity,Region) # Here I made a tuple in the asked format and add it to a list in the next line
        list_of_tuples.append(tup)
    return list_of_tuples

#Given a list of character tuples, this function will retrieve the characters that match a certain criteria 
def get_characters_by_criterion (list_of_tuples, criteria, value):
   
    final_data= []
    
    if criteria == 3: # here I checked if the criteria was rarity meainging it's will be a number 
        for i in list_of_tuples:
            if value in i:
                final_data.append(i)
    else:# here this else statement is going to take strings 
        value = value.capitalize() # I wrote this line so only the first letter will be capital and all the other letters will be small so it can both matches with the file
        for i in list_of_tuples:
            if value in i:
                final_data.append(i)
    return final_data        

#This function takes as parameter the list of tuples returned by the read_file function master_list, an element, a weapon, and a rarity and returns a list of tuples filtered using those 3 criterias. This function looks similar to the


def get_characters_by_criteria(master_list, element, weapon, rarity):
    get_characters_by_criteria_filtred_list= []
    
    for i in master_list:
        element= element.capitalize() # I wrote this line and the next one  so only the first letter will be capital and all the other letters will be small so it can both matches with the file
        weapon= weapon.capitalize()
        
        if element in i and weapon in i and rarity in i: # here I checked if the function preamters are in the tuple and if so it will be added to the list
            get_characters_by_criteria_filtred_list.append(i)

    return get_characters_by_criteria_filtred_list

#This function will retrieve all available regions into a list 
def get_region_list(master_list):
    region_list= []
    for i in master_list:
        if i[-1] not in region_list and i[-1] != None:# here I made sure that when I used the loop the regiom wouldn't be added again if it already added and at the same time the value is not None
            region_list.append(i[-1])
        sorted_refion_list= sorted(region_list)
    return sorted_refion_list

        
    pass
#this function will create a new list where character tuples have been sorted. The order of sorting is by decreasing rarity and alphabetically by name. it will first sort it alphabetically on names, and then sort again by rarity


def sort_characters (list_of_tuples):
    sorted_characters_list= sorted(list_of_tuples) #get the list sorted alphabetically
    sorted_characters_list_by_rarity= sorted(sorted_characters_list,key=itemgetter(3),reverse= True) #get the list sorted rarity
    return sorted_characters_list_by_rarity
    pass

#display the characters along with their information, using the given formats
def display_characters (list_of_tuples):
    
    if not list_of_tuples:# if the list was empty print a message will be printed
        print("\nNothing to print.")
        
        
    else:#the header will be printed along with the list of characters with their criteria
        print("\n{:20s}{:10s}{:10s}{:<10s}{:25s}".format("Character","Element","Weapon","Rarity","Region"))
        for i in list_of_tuples:
            if i[-1]== None:
                print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(i[0],i[1],i[2],i[3],"N/A"))
            else:
                print("{:20s}{:10s}{:10s}{:<10d}{:25s}".format(i[0],i[1],i[2],i[3],i[4]))
    
#Display a menu of options and prompt for input 
def get_option():
    #yhe menue message
    promot= int(input("\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "))
    if promot != 1 and promot != 2 and promot != 3 and promot != 4: # if the promot wasn't any of the number of the given choices, it will print an invalid message
        print("\nInvalid input")
    return promot

#the main function will combine every function above with some adjustment
def main():
    fp= open_file()# I wrote this line so I can open the file
    file_reader_variable= read_file(fp)
    promot_value= get_option()
    while promot_value != 4:# here I created a loop that will continue until the user enter number 4
        if promot_value ==1:# this choice will use the region function that was created above and print all the avaliable regions comma sparated 
            print("\nRegions:")
            region_list_for_main_function= get_region_list(file_reader_variable)
            regions= ", ".join(region_list_for_main_function)
            print(regions)
        elif promot_value ==2:
            criteria_value= int(input(CRITERIA_INPUT))# here I made the criteria_value integer
            loop= True
            while loop == True:

                if criteria_value >=1 and criteria_value <=4:#here I made sure that the criteria_value is between 4 and 1 inclusive
                    value_value= input(VALUE_INPUT)

                    if criteria_value == 3:
                        if value_value.isdigit(): # here I made sure that the value is digit number and not a string or any other type, if the value was not an integer, a statement will be printed
                            value_value=int(value_value)

                            characters= get_characters_by_criterion(file_reader_variable,criteria_value,value_value) # here I used the function I previously created

                            sort_characters_value =sort_characters(characters)
                            display_characters(sort_characters(sort_characters_value))
                            loop= False
                            
                        else:# this is going to print a statment in case the value was not integer
                            print(INVALID_INPUT)
                            
                    else:# this condition will be functioned if the criteria_value was not rarity and will use many of the function I previously wrote as it has been asked in the document
                        characters= get_characters_by_criterion(file_reader_variable,criteria_value,value_value)

                        sort_characters_value =sort_characters(characters)
                        display_characters(sort_characters_value)
                        loop= False
                else:
                    print(INVALID_INPUT)
                    criteria= int(input(CRITERIA_INPUT))
        elif promot_value == 3: # this option will prompt in this order for element, weapon, rarity and filter the characters using these criterias and sort them and thenfinally displayit
            element_INPUT= input(ELEMENT_INPUT)
            weapon_INPUT= input(WEAPON_INPUT)   
            rarity_INPUT= input(RARITY_INPUT)
            loop= True
            while loop == True:
                if rarity_INPUT.isdigit(): # here I checked if the rarity input was integer or invalid
                    rarity_INPUT= int(rarity_INPUT)
                    characters= get_characters_by_criteria(file_reader_variable,element_INPUT,weapon_INPUT,rarity_INPUT)
                    sort_characters_value =sort_characters(characters)
                    display_characters(sort_characters_value)
                    loop = False

                else:# this condion will be printed if the rarity input is invalid
                    print(INVALID_INPUT)
                    rarity_INPUT= input(RARITY_INPUT)    
                    

        
        promot_value= get_option()
    fp.close()# here I made sure I closed the file

# DO NOT CHANGE THESE TWO LINES
#These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()
    
