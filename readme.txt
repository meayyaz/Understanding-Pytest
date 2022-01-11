pytest -k test_ayyaz  --> One file
pytest -k --> all files containing 'test' in file name

# Fixtures are functions, which will run before each test function to which it is applied.

pytest -k  divisible -v fixture_text.py


we can use Conftest.py for common fixtures


pip install pytest-cov

pytest --cov