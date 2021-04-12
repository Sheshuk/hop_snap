=============================
SNAP+Hopskotch interface test
=============================

Preparation
------------

Create the virtual environment (optional)::

    python -m venv venv_hopsnap
    source venv_hopsnap/bin/activate

Install dependencies::
    
    pip install -r requirements.txt

Run hopskotch server::

    docker run -p 9092:9092 -dit --rm=true --name=scimma-server --hostname localhost scimma/server:latest --noSecurity

Test#1 send/recv of python dicts:
---------------------------------

Sender
""""""

Run sender in one shell session::

    snap sntest.yml -n node_send

Receiver
""""""""

Run receiver in another shell session::
   
    snap sntest.yml -n node_recv

or receive using the hop client::

    hop subscribe --no-auth kafka://localhost:9092/test --persist

