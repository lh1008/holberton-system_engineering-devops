# 0x0B. SSH

## Learning Objectives

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Tasks

_**0. Use a private key**_
Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/holberton` with the user `ubuntu`.

_**1. Create an SSH key pair**_
Write a Bash script that creates an RSA key pair.

_**2. Client configuration file**_
Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

_**3. Let me in!**_
Add the SSH public key below to your server so that we can connect using the ubuntu user.
