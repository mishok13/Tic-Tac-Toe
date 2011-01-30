#!/usr/bin/python


"""The engine for the tic-tac-toe game"""


class Victory(Exception):
    pass


class Draw(Exception):
    pass


class Engine(object):

    values = {'X': 1, 'O': -1}

    def __init__(self):
        self.board = dict(((x, y), None) for x in xrange(3) for y in xrange(3))

    def move(self):
        """Make AI move"""
        # We're assuming that if everything's right, then
        # sum of
        if sum(self.board.itervalues()) == 1:
            value = 'O'
        else:
            value = 'X'
        value, coord = None, None
        self.mark(coord, value)

    def mark(self, coord, value):
        """Mark the coord and check for the winning position"""
        self.board[coord] = value
        self.check()

    def check(self):
        """Simple routine for checking if somebody has won"""
        for x in xrange(3):
            if abs(sum(self.board[(x, y)] for y in xrange(3))) == 3:
                raise Victory
        for y in xrange(3):
            if abs(sum(self.board[(x, y)] for x in xrange(3))) == 3:
                raise Victory
        # Now, check the diagonals
        if (abs(sum(self.board[(x, x)] for x in xrange(3))) == 3 or
            abs(sum(self.board[(x, 2 - x)] for x in xrange(3))) == 3):
            raise Victory
        if None not in self.board.values():
            raise Draw
