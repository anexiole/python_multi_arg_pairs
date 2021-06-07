# from argsets import __version__
from argsets.argsets import hello, ParseKwargs # this means, in argsets/argsets.py, import the function, hello and the class, ParseKwargs
import pytest
import argparse
import sys

def test_version():
    assert __version__ == '0.1.0'

def  test_world():
    assert hello() == "world"

def test_multi_args():
    # creating parser pbject
    parser = argparse.ArgumentParser()

    # adding an arguments
    parser.add_argument('--server',
                        nargs='*',
                        dest='servers',
                        action='append')

    # fake some args
    raw_args = ['--server', 'One', '--server', 'Two', '--server', 'Three']

    # this is where I simulate the command line passing multiple
    # arguments of the same key. Once I get this working, I will
    # do the same for another attribute, --userId
    ret_args = vars(parser.parse_args(raw_args))

    assert 'servers' in ret_args
    assert ret_args['servers'] == [['One'], ['Two'], ['Three']]


