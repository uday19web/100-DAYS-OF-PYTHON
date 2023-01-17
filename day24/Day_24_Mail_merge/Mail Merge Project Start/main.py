PLACE_HOLDER = '[name]'

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode='r') as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as email:
    content = email.read()
    for guest in name_list:
        strip_name = guest.strip()
        with open(f"./Output/ReadyToSend/invited_{strip_name}.txt", mode='w') as names:
            # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
            names.write(content.replace(PLACE_HOLDER, strip_name))
