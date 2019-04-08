# Shared-file-protection-by-Locking-scheme-in-a-Distributed-System

Implementation, Learnings and Issues:

Implemented the centralized locking algorithm. There is a server and multiple clients, where multiple clients try to access a shared file. So, when a first client accesses the shared file it acquires a lock, increments a counter. During this time no other client can access this file. Once the lock is released by the first client the other clients gets to access the shared file. The goal is to make sure that at a time only one client acquires the lock to a shared file while the other clients wait for their access to the shared file.

Learnt the concept of multithreading and how the shared resources are handled in real time. Implementing the lock acquire feature by the clients and the communication among the clients was an issue in this assignment. 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Importing project into workspace:

* Open PyCharm IDE.
* Right click on File.
* Select “Open..”
* Browse to the folder where the project is saved.
* Click “OK” to complete the process.

Running of the Python Project:

* Open the project in the PyCharm IDE.
* Run the server.py file followed by the client.py file.
* Run the client.py file as many time required to create a number of multiple clients.
* Open the file.txt file to see the counter update.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
