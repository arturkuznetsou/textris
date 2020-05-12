import tetmacros

class piece:

    def __init__(self, pieceType):
        self.macro = tetmacros.pieces[pieceType]
        self.piece = self.macro[0]
        self.x = 0
        self.y = 0
        self.pieceMode = 0

    def prevMode(self):
        if self.pieceMode > 0:
            self.pieceMode -= 1
        else:
            self.pieceMode = len(self.macro) - 1
        self.piece = self.macro[self.pieceMode]

    def nextMode(self):
        if self.pieceMode < len(self.macro) - 1:
            self.pieceMode += 1
        else:
            self.pieceMode = 0
        self.piece = self.macro[self.pieceMode]
