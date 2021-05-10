import os.path
from os import path
from os import listdir
from os.path import isdir, join

def get_folders():
    output = str
    while True:
        master_path = input("plz enter directory: ")
        if(path.exists(master_path)):

            output_files = list()
            # only collects folders
            for file in listdir(master_path):
                if(isdir(join(master_path, file))):
                    output_files.append(join(master_path, file))
            return output_files
        else:
            print("directory not found")

def convert_ram_to_text(folder, file):
    directory = join(folder, file)
    operaten = ["take", "add", "sub", "save", "jmp", "tst", "inc", "dec", "null", "hlt"]
    text = list()
    pointer = 0
    with open(directory, "r") as f:
        text.append(os.path.basename(folder) + "_" + os.path.splitext(file)[0])
        for i, line in enumerate(f, 1):
            stripped_line = line.strip()
            op = stripped_line[:len(stripped_line)-3]

            try:
                if int(op)<=len(operaten):
                    text.append(format(i, '03d')+ " " + operaten[int(op)-1] + " " + stripped_line[len(stripped_line)-3:])
                    pointer = i
            except:
                if op=="":
                    if(stripped_line=="000"):
                        text.append(format(i, '03d')+ " 00 "+ "000")
                    else:
                        text.append(format(i, '03d')+ " 00 "+ stripped_line)
                        pointer = i

                else:
                    print("unvalid ram content")
                    text.append(format(i, '03d')+ " "+ op+ " "+ stripped_line[len(stripped_line)-3:])
                    pointer = i

    return text[:pointer]

def save_ram(folder):
    files = [f for f in listdir(folder) if f.endswith(".ram")]
    for file in files:

        with open(os.path.dirname(folder)+"/"+ os.path.basename(folder) + "_" + os.path.splitext(file)[0] + ".txt", "w") as f:
            print("saved in: " + os.path.dirname(folder)+"/"+ os.path.basename(folder) + " " + file)
            a = convert_ram_to_text(folder, file)
            f.writelines("%s\n" % line for line in a)
    

if  __name__ == "__main__":

    folders = get_folders()
    for folder in folders:
        save_ram(folder)
    print("finished")