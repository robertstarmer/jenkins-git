"""
A place to collect arguments and add other fixture
"""

import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="environment to run tests against")
    parser.addoption("--browser", action="store", default="chrome", help="browser for running tests")
    parser.addoption("--number", type=int, default=0, help="integer type")