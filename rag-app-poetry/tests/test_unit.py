import sys

sys.path.append("/Users/Markus/oxford-genai-llmops-project/rag-app-poetry/")
from src.rag_app_poetry.basic_functions import *

def test_add():
    assert add(5,5) == 10


def test_multiply():
    assert multiply(5,5) == 25


def test_substarct():
    assert substract(5,5) == 9