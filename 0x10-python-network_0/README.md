
# 0x10. Python - Network #0

## Table of Contents
- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. cURL body size](#0-curl-body-size)
  - [1. cURL to the end](#1-curl-to-the-end)
  - [2. cURL Method](#2-curl-method)
  - [3. cURL only methods](#3-curl-only-methods)
  - [4. cURL headers](#4-curl-headers)
  - [5. cURL POST parameters](#5-curl-post-parameters)
  - [6. Find a peak](#6-find-a-peak)
  - [7. Only status code](#7-only-status-code)
  - [8. cURL a JSON file](#8-curl-a-json-file)
  - [9. Catch me if you can!](#9-catch-me-if-you-can)
- [Copyright and Plagiarism](#copyright-and-plagiarism)




## Tasks

### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

### 1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.

### 2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`.

### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable `email` must be sent with the value `test@gmail.com`, and a variable `subject` must be sent with the value `I will always be here for PLD`.

### 6. Find a peak
Write a function that finds a peak in a list of unsorted integers.

### 7. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

### 8. cURL a JSON file
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. The script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.

### 9. Catch me if you can!
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
