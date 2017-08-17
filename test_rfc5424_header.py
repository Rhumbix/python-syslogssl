from collections import namedtuple
from syslogssl import RFC5424Header, SSLSysLogHandler


MockRecord = namedtuple( "MockRecord", 'created process' )


def test_formats_all_values_specified():
    handler = SSLSysLogHandler( "localhost" )
    handler.process_name = "robert"
    handler.hostname = "captain"

    record = MockRecord( created= 0, process=1985 )

    formatter = RFC5424Header()
    result = formatter.format_header( handler, record, "<1>", "modest little mouse")
    assert "<1>1 1970-01-01T00:00:00Z captain robert 1985 - - modest little mouse" == result
