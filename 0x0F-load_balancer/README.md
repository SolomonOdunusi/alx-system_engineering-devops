# 0x0F Load Balancer

This project focuses on configuring a load balancer to distribute traffic across multiple web servers, ensuring redundancy, scalability, and improved reliability of the web stack.

![Load Balancer and Server Image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)
## Table of Contents

- [Project Description](#project-description)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Double the number of webservers](#0-double-the-number-of-webservers)
  - [1. Install your load balancer](#1-install-your-load-balancer)

## Project Description

In this project, we aim to enhance our web stack by introducing redundancy for our web servers. The addition of a load balancer allows us to handle more traffic by distributing requests across multiple servers. If one server fails, the load balancer ensures that another server can handle the requests, making the infrastructure more reliable.

## Requirements

- All files will be interpreted on Ubuntu 16.04 LTS.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck (version 0.3.7) without any error.
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- A README.md file, at the root of the project folder, is mandatory.

## Tasks

### 0. Double the number of webservers

Configure Nginx on both web-01 and web-02 servers to contain a custom header in the HTTP response. The custom header, `X-Served-By`, should indicate the hostname of the server handling the request.

- Script: [0-custom_http_response_header](./0-custom_http_response_header)
- Example Usage:

  `bash`
  curl -sI [SERVER_IP] | grep X-Served-By

### 1. Install your load balancer
Install and configure HAproxy on lb-01 server to distribute traffic to web-01 and web-02 using a round-robin algorithm. Ensure HAproxy can be managed via an init script.

- Script: 1-install_load_balancer

- Example Usage:

 ```bash
curl -Is [LB_IP]
