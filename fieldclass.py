from piececlass import piece
from random import randint
from time import sleep
import curses
class field:

    def __init__ (self, height, width, scrn):
        self.scrn = scrn

        self.h = height
        self.w = width

        self.unit = 1
        self.calcUnit()


        self.field = []
        self.collision = False




        for n in range( height + 1):
            row = []
            for n in range( width + 1):
                row += 'O'
            self.field.append(row)


        self.p = piece(randint(0, 6))
        self.p.x = int(self.w / 2 - len(self.p.piece) / 2)
        self.mapPiece('X')

        self.pnext = piece(randint(0, 6))



    #Draws the next piece, score and level
    def drawNext(self, score, level):

        startx = (self.w * self.unit + self.unit) * 2 + 3;
        starty = int(self.h / 2 * self.unit)

        scorestr = "Score: %i" % (score)
        lvlstr = "Level: %i" % (level)


        try:
            self.scrn.addch(starty - 4, startx - 1, curses.ACS_ULCORNER)
            self.scrn.addch(starty - 4, startx + len(scorestr), curses.ACS_URCORNER)
            self.scrn.addch(starty - 1, startx - 1, curses.ACS_LLCORNER)
            self.scrn.addch(starty - 1, startx + len(scorestr), curses.ACS_LRCORNER)
            self.scrn.addstr(starty - 3, startx, scorestr)
            self.scrn.addstr(starty - 2, startx, lvlstr)
        except:
            pass

        for y in range(5):
            for x in range(5):
                self.scrn.addstr(starty + y, startx + x * 2, '  ')

        for y in range(len(self.pnext.piece)):
            for x in range(len(self.pnext.piece[0])):
                if self.pnext.piece[y][x] != 0:
                    self.scrn.addstr(starty + y, startx + x * 2, '  ', curses.A_STANDOUT)

        self.scrn.addch(starty, startx - 1, curses.ACS_ULCORNER)
        self.scrn.addch(starty, startx + 2 * len(self.pnext.piece[0]), curses.ACS_URCORNER)
        self.scrn.addch(starty + 3, startx - 1, curses.ACS_LLCORNER)
        self.scrn.addch(starty + 3, startx + 2 * len(self.pnext.piece[0]), curses.ACS_LRCORNER)




    def calcUnit(self):
        height, width = self.scrn.getmaxyx()
        #I substract one from the width to leave room for the seperator (the line of pipe symbols between the playingfield and the next piece) and add one to the width to have room to display the next piece
        #Width is how many characters fit on the screen
        #self.w is the width of the playing field in cells
        widthCell = (width / 2 - 1)/ (self.w + 1)
        heightCell = height / self.h

        if widthCell < heightCell:
            self.unit = int(widthCell)
        else:
            self.unit = int(heightCell)


    # A function to draw a tile
    def drawTile(self, x, y, mode):
        emptStr = ''
        for n in range(self.unit):
            emptStr += '  '
        #Empty
        if mode == -1:
            for n in range(self.unit):
                self.scrn.addstr(y * self.unit + n, self.unit * x * 2, emptStr)
        #White
        elif mode == 0:
            for n in range(self.unit):
                self.scrn.addstr(y * self.unit + n, self.unit * x * 2, emptStr, curses.A_STANDOUT)

    def drawField(self):
        #The first line is only for fixing rotating (rotate to outside of the screen).
        #It should not be drawn
        self.scrn.clear()
        for y in range(1, self.h + 1):
            for x in range(self.w + 1):
                self.drawTile(x, y, -int(self.field[y][x] == 'O'))
            sleep(0.002)

        height, width = self.scrn.getmaxyx()
        for n in range((self.h + 1) * self.unit):
            self.scrn.addch(n, 2 * self.w * self.unit + self.unit * 2, curses.ACS_VLINE)
        for n in range(2 * ((self.w + 1) * self.unit)):
            self.scrn.addch((self.h + 1) * self.unit, n, curses.ACS_HLINE)

        self.scrn.addch((self.h + 1) * self.unit,\
                2*((self.w + 1) * self.unit),\
                curses.ACS_LRCORNER)


    def spawnPiece(self):
        self.mapPiece('T')
        self.p = self.pnext
        self.pnext = piece(randint(0, 6))
        self.p.x = int(self.w / 2 - len(self.p.piece) / 2)
        if self.checkPieceCollision():
            self.mapPiece('T')
            self.collision = True
        self.scrn.refresh()

    def mapPiece(self, letter):
        for y in range(len(self.p.piece)):
            for x in range(len(self.p.piece[y])):
                if self.p.piece[y][x] != 0:
                    self.drawTile(self.p.x + x, self.p.y + y, -int(letter == 'O'))
                    self.field[self.p.y + y][self.p.x + x] = letter

    def checkPieceCollision(self):
        for y in range(len(self.p.piece)):
            for x in range(len(self.p.piece[y])):
                if self.p.piece[y][x] != 0:
                    if self.p.x + x > self.w or self.p.y + y > self.h or self.p.x + x < 0:
                        return True
                    if  self.field[self.p.y + y][self.p.x + x] != 'X'\
                            and self.field[self.p.y + y][self.p.x + x] != 'O':
                        return True
        return False

    def moveX(self, x):
        self.p.x += x
        if self.checkPieceCollision():
            self.p.x -= x
            return
        self.p.x -= x
        self.mapPiece('O')
        self.p.x += x
        self.mapPiece('X')

    def checkTetris(self):
        lines = 0
        for row in list(reversed(self.field)):
            remRow = True
            for letter in row:
                if letter != 'T':
                    remRow = False
                    break
            if remRow:
                lines += 1
                self.field.remove(row)

        for n in range(lines):
            row = [[]]
            for n in range(0, self.w + 1):
                row[0].append('O')
            self.field = row + self.field
        return lines

    def moveDown(self):
        self.p.y += 1
        if self.checkPieceCollision():
            self.p.y -= 1
            self.spawnPiece()
            return True
        self.p.y -= 1
        self.mapPiece('O')
        self.p.y += 1
        self.mapPiece('X')
        return False

    def rotateClock(self):
        self.p.nextMode()
        if self.checkPieceCollision():
            self.p.prevMode()
            return
        self.p.prevMode()
        self.mapPiece('O')
        self.p.nextMode()
        self.mapPiece('X')

    def rotateCounter(self):
        self.p.prevMode()
        if self.checkPieceCollision():
            self.p.nextMode()
            return
        self.p.nextMode()
        self.mapPiece('O')
        self.p.prevMode()
        self.mapPiece('X')

    def writeFieldToLog(self):
        f = open('log', 'a')
        for item in self.field:
            f.write('\n')
            f.write(str(item))
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.close()

    def hardDrop(self):
        while not self.moveDown():
            continue
