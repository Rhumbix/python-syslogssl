from syslogssl import NewLineFraming

def test_no_input_just_new_line():
    assert "\n" == NewLineFraming().frame("")

def test_adds_new_to_input():
    assert "must be something\n" == NewLineFraming().frame("must be something")

def test_ignores_newlines_in_input():
    assert "It's okay\nWe're alright\n" == NewLineFraming().frame("It's okay\nWe're alright")
