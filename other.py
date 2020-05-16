helpMsg = """
    Tetris in your terminal.

OPTIONS:
	-h: Help.
	-f n: Sets the framerate of the game to n (must be greater than 60).
	-x: Disables next piece preview.
	-l n: Sets the starting level (default is 5. Anything above or equal to 27 has the same dropping speed.)

KEY BINDINGS:
	w: rotate clockwise
	s: rotate counterclockwise
	a: move left
	b: move right
	j: drop
        ESC: exit
        """


def printHelpMsg():
    print(helpMsg)

