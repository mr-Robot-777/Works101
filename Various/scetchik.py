numBlocks = int(input('Сколько блоков звезд вам нужно? '))
numLines = int(input('Сколько строк в каждом блоке? '))
numStars = int(input('Сколько звезд в строке? '))
for block in range(0, numBlocks):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print ('*'),
    print()
print()
