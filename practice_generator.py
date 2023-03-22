def file_read():
    with open('words.txt', 'r', encoding='utf-8') as file:
        while True:
            word = file.readline()
            if word == '':
                break
            yield word.strip('\n')

for i in file_read():
    print(i)