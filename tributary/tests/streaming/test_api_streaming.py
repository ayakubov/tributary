import tributary.streaming as ts


class TestAPI:
    def test_api(self):
        assert hasattr(ts.StreamingNode, '__add__')
        assert hasattr(ts.StreamingNode, '__add__')
        assert hasattr(ts.StreamingNode, '__radd__')
        assert hasattr(ts.StreamingNode, '__sub__')
        assert hasattr(ts.StreamingNode, '__rsub__')
        assert hasattr(ts.StreamingNode, '__mul__')
        assert hasattr(ts.StreamingNode, '__rmul__')
        assert hasattr(ts.StreamingNode, '__div__')
        assert hasattr(ts.StreamingNode, '__rdiv__')
        assert hasattr(ts.StreamingNode, '__truediv__')
        assert hasattr(ts.StreamingNode, '__rtruediv__')
        assert hasattr(ts.StreamingNode, '__pow__')
        assert hasattr(ts.StreamingNode, '__rpow__')
        assert hasattr(ts.StreamingNode, '__mod__')
        assert hasattr(ts.StreamingNode, '__rmod__')
        assert hasattr(ts.StreamingNode, 'sum')
        assert hasattr(ts.StreamingNode, 'average')
        assert hasattr(ts.StreamingNode, 'invert')
        assert hasattr(ts.StreamingNode, '__and__')
        assert hasattr(ts.StreamingNode, '__or__')
        assert hasattr(ts.StreamingNode, '__invert__')
        assert hasattr(ts.StreamingNode, '__bool__')
        assert hasattr(ts.StreamingNode, 'int')
        assert hasattr(ts.StreamingNode, 'float')
        assert hasattr(ts.StreamingNode, '__str__')
        assert hasattr(ts.StreamingNode, '__lt__')
        assert hasattr(ts.StreamingNode, '__le__')
        assert hasattr(ts.StreamingNode, '__gt__')
        assert hasattr(ts.StreamingNode, '__ge__')
        assert hasattr(ts.StreamingNode, '__eq__')
        assert hasattr(ts.StreamingNode, '__ne__')
        assert hasattr(ts.StreamingNode, '__neg__')
        assert hasattr(ts.StreamingNode, '__len__')
        assert hasattr(ts.StreamingNode, 'log')
        assert hasattr(ts.StreamingNode, 'sin')
        assert hasattr(ts.StreamingNode, 'cos')
        assert hasattr(ts.StreamingNode, 'tan')
        assert hasattr(ts.StreamingNode, 'asin')
        assert hasattr(ts.StreamingNode, 'acos')
        assert hasattr(ts.StreamingNode, 'atan')
        assert hasattr(ts.StreamingNode, 'abs')
        assert hasattr(ts.StreamingNode, 'sqrt')
        assert hasattr(ts.StreamingNode, 'exp')
        assert hasattr(ts.StreamingNode, 'erf')
        assert hasattr(ts.StreamingNode, 'round')
        assert hasattr(ts.StreamingNode, 'floor')
        assert hasattr(ts.StreamingNode, 'ceil')

        assert hasattr(ts.StreamingNode, 'delay')
        # assert hasattr(ts.StreamingNode, 'state')
        assert hasattr(ts.StreamingNode, 'apply')
        assert hasattr(ts.StreamingNode, 'window')
        assert hasattr(ts.StreamingNode, 'unroll')
        assert hasattr(ts.StreamingNode, 'unrollDataFrame')
        assert hasattr(ts.StreamingNode, 'merge')
        assert hasattr(ts.StreamingNode, 'listMerge')
        assert hasattr(ts.StreamingNode, 'dictMerge')
        assert hasattr(ts.StreamingNode, 'map')
        assert hasattr(ts.StreamingNode, 'reduce')

        assert hasattr(ts.StreamingNode, 'graph')
        assert hasattr(ts.StreamingNode, 'pprint')
        assert hasattr(ts.StreamingNode, 'graphviz')
        assert hasattr(ts.StreamingNode, 'dagre')
        assert hasattr(ts.StreamingNode, 'print')
        assert hasattr(ts.StreamingNode, 'if_')

    def test_api_streaming_specific(self):
        '''apis specific to streaming nodes'''
        # window functions
        assert hasattr(ts.StreamingNode, 'perspective')
        assert hasattr(ts.StreamingNode, 'rollingCount')
        assert hasattr(ts.StreamingNode, 'rollingSum')
        assert hasattr(ts.StreamingNode, 'rollingCount')
        assert hasattr(ts.StreamingNode, 'rollingMin')
        assert hasattr(ts.StreamingNode, 'rollingMax')
        assert hasattr(ts.StreamingNode, 'rollingAverage')
        assert hasattr(ts.StreamingNode, 'diff')
        assert hasattr(ts.StreamingNode, 'sma')
        assert hasattr(ts.StreamingNode, 'ema')
        assert hasattr(ts.StreamingNode, 'rollingLast')
        assert hasattr(ts.StreamingNode, 'rollingFirst')

        # inputs
        assert hasattr(ts, "Console")
        assert hasattr(ts, "File")
        assert hasattr(ts, "FileSource")
        assert hasattr(ts, "FileSink")
        assert hasattr(ts, "HTTP")
        assert hasattr(ts, "HTTPSource")
        assert hasattr(ts, "HTTPSink")
        assert hasattr(ts, "Kafka")
        assert hasattr(ts, "KafkaSource")
        assert hasattr(ts, "KafkaSink")
        assert hasattr(ts, "Postgres")
        assert hasattr(ts, "PostgresSource")
        assert hasattr(ts, "PostgresSink")
        assert hasattr(ts, "SocketIO")
        assert hasattr(ts, "SocketIOSource")
        assert hasattr(ts, "SocketIOSink")
        assert hasattr(ts, "WebSocket")
        assert hasattr(ts, "WebSocketSource")
        assert hasattr(ts, "WebSocketSink")

        # Other inputs
        assert hasattr(ts, "Timer")
        assert hasattr(ts, "Const")
        assert hasattr(ts, "Curve")
        assert hasattr(ts, "Foo")
        assert hasattr(ts, "Random")
