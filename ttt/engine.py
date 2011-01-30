#!/usr/bin/python


"""The engine for the tic-tac-toe game"""


import random


class Victory(Exception):
    pass


class Draw(Exception):
    pass


EMPTY = 0
CROSS = 1
DRAUGHT = -1


class Engine(object):

    values = {'X': 1, 'O': -1}

    def __init__(self):
        self.board = dict(((x, y), EMPTY) for x in xrange(3) for y in xrange(3))

    @property
    def current_mark(self):
        # We're assuming that if everything's right, then
        # sum of all values should be 0 or 1, where
        # 0 would mean that it's crosses move
        # and 1 would make draughts move
        if sum(self.board.itervalues()):
            value = DRAUGHT
        else:
            value = CROSS
        return value

    def move(self):
        """Random AI, what could be better?"""
        self.mark(random.choice([coord for coord, value in self.board.iteritems()
                                 if value == EMPTY])

    def mark(self, coord):
        """Mark the coord and check for the winning position"""
        self.board[coord] = self.current_mark
        check(self.board)


def check(board):
    """Simple routine for checking if somebody has won"""
    for x in xrange(3):
        if abs(sum(board[(x, y)] for y in xrange(3))) == 3:
            raise Victory
    for y in xrange(3):
        if abs(sum(board[(x, y)] for x in xrange(3))) == 3:
            raise Victory
    # Now, check the diagonals
    if (abs(sum(board[(x, x)] for x in xrange(3))) == 3 or
        abs(sum(board[(x, 2 - x)] for x in xrange(3))) == 3):
        raise Victory
    if 0 not in board.values():
        raise Draw
