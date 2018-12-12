#All of this was provided in A3 Chatbots

def is_question(input_string):
    for char in input_string:
        if char== '?':
            output = True
        else: 
            output = False
    return output

#removes all punctuation from the input string

def remove_punctuation(input_string):
    out_string= ''
    for word in input_string:
        if not word in string.punctuation:
            out_string += word
    return out_string

#creates list from words in input_string

def prepare_text(input_string):
    temp_string = str.lower(input_string)
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

#This was altered so that we return a specific output determined in the main_chat function

def selector(input_list, check_list, attribute_reply):
    output = None
    for char in input_list:
        if char in check_list:
            output = attribute_reply
            break
    return output


def list_to_string(input_list, separator):
    output = input_list[0]
    for word in input_list[1:]:
        output = string_concatenator(output,word,separator)
    return output

def string_concatenator(string1, string2, separator):
    output = string1 + separator + string2
    return output


#I edited this a little to loop through a list instead of checking a single word
def end_chat(input_list):
    possible = ['quit', 'exit', 'bye', 'finished', 'peace']
    
    for word in possible:
        if word in input_list:
            return True
        else: 
            return False

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


###############################################
## The following are functions I created
###############################################

def greeting_1():
    
    """ First opener for the chatbot """
    
    
    output_1=input("           Welcome, my name is Peanut\n\nWould you like to learn about endangered animals?\n\n                 Yes or No\n")
    output_1 = output_1.lower()
    possible_outputs = ['yes','y', 'okay','yeah']
    
    if output_1 in possible_outputs:
        
        print("\n")
        print_menu()  
        menu_interest = input()
        return menu_interest
    
    elif output_1 == 'no':
        
        print('Come back again then.')
        return False
    
    else:
        
        print("Answer Yes or No, please!")

def print_menu():
    
    """Print the main menu"""
    
    animal_menu = ["1. Mammals", "2. Reptiles", "3. Birds", "4. Leave"]
    print("Please choose a number for your category of interest:\n")
    
    for animal in animal_menu:
        
        print(animal)

#for a specific animal category
def print_menu2(animal_choice): 
    
    """Print the second menu for specific animal category"""
    
    index = 1
    
    for animal in animal_choice:


def menu_eval(interest_1):
    
    if interest_1 == "1" or interest_1 == "one": #mammals
            
        choice = mammals
        print("Do you want to learn about ocean and land mammals?")
        return mammals
            
    elif interest_1 == "2" or interest_1 == "two":
            
        choice = reptiles
        print("Do you want to learn about reptiles?")
        return choice
    
    elif interest_1 == "3" or interest_1 == "three":
            
        choice = birds
        print("Do you want to learn about the birds?") 
        return choice
    
    elif interest_1 == '4' or interest_1 == 'four':
        print('Thanks for stopping by!')
        chat = False
        
        index = str(index)
        print(index + '. ' + animal.name)
        index = int(index) + 1
     


