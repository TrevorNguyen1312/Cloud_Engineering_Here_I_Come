languages = ['Spanish', 'English', 'Russian', 'Chinese']

for language, num in enumerate(languages):
    print(f'Index {num} and language {language}')

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')