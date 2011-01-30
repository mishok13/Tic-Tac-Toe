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


def next_mark(board):
    """What should the next mark be"""
    if sum(board.itervalues()):
        return DRAUGHT
    else:
        return CROSS


def current_mark(board):
    """What was the latest mark on the board"""
    if sum(board.itervalues()):
        return CROSS
    else:
        return DRAUGHT


def random_move(board):
    """This is liek the most powerful AI ever"""
    return random.choice([coord for coord, value in board.iteritems()
                          if value == EMPTY])


def bruteforce(board):
    """Going through the simple way"""
    # Opening, just put cross into the corner
    if sum(value == EMPTY for value in board.itervalues()) == 9:
        return (0, 0)
    # Opening, but from the draughts side, put draught in the center
    if (sum(value == EMPTY for value in board.itervalues()) == 8 and
        board[(1, 1)] == EMPTY):
        return (1, 1)
    # If there's a situation with two in a row, block it or win
    for line in columns_and_diagonals(board):
        if abs(sum(line.values())) == 2:
            return (coord for coord, value in line.iteritems()
                    if value == EMPTY).next()
    # TODO: fork
    # Play center
    if board[(1, 1)] == EMPTY:
        return (1, 1)
    # TODO: opposite corner
    # Empty corner
    for coord in ((x, y) for x in (0, 2) for y in (0, 2)):
        if board[(1, 1)] == EMPTY:
            return coord
    # There's nothing else left, just play whatever there is
    return random_move(board)


def columns_and_diagonals(board):
    for x in xrange(3):
        yield dict(((x, y), board[(x, y)]) for y in xrange(3))
        yield dict(((y, x), board[(y, x)]) for y in xrange(3))
    yield dict(((x, x), board[(x, x)]) for x in xrange(3))
    yield dict(((x, 2 - x), board[(x, 2 - x)]) for x in xrange(3))



def empty_board():
    return dict(((x, y), EMPTY) for x in xrange(3) for y in xrange(3))


def check(board):
    """Simple routine for checking if somebody has won"""
    for line in columns_and_diagonals(board):
        if abs(sum(line.values())) == 3:
            raise Victory
    if 0 not in board.values():
        raise Draw
