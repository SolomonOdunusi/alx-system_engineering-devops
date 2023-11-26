# 0x0B. SSH - DevOps Project

## Introduction

This project involves configuring SSH for secure remote access to an Ubuntu server. The tasks include creating and using an RSA key pair, configuring the SSH client, and using Puppet for client configuration.

Author: Solomon Odunusi

## Project Overview

The project is centered around the following tasks:

1. **Use a private key**
    - Write a Bash script that connects to the server using the private key `~/.ssh/school` with the user `ubuntu`.

    ```bash
    ./0-use_a_private_key
    ```

2. **Create an SSH key pair**
    - Write a Bash script that creates an RSA key pair named `school` with a passphrase.

    ```bash
    ./1-create_ssh_key_pair
    ```

3. **Client configuration file**
    - Configure the local SSH client to use the private key `~/.ssh/school` and refuse password authentication.

4. **Let me in!**
    - Add an SSH public key to the server to allow connecting using the `ubuntu` user.

5. **Client configuration file (w/ Puppet)**
    - Use Puppet to configure the client SSH configuration file to use the private key `~/.ssh/school` and refuse password authentication.

    ```bash
    sudo puppet apply 100-puppet_ssh_config.pp
    ```

## Usage

- Clone the repository:

    ```bash
    git clone https://github.com/solomonodunusi/alx-system_engineering-devops.git
    ```

- Navigate to the project directory:

    ```bash
    cd alx-system_engineering-devops/0x0B-ssh
    ```

- Execute the scripts based on the task requirements.

## Additional Notes

- Ensure that the SSH client configurations align with the provided requirements.
- Follow the instructions in each task carefully for successful completion.


