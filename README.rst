=============================
SNAP+Hopskotch interface test
=============================

Preparation
------------

Create the virtual environment (optional)::

    python -m venv venv_hopsnap
    source venv_hopsnap/bin/activate
    pip install --upgrade pip

Install dependencies::
    
    pip install -r requirements.txt

Run hopskotch server::

    docker run -p 9092:9092 -dit --rm=true --name=scimma-server --hostname localhost scimma/server:latest --noSecurity

Test#1: send/recv of python dicts
---------------------------------

First test to show that we can send the generated python dict (with current timestamp) via the hopskotch server.

* Module: `sntest.py`
* Configuration: `sntest1.yml`

The sender node will produce a message with current timestamp every second and send it to `kafka://localhost:9092/test`

The receiver will get this message and print it on the screen.

Sender
""""""

Run sender in one shell session::

    snap sntest1.yml -n node_send

Receiver
""""""""

Run receiver in another shell session::
   
    snap sntest1.yml -n node_recv

or receive using the hop client::

    hop subscribe --no-auth kafka://localhost:9092/test --persist

Test#2: sending/receiving `snap.DataBlock` as an unformatted JSON blob
----------------------------------------------------------------------

In this example we produce fake neutrino events, calculate the significance vs time for  a client, and send this data as a hopskotch message to `kafka://localhost:9092/test`.

The combination node will receive these messages, combine them (in case there are several clients) and apply the threshold to the combination. If the significance exceeds threshold (5 sigma), the time series are sent to the `kafka://localhost:9092/alert` topic.

* Configuration: `sntest2.yml`

Client sender
"""""""""""""

In shell session #1::

    snap sntest2.yml -n node_client

Combination node
""""""""""""""""

In shell session #2::

    snap sntest2.yml -n node_combine

Receiving alerts
""""""""""""""""

You can monitor the alerts with the hop cli::

    hop subscribe --no-auth kafka://localhost:9092/alert --persist

Also you can check the files, where the data is dumped on each step:

* data_received.dat
* data_combined.dat
* data_triggered.dat

Test#3: sending/receiving `snap.DataBlock` as a registered message
------------------------------------------------------------------

**TODO**
