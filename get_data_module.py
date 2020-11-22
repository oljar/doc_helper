import os

def get_data() :
    file = "dane.txt"  # pobieranie tekstu label
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file)
    LabList = open(my_file, "r", encoding="utf-8").read()
    word = str()
    wordList = []


    for a in (LabList):

       if a == ';':
           wordList.append(word)
           word=''
           continue
       word += a

    return (wordList)

if __name__ =='__main__':

    for i in get_data():
        print(i)





