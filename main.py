from rich import print
from subprocess import call
import json
import os
import pyfiglet
import sys

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

def done():
    sys.exit()

def do_display(json_entry):
    print("\n"+("-"*(20+(len(json_entry['resource'])))))
    print("Resource Found! [link="+json_entry['resource-link']+"]"+json_entry['resource']+"[/link]")
    print("-"*(10+(len(json_entry['resource']))))
    print("Sourced at [link="+json_entry['grabbed-from-link']+"]"+json_entry['grabbed-from']+"[/link]")
    print("-"*(10+(len(json_entry['grabbed-from']))))
    print("Description:\n" + json_entry['description'])
    print("-"*(20+(len(json_entry['grabbed-from']))))

def do_intro():
    print(pyfiglet.figlet_format("OSINT-Tree"))
    print("A keyword-based search for referencing your favorite Cybersec tools!")
    print("Instruction: Type any 1-word based on what you remember.")

def do_search(str_search):
    with open("osint-tree.json", "r") as json_file:
        json_data = json.load(json_file)
        for json_entry in json_data:
            if str_search.lower() in json_entry['category-1'].lower() or str_search.lower() in json_entry['category-2'].lower() or str_search.lower() in json_entry['service-type'].lower() or str_search.lower() in json_entry['resource'].lower() or str_search.lower() in json_entry['grabbed-from'].lower() or str_search.lower() in json_entry['resource-link'].lower() or str_search.lower() in json_entry['grabbed-from-link'].lower() or str_search.lower() in json_entry['tags'].lower() or str_search.lower() in json_entry['compatibility'].lower() or str_search.lower() in json_entry['description'].lower():
                do_display(json_entry)
        json_file.close()

def main():
    while True:
        try:
            clear()
            do_intro()
            str_search = input("\nEnter your keyword (blank to exit): ")
            if str_search == "":
                done()
            do_search(str_search)
            input("\nPress enter to continue...")
        except:
            print("Goodbye.")
            done()

if __name__ == "__main__":
    main()
