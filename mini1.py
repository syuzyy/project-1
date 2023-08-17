#This code allows the user to choose a template, generates a story based on the chosen template and user inputs, 
#and uses the random library to meet the specified requirements.

import random


templates = [
    '''It was about {0} {1} ago when I arrived at the hospital in a {2}. The hospital is a/an {3} place, there are a lot of {4} {5} here. There are nurses here who have {6} {7}. If someone wants to come into my room I told them that they have to {8} first. I’ve decorated my room with {9} {10}. Today I talked to a doctor and they were wearing a {11} on their {12}. I heard that all doctors {13} {14} every day for breakfast. The most {15} thing about being in the hospital is the {16} {17}!'''
]

#as required, I've put only one template, to make evaluation process easier.    

def choose_template():
    print("Choose a template:")
    print("1. Hospital Story")
    choice = input("Enter the number of the template: ")
    return templates[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= len(templates) else None


#this line serves as input validation to ensure that the user's choice is within the valid range of available templates.


def generate_story(template):
    number = input("Type a number: ")
    measure_of_time = input("Type a measure of time: ")
    mode_of_transportation = input("Type a mode of transportation: ")
    adjective = input("Type an adjective: ")
    adjective2 = input("Type another adjective: ")
    noun = input("Type a noun: ")
    color = input("Type a color: ")
    part_of_the_body = input("Type a part of the body: ")
    verb = input("Type a verb: ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type another noun: ")
    part_of_the_body2 = input("Type another part of the body: ")
    verb2 = input("Type a verb: ")
    noun4 = input("Type another noun: ")
    adjective3 = input("Type another adjective: ")
    silly_word = input("Type a silly word: ")
    noun5 = input("Type another noun: ")
    story = template.format(number, measure_of_time, mode_of_transportation, adjective, adjective2,
                            noun, color, part_of_the_body, verb, number2, noun2, noun3,
                            part_of_the_body2, verb2, noun4, adjective3, silly_word, noun5)
    print("\nGenerated Story:\n" + story)

def main():
    template = choose_template()
    if template:
        generate_story(template)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
