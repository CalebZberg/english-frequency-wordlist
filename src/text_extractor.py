def clean_word(word: str) -> list[str]:
    if not word:
        return None
    
    words = []
    i = 0
    n = len(word)

    while i < n:
        while i < n and not word[i].isalpha():
            i += 1
        start = i
        while i < n and (word[i].isalpha() or word[i] == "'"):
            i += 1
        if i > start:
            token = word[start:i].replace("'", "")
            if token:
                words.append(token.upper())
    return words


def main():
    #pathway = input("Enter .txt file pathway: ")
    pathway = r"C:\Users\Caleb\Desktop\.txt Files\Athens_ Its_Rise_And_Fall.txt"

    words_dict = {}

    with open(pathway, 'r') as f:
        for line in f:
            for word in line.split():
                words = clean_word(word)
                for word in words:
                    if word in words_dict:
                        words_dict[word] += 1
                    else:
                        words_dict[word] = 1


    total_count = 0
    for word in words_dict:
        print(f'{word}: {words_dict[word]}')
        total_count += words_dict[word]
    print(len(words_dict), " words")
    print("Total count: ", total_count)


if __name__ == "__main__":
    main()