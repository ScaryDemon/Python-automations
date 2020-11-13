import os
import time

project_destination = "/Users/MelRaeven/Documents/GIT"
print("What is the project name")
project_name = input()
if project_name == "":
    print("No name was given... exiting program...")

else:
    final_destination = project_destination + "/" + project_name
    os.makedirs(final_destination)
    os.chdir(final_destination)
    print("select project type:")
    print(" 1: reactJS \n 2: vueJS \n 3: python \n 4: none")
    project_type = input()
    if project_type == "1":
        print("create a python backend? \ny/n")
        back_end_builder = input()
        if back_end_builder == "y":
            os.popen('mkdir backend')
            time.sleep(2)
            os.chdir('backend')
            os.popen('touch main.py')
            print("created backend succesfully")
            time.sleep(2)
            print("building frontend...")
            os.popen('npx create-react-app frontend')
            print("succesfully created project!")
        elif back_end_builder == "n":
            os.popen('npx create-react-app frontend')
            print("succesfully created project!")
        else:
            print("no valid option given... exiting program...")
    
    elif project_type == "2":
        print("create a python backend? \ny/n")
        back_end_builder = input()
        if back_end_builder == "y":
            os.popen('mkdir backEnd')
            time.sleep(2)
            os.chdir('backend')
            os.popen('touch main.py')
            print("created backend succesfully")
            time.sleep(2)
            print("building frontend...")
            os.popen('vue ui')
            print("succesfully created project!")
        elif back_end_builder == "n":
            os.popen('vue ui')
            print("succesfully created project!")
        else:
            print("no valid option given... exiting program...")
    
    elif project_type == "3":
        os.popen('virtualenv venv')
        print("don't forget to activate the source!")
        print("succesfully created project!")

    elif project_type == "4":
        print("succesfully created project!")
    