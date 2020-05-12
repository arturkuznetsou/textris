


#Returns the frames per move for each level
#Based on NES
#https://tetris.fandom.com/wiki/Tetris_(NES,_Nintendo)

def speed(level):
    lvlarrsub10 = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6]
    if level < 10:
        return lvlarrsub10[level]
    elif level < 12:
        return 5
    elif level < 15:
        return 4
    elif level < 18:
        return 3
    elif level < 28:
        return 2
    else:
        return 1

#Returns lines until next move
#Based on NES Tetris
#https://tetris.fandom.com/wiki/Tetris_(NES,_Nintendo)

def calcScore(lines, level):
    if lines == 1:
        return (level + 1) * 40
    if lines == 2:
        return (level + 1) * 100
    if lines == 3:
        return (level + 1) * 300
    if lines == 4:
        return (level + 1) * 1200

    return 0

def linesNextLevel(level):
    lines_until_next_level = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100, 100, 100, 100, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 200, 200, 200]

    if level >= len (lines_until_next_level):
        return -1

    return lines_until_next_level[level]


pieceIndex = ['o', 't', 'j', 'l', 's', 'z', 'i']


opiece = [
        [[0,0],
        [1,1],
        [1,1]]
        ]

tpiece = [
        [[0,0,0],
        [2,2,2],
        [0,2,0]],

        [[0,2,0],
        [2,2,0],
        [0,2,0]],

        [[0,0,0],
        [0,2,0],
        [2,2,2]],

        [[0,2,0],
        [0,2,2],
        [0,2,0]]
        ]

jpiece = [
        [[0,0,0],
        [3,3,3],
        [0,0,3]],

        [[0,3,0],
        [0,3,0],
        [3,3,0]],

        [[0,0,0],
        [3,0,0],
        [3,3,3]],

        [[0,3,3],
        [0,3,0],
        [0,3,0]]
        ]

lpiece = [
        [[0,0,0],
        [4,4,4],
        [4,0,0]],

        [[4,4,0],
        [0,4,0],
        [0,4,0]],

        [[0,0,0],
        [0,0,4],
        [4,4,4]],

        [[0,4,0],
        [0,4,0],
        [0,4,4]]
        ]

spiece = [
        [[0,0,0],
        [0,5,5],
        [5,5,0]],

        [[5,0,0],
        [5,5,0],
        [0,5,0]]
        ]
zpiece = [
        [[0,0,0],
        [6,6,0],
        [0,6,6]],

        [[0,0,6],
        [0,6,6],
        [0,6,0]],
        ]

ipiece = [
        [[0,0,0,0],
        [7,7,7,7],
        [0,0,0,0],
        [0,0,0,0]],

        [[0,0,7,0],
        [0,0,7,0],
        [0,0,7,0],
        [0,0,7,0]]
        ]

pieces = [opiece, tpiece, jpiece, lpiece, spiece, zpiece, ipiece]
