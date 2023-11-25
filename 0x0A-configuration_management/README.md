# Configuration Management Project

## Overview

This project focuses on configuration management using Puppet, with an emphasis on managing files, installing packages, and executing commands. The tasks aim to provide hands-on experience in using Puppet for system administration and DevOps purposes.

## Project Details

- **Author:** Sylvain Kalache
- **Weight:** 1
- **Project Start:** Nov 24, 2023, 6:00 AM
- **Project End:** Nov 25, 2023, 6:00 AM
- **Checker Release:** Nov 24, 2023, 12:00 PM
- **Auto Review Deadline:** Nov 25, 2023, 6:00 AM

## Background

The project is inspired by a real-world scenario where a bug in an auto-remediation tool led to unintended consequences. Sylvain shares an incident from his time at SlideShare, highlighting the importance of configuration management tools like Puppet for infrastructure reliability.

## Resources

Before you start, make sure to familiarize yourself with the following resources:

- [Intro to Configuration Management](#)
- [Puppet resource type: file](#) (Check "Resource types" for all manifest types in the left menu)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](#)
- [Puppet lint](#)
- [Puppet emacs mode](#)

## Requirements

### General

- All files interpreted on Ubuntu 20.04 LTS.
- Files end with a new line.
- Mandatory README.md file at the project root.
- Puppet manifests must pass puppet-lint version 2.1.1 without errors.
- Puppet manifests must run without errors.
- Puppet manifest files must end with the extension .pp.

### Versioning

Ensure your Ubuntu 20.04 VM has Puppet 5.5 preinstalled. Use the following commands:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
$ gem install puppet-lint
```

## Tasks

### Task 0: Create a File

Using Puppet, create a file in /tmp.

#### Requirements:

- File path is /tmp/school
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains "I love Puppet"


