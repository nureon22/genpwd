import json, re
from requests import request

WORDLISTS = {
    "names": [
        "https://github.com/danielmiessler/SecLists/raw/refs/heads/master/Usernames/Names/names.txt"
    ],
    "words": [
        "https://github.com/danielmiessler/SecLists/raw/refs/heads/master/Miscellaneous/Words/EFF-Dice/large_words.txt",
        "https://github.com/danielmiessler/SecLists/raw/refs/heads/master/Miscellaneous/Words/EFF-Dice/small_1_words.txt",
        "https://github.com/danielmiessler/SecLists/raw/refs/heads/master/Miscellaneous/Words/EFF-Dice/small_2_words.txt",
    ],
}

for category in WORDLISTS:
    sources = WORDLISTS[category]
    words: list[str] = []
    regx = r'^[A-Za-z]+$'


    for source in sources:
        res = request("GET", source, stream=True)

        for word in res.iter_lines():
            if not word: continue

            word = word.decode('utf-8')

            if re.match(regx, word):
                words.append(word)

    print("Got {} entries for {}".format(len(words), category))

    with open(f"wordlist/{category}.json", "w") as f:
        f.write(json.dumps(words))
        f.close()