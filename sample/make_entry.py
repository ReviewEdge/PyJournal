import config
import datetime
import os
from furtherpy.sample import date_conv_tool
from furtherpy.sample import files_tool

# Sets my_path using the project path provided in config
my_path = config.my_project_path

# Creates a line spacer
line_spacer = "\n------------------------\n"

journal_entry = input("Journal Entry:\n")

# Adds time stamp to journal entry
journal_entry = date_conv_tool.get_readable_full_month() + "\n\n" + journal_entry

print("Your journal entry:\n" + line_spacer + journal_entry + line_spacer)

answer = input("Confirm? ('y' or 'n')\n").lower()

if answer == "y":
    now = datetime.datetime.now()

    # Finds what number entry you are creating by checking the memory
    current_entry_number = files_tool.basic_read_file(my_path + "/mem/entry_number.txt")

    # Makes an entry number memory if one does not exist
    if current_entry_number == "FILE NOT FOUND":
        new_path = my_path + "/mem"
        os.mkdir(new_path)
        files_tool.basic_write_file(my_path + "/mem/entry_number.txt", "1")
        current_entry_number = "1"

    # Increments entry_number for next time and saves it to memory
    next_entry_number = str(int(current_entry_number) + 1)
    files_tool.basic_write_file(my_path + "/mem/entry_number.txt", next_entry_number)

    entry_file_name = my_path + "/entries/" + current_entry_number + " " + now.strftime("%m-%d-%Y") + ".txt"

    # Creates new entries directory if it does not exist
    if not os.path.isdir(my_path + "/entries"):
        entries_new_path = my_path + "/entries"
        os.mkdir(entries_new_path)

    # Creates entry file
    files_tool.basic_write_file(entry_file_name, journal_entry)
