"""
Salt execution module
"""
import logging
import random

log = logging.getLogger(__name__)

__virtualname__ = "eight_ball"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The eight_ball  module is not implemented yet")
    return __virtualname__


def print():
    """
    Return a random choice from Magic 8 Ball replies

    CLI Example:

    .. code-block:: bash

        salt '*' eight_ball.print
    """
    replies = [
        {"result": True, "message": "Signs point to yes"},
        {"result": True, "message": "Without a doubt"},
        {"result": True, "message": "You may rely on it"},
        {"result": False, "message": "Do not count on it"},
        {"result": True, "message": "Looking good"},
        {"result": False, "message": "Cannot predict now"},
        {"result": True, "message": "It is decidedly so"},
        {"result": False, "message": "Outlook not so good"},
    ]
    return random.choice(replies)
