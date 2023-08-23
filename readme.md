## Chat-with-Python: Simple Client-Server Chat Program
The Chat-with-Python program is a basic client-server chat application that allows multiple users to connect and communicate with each other over a network. This README will guide you through the steps to set up and run the chat program on your computer.

## Getting Started
Follow these steps to set up and run the Chat-with-Python program on your computer.

## Prerequisites
Python 3.x installed on your computer.

## Step 1: Starting the Server
Open your command prompt or terminal.

Navigate to the directory where the server.py file is located.

Run the following command to start the server:

```bash
python -u server.py
```
This will start the chat server, which will be responsible for handling client connections and messages.

Step 2: Running the Client Program
Open a new command prompt or terminal window.

Navigate to the directory containing the clientgui.py file.

If you're running the client program on the same computer as the server, no changes are needed. Simply run the following command:

```bash
python clientgui.py
```
This will open the client GUI, allowing you to connect and start chatting.

If you want to connect from an external computer, you need to edit the clientgui.py file.(Note both computer should be in same wifi):

Open clientgui.py in a text editor.

Locate the line that sets the IP address in the code. Update the IP address to match the IP address of the computer running the server.

```python
SERVER_IP = 'server_ip_address_here'
```
Replace 'server_ip_address_here' with the actual IP address of the server computer.

Save the changes.

Run the following command to start the client GUI:

```bash
python clientgui.py
```
Using the Chat Program
Once the client GUI is open, you can enter a username and click the "Connect" button to join the chat.

You can exchange messages with other connected users by typing in the text input area and pressing "Send" or hitting Enter.

To disconnect from the chat, simply close the client GUI window.

## Final words
This can be useful for students searching for a basic python projects that uses sockets.
Make your changes accordingly and feel free to contribute
