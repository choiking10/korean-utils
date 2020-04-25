
import os
from konlpy.tag import Kkma
from konlpy.utils import pprint
from konlpy.tag import Okt
import nltk

nltk.download('punkt')

nlpy = Okt()

for filename in os.listdir("test"):
    try:
        with open(os.path.join("test", filename), 'r', encoding="utf-8") as f:  # open in readonly mode
            print("file :" + filename)
            sentences = f.read()
            nouns = nlpy.morphs(sentences)
            counter = {}
            for noun in nouns:
                if noun not in counter:
                    counter[noun] = 1
                else:
                    counter[noun] += 1

            if len(counter) == 0:
                nouns_eng = nltk.word_tokenize(sentences)
                for noun in nouns_eng:
                    if noun not in counter:
                        counter[noun] = 1
                    else:
                        counter[noun] += 1

            sorter = [(value, key) for key, value in counter.items()]
            sorter.sort()
            sorter.reverse()
            pprint(sorter)
            with open(os.path.join('output', "count_nouns_" + filename), 'w', encoding="utf-8") as wf:
                for num, tag in sorter:
                    wf.write("{}, {}\n".format(tag, num))

    except Exception as e:
        print(filename + " cannot open \n\n" + str(e))
