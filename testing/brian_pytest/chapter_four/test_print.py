""" To demostrate that the capsys fixture in Pytest captures the output.
This is why pytest test_print.py, attempting to test this script, won't write anything to the command interface
pytest -s test_print.py or pytest --capture=no test_print.py will overwrite the output.
"""
def test_normal():
    print("\nnormal print")

""" Pytest would show the print statement last since it is a failing test"""
def test_fail():
    print("\nprint in failing test")
    assert False

""" The output in the with bloc will always be disabled, even without the -s flag.
This means they will be written to the CI"""
def test_disabled(capsys):
    with capsys.disabled():
        print("\ncapsys disabled print")