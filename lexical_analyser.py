import sys


def main():
    result = {} # {str:int}
    if len(sys.argv) > 1:
        if sys.argv[1] == "help" or sys.argv[1] == "h":
            help()
            exit()
        file = sys.argv[1]
    else:
        print("Invalid Arguments")
        help()
        exit()
    with open(file) as f:
        contents = f.read()
        word = ""
        for char in contents:
            if not char.isspace(): # all words are seperated by whitespace or newline
                if not (char == "," or char == "."):
                    word += char.lower()
            else:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
                word = ""
    print(result)

def help():
    print("Simple lexical analyser tool that counts number of words in a given file and prints out the output as a python dictionary \nUsage: python lexical_analyser.py [FILENAME]")

main()