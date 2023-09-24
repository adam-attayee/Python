##Take list of names from invited_names.txt
##Replace [name] from letter template with the name from the invited_names file.
##Create a new .txt for each person and save it as: letter_for_[name]

with open("input/Names/invited_names.txt") as name_file:
    names_list = name_file.readlines()
    for i in range(len(names_list)):
        names_list[i] = names_list[i].strip()

with open("input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()

    for name in names_list:
        new_letter = letter_template.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
            file.write(new_letter)
