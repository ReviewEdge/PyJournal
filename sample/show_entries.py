import config
from furtherpy.sample import files_tool
import os

# Sets my_path using the project path provided in config
my_path = config.my_project_path

# Creates a line spacer
line_spacer = "\n------------------------\n"

# Gets a list of all entries from the entries directory
entries_list = os.listdir(my_path + "/entries")

# Creates dictionary to hold entries
entries_dict = {}
# Fills dictionary with entry ids paired with entry file names
for entry in entries_list:
    # Removes .txt from file name
    entry = entry[:-4]

    # Finds entry id number
    id_loc = entry.find(" ")
    entry_id = int(entry[:id_loc])

    # Adds entry to dictionary
    entries_dict[entry_id] = entry


print("\nJOURNAL ENTRIES:\n")


# Lists file names of all entries, in order of file id
amount_of_keys_found = 0
key_value_being_checked = 1
while amount_of_keys_found < len(entries_dict):
    if key_value_being_checked in entries_dict:
        print(entries_dict[key_value_being_checked])
        amount_of_keys_found += 1
    key_value_being_checked += 1


# Allows user to choose an entry id
chosen_entry_id = int(input(line_spacer + "Enter an entry-number to choose a journal entry to view.\n"))

# Opens entry
chosen_entry_file = my_path + "/entries/" + entries_dict[chosen_entry_id] + ".txt"

# Prints journal entry text
print("\nEntry #" + str(chosen_entry_id) + ":" + line_spacer + files_tool.basic_read_file(chosen_entry_file) + line_spacer)
