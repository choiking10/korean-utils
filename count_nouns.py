
import os
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Okt

nlpy = Okt()

for filename in os.listdir("test"):
    try:
        with open(os.path.join("test", filename), 'r', encoding="utf-8") as f:  # open in readonly mode
            print("file :" + filename)
            sentences = f.read()
            nouns = nlpy.nouns(sentences)
            counter = {}
            for noun in nouns:
                if noun not in counter:
                    counter[noun] = 1
                else:
                    counter[noun] += 1
            sorter = [(value, key) for key, value in counter.items()]
            sorter.sort()
            sorter.reverse()
            pprint(sorter)
    except Exception as e:
        print(filename + " cannot open\n\n")
