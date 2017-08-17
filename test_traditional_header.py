from syslogssl import TraditionalHeader

def test_only_message_and_priority():
    assert "<81>I'm just a message" == TraditionalHeader().format_header("not syslog", "not record", "<81>", "I'm just a message")
