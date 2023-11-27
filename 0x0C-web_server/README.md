# 0x0C. Web Server

## Overview

The "0x0C Web Server" project focuses on configuring and automating web server-related tasks on an Ubuntu 16.04 LTS environment. This project delves into essential concepts such as web servers, DNS, child processes, and HTTP requests. The goal is to create an automated setup that aligns with the specified requirements.

## Concepts

### What is a Child Process?

A child process is a subprocess spawned by a parent process. In the context of web servers, the main HTTP server process often spawns child processes to handle incoming requests, ensuring efficient handling of multiple connections.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the main role of a web server.
- Explain the concept of a child process and its relevance in web server architecture.
- Outline the main HTTP requests.
- Define DNS, its primary role, and common DNS record types (A, CNAME, TXT, MX).

## Requirements

- Allowed Editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- Files should end with a newline
- Bash scripts must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any errors
- The first line of Bash scripts should be `#!/usr/bin/env bash`
- The second line of Bash scripts should explain the script's purpose
- No use of `systemctl` for restarting a process

## Tasks

### 0. Transfer a File to Your Server

Write a Bash script that transfers a file from a client to a server using `scp`. The script should accept parameters for the file path, server IP, username, and SSH private key path. Strict host key checking must be disabled.

Example:

```bash
./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
```

### 1. Install Nginx Web Server

Write a Bash script to install Nginx on your web-01 server. Nginx should be listening on port 80, and a GET request to its root ("/") should return a page containing the string "Hello World!"

Example:

```bash
./1-install_nginx_web_server
curl localhost
# Output: Hello World!
```

### 2. Setup a Domain Name

Provide the domain name obtained from .TECH Domains. Configure DNS records with an A entry so that the root domain points to your web-01 IP address.

Example:

```bash
cat 2-setup_a_domain_name
# Output: myschool.tech
```

### 3. Redirection

Configure Nginx to redirect "/redirect_me" to another page using a "301 Moved Permanently" redirection.

Example:

```bash
./3-redirection
curl -sI 34.198.248.145/redirect_me/
# Output: HTTP/1.1 301 Moved Permanently
# Location: https://www.youtube.com/watch?v=QH2-TGUlwu4
```

### 4. Not Found Page 404

Configure Nginx to have a custom 404 page containing the string "Ceci n'est pas une page."

Example:

```bash
./4-not_found_page_404
curl -sI 34.198.248.145/xyz
# Output: HTTP/1.1 404 Not Found
curl 34.198.248.145/xyzfoo
# Output: Ceci n'est pas une page
```

## Conclusion

This project emphasizes automation and configuration of web servers, enhancing your understanding of critical concepts in web development and server management. The goal is to create efficient, automated processes that adhere to best practices.
