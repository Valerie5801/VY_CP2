#VY 2nd Menu Actions for Word Counter

#this is where the functions that use other functions for their mechanics will be

#function for updating file path with parameter of the dictionary that holds all the file data:
def update_path(doc_info):
    #Ask the user for the specific file path
    new_path = input("\nPlease type the EXACT relative path for the file: ")
    #Replace the old file path in the dictionary with the new one
    doc_info[0]["Path"] = new_path
    #return the dictionary
    return doc_info

#function that shows the whole txt document to the user:
def show_doc():
    #try the following
    from pathlib import Path
    try:
        #open the txt document:
        doc_path = Path(__file__).parent / "example_doc.txt"
        with open(doc_path, "r") as document:
            #make a list named content
            content = []
            #for loop here:
            for line in document:
                content.append(line.strip())
                #for each line in the txt document, append it to content
    #except:
    except:
        print("document not found")
        #show that the txt document doesn't work
    #else statement:
    else:
        #loop through content:
        print("")
        for line in content:
            print(line)
            #print out each line

#function that lets the user add content to the document with parameter of the list that holds lines of the txt document in different values:
def add_content(doc_content):
    #Ask the user for what they want to add to the document, and tell them to press enter twice to stop editing (this allows the user to write on separate lines)
    print("\nEnter new content (press Enter twice when you're done.): ")
    # Read multiple lines until the user enters a blank line.
    # Collect only the newly added lines and update the in-memory `doc_content`.
    added_lines = []
    while True:
        line = input()
        if line == "":
            break
        # Keep `doc_content` as a list of lines without trailing newlines (consistent with save_doc())
        doc_content.append(line)
        added_lines.append(line)
    # Return only the new lines
    return added_lines