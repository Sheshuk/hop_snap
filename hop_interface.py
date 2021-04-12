import hop

async def recv(address: str, auth: bool=False):
    """ Receive messages from hopskotch (source)
    Args:
        address: hopskotch location of the format 'kafka://{host}:{port}/{topic} to subscribe
        auth: use hopskotch authentication (default: false)
    Yields:
        received message
    """
    stream = hop.Stream(auth=auth, persist=True)
    while True:
        try:
            with stream.open(address, 'r') as s:
                for msg in s:
                    yield msg
        except ValueError as e:
            print(e)

def send(address: str, auth: bool=False):
    """ Send messages to hopskotch (step)
        Args:
           address: hopskotch location of the format 'kafka://{host}:{port}/{topic} to publish
           auth: use hopskotch authentication (default: false)
    """
    stream = hop.Stream(auth=None)
    s = stream.open(address, 'w')
    def _f(data):
        try:
            s.write(data)
        except ValueError:
            print(e)
    return _f

