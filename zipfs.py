import string
import numpy as np
import requests
from matplotlib import pyplot as plt


def load_file(url,file_name):
    r = requests.get(url,allow_redirects=True)
    open(file_name,'wb').write(r.content)
    document_text = open(file_name,'r')
    # Read the text from the file
    text_string = document_text.read().lower()
    return text_string

def word_freq(text_string):
    words = []
    occurances = []
    character_list = list(set(text_string))
    list_for_removal = [c for c in character_list if not c.isalpha()]
    text_no_punc = text_string.translate(
        str.maketrans('', '', string.punctuation))

    for character in text_no_punc:
        if character in list_for_removal:
            text_no_punc = text_no_punc.replace(character, " ")

    frequency = {}
    for word in text_no_punc.split():
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    word_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    for word in word_frequency:
        words.append(word[0])
        occurances.append(word[1])

    return occurances


def main(url, file_name):
    text_st = load_file(url, file_name)
    frequency = word_freq(text_st)
    return frequency

freq = main('https://www.gutenberg.org/files/2600/2600-0.txt', 'warandpeace.txt')
freq_1 = main('https://www.gutenberg.org/files/65709/65709-0.txt', 'thehouseofthesecret.txt')
freq_2 = main('https://www.gutenberg.org/files/65707/65707-0.txt', 'thecrimeofcasteinourcountry.txt')
freq_3 = main('https://www.gutenberg.org/files/65703/65703-0.txt', 'follasnovas.txt')



rank_list = [np.log(i) for i in list(range(len(freq)))]
freq_list = [np.log(i) for i in freq]
rank_list_1 = [np.log(i) for i in list(range(len(freq_1)))]
freq_list_1 = [np.log(i) for i in freq_1]
rank_list_2 = [np.log(i) for i in list(range(len(freq_2)))]
freq_list_2 = [np.log(i) for i in freq_2]
rank_list_3 = [np.log(i) for i in list(range(len(freq_3)))]
freq_list_3 = [np.log(i) for i in freq_3]


#PLOT OF ZIPF'S LAW FOR THE GIVEN BOOK
plt.figure(2)
plt.subplot(2,2,1)
plt.plot(rank_list, freq_list, label="war and peace")
plt.xlabel('Rank')
plt.ylabel('Freq')
plt.legend()

plt.subplot(2,2,2)
plt.plot(rank_list_1, freq_list_1, label="the house of the secret")
plt.xlabel('Rank')
plt.ylabel('Freq')
plt.legend()

plt.subplot(2,2,3)
plt.plot(rank_list_2, freq_list_2, label="the crime of caste in our country")
plt.xlabel('Rank')
plt.ylabel('Freq')
plt.legend()

plt.subplot(2,2,4)
plt.plot(rank_list_3, freq_list_3, label="follas novas")
plt.xlabel('Rank')
plt.ylabel('Freq')
plt.legend()

plt.suptitle("ZIPF'S LAW")
plt.show()