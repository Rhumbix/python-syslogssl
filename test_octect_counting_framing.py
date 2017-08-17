from syslogssl import OctetCountingFraming

def test_empty_input_has_zero_frame():
    assert "0 " == OctetCountingFraming().frame( "" )

def test_adds_new_to_input():
    assert "19 Down in the village" == OctetCountingFraming().frame( "Down in the village" )

def test_ignores_newlines_in_input():
    assert "22 Ignores new\nline input" == OctetCountingFraming().frame( "Ignores new\nline input" )
