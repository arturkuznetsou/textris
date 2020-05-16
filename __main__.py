import curses, time, sys, getopt, other
from threading import Thread
from fieldclass import field
from tetmacros import speed, linesNextLevel, calcScore

SHOW_NEXT = True
START_LEVEL = 5



args, opts = getopt.getopt(sys.argv[1:], 'hxl:f:')

if opts != []:
    sys.exit('Unknown option \'%s\'. Exiting.' % (opts[0]))
for arg, value in args:
    if arg == '-l':
        if value == '':
            print('-l starting level')
            sys.exit(-1)
        START_LEVEL = int(value)
    elif arg == '-f':
        if value == '':
            sys.exit('-l framerate')
        if int(value) < 60:
            sys.exit('Framerate has to be equal to or greater than 60.')
        FPS = int(value)
    elif arg == '-x':
        SHOW_NEXT = False
    elif arg == '-h':
        other.printHelpMsg()
        sys.exit(1)

DROP_FAC = 0
FPS = 240
level = START_LEVEL
score = 0
linesNext = linesNextLevel(level)
spd = int(speed(level) * FPS/60)


scr = curses.initscr(); curses.noecho(); curses.cbreak(); scr.refresh(); curses.curs_set(0); scr.nodelay(1); scr.timeout(0); scr.clear()
fld = field(20, 9, scr)


def checkLines():
    global score
    global level
    global linesNext
    global FPS
    global spd
    lines = fld.checkTetris()
    if lines != 0:
        score += calcScore(lines, level)
        linesNext -= lines
        if linesNext < 1:
            level += 1
            spd = int(speed(level) * FPS/60)
            linesNext = linesNextLevel(level) + linesNext
        fld.drawField()


def keyPress(delay, scrn):
    global score
    global level
    global linesNext
    global FPS
    global spd
    while not fld.collision:
        c = scr.getch()
        if c == ord('a'):
            fld.moveX(-1)
        elif c == ord('j'):
            fld.hardDrop()
            fld.drawNext(score, level)
            checkLines()
            scr.refresh()
        elif c == ord('d'):
            fld.moveX(1)
        elif c == ord('w'):
            fld.rotateClock()
        elif c == ord('s'):
            fld.rotateCounter()
        elif c == curses.KEY_RESIZE:
            fld.calcUnit()
            fld.drawField()
            fld.drawNext(score, level)
        elif c == 27:
            fld.collision = True
        time.sleep(delay)

def gameFunc():
    global score
    global level
    global linesNext
    global FPS
    frames = 0
    fld.drawField()
    fld.drawNext(score, level)

    while not fld.collision:
        frames += 1
        startTime = time.time()


        if frames % spd == 0:
            framesToSleep = 10 + fld.p.y / 2
            if fld.moveDown():
                checkLines()
                fld.drawNext(score, level)
                scr.refresh()

        time.sleep(max(1./FPS - (time.time() - startTime), 0))

keyThread = Thread(target = keyPress, args = (1/120, scr))
gameThread = Thread(target = gameFunc)

keyThread.start()
gameThread.start()
keyThread.join()
gameThread.join()

curses.nocbreak(); scr.keypad(0); curses.echo(); curses.endwin()

