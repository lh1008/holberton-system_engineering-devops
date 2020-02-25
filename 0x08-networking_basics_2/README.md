# 0x08. Networking basics #1

## Learning Objectives

- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is `/etc/hosts`
- How to display your machine’s active network interfaces

## Tasks

_**0. Localhost**_  
- What is localhost?
  1. A hostname that means this IP
  2. A hostname that means this computer
  3. An IP attached to a computer

_**1. All IPs**_  
- What is 0.0.0.0?
  1. All IPv4 addresses on the local machine
  2. All the IPs
  3. It means null in networking

_**2. Change your home IP**_  
Write a Bash script that configures an Ubuntu server with the below requirements.
- Requirements:

  - localhost resolves to 127.0.0.2
  - facebook.com resolves to 8.8.8.8.
  - The checker is running on Docker, so make sure to read [this](https://web.archive.org/web/20171117023601/http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

_**3. Show attached IPs**_  
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
