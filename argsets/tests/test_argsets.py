from argsets import __version__
from argsets.argsets import hello, ParseKwargs # this means, in argsets/argsets.py, import the function, hello and the class, ParseKwargs
import pytest
import argparse

def test_version():
    assert __version__ == '0.1.0'

def  test_world():
    assert hello() == "world"


def test_pairs():
    # creating parser pbject
    parser = argparse.ArgumentParser()
      
    # adding an arguments 
    parser.add_argument('--server', 
                        nargs='*', 
                        action = ParseKwargs)

    # this is where I simulate the command line passing multiple
    # arguments of the same key. Once I get this working, I will
    # do the same for another attribute, --userId
    raw_args = [ '--server', 'One', '--server' , 'Two', '--server', 'Three' ]
      
     #parsing arguments 
    args = parser.parse_args(raw_args)
      
    # show the dictionary
    print(args.kwargs)

    assert 1 == 1
