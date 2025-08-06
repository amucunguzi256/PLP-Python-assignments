try:
    file_name= input("Please input file name ending with .txt: ").strip()
    with open("alice.txt", "r") as rf:
        contents=rf.read()
        if file_name.endswith(".txt"): 
            with open(file_name, "w") as wf:
                new_text= input("Please write what you want to add to the document: ")
                wf.write(contents + "\n" + new_text)
                print(f"\n Content successfully added to {file_name}")
        else:
            print("Please enter a file name that ends with .txt")
except FileNotFoundError:
    print("File not found")

    