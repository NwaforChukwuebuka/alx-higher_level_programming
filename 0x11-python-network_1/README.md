# Python - Network

This repository contains scripts written in Python for interacting with HTTP messages, URLs, and APIs using the `urllib` and `requests` libraries. These scripts were created as part of the learning process to understand how to send and receive HTTP messages, fetch JSON resources, and interact with various APIs such as the Star Wars API, GitHub API, and Twitter API.

## Tasks

### 0. What's my status? #0
**File:** `0-hbtn_status.py`  
**Description:** Python script that fetches the status of [https://intranet.hbtn.io/status](https://intranet.hbtn.io/status) using `urllib`.

### 1. Response header value #0
**File:** `1-hbtn_header.py`  
**Description:** Python script that displays the value of the `X-Request-Id` response header variable of a request to a given URL using `urllib`.

### 2. POST an email #0
**File:** `2-post_email.py`  
**Description:** Python script that sends a POST request to a given URL with a specified email and displays the response body using `urllib`.

### 3. Error code #0
**File:** `3-error_code.py`  
**Description:** Python script that sends a request to a given URL and displays the response body. It handles HTTP errors using `urllib`.

### 4. What's my status? #1
**File:** `4-hbtn_status.py`  
**Description:** Python script that fetches the status of [https://intranet.hbtn.io/status](https://intranet.hbtn.io/status) using `requests`.

### 5. Response header value #1
**File:** `5-hbtn_header.py`  
**Description:** Python script that displays the value of the `X-Request-Id` response header variable of a request to a given URL using `requests`.

### 6. POST an email #1
**File:** `6-post_email.py`  
**Description:** Python script that sends a POST request to a given URL with a specified email and displays the response body using `requests`.

### 7. Error code #1
**File:** `7-error_code.py`  
**Description:** Python script that sends a request to a given URL and displays the response body. It handles HTTP errors using `requests`.

### 8. Search API
**File:** `8-json_api.py`  
**Description:** Python script that sends a POST request to [http://0.0.0.0:5000/search_user](http://0.0.0.0:5000/search_user) with a letter passed as a parameter and displays the response body using `requests`.

### 9. Star Wars API #0
**File:** `9-starwars.py`  
**Description:** Python script that sends a search request to the Star Wars API people endpoint with a given string and displays the total number and name of each result using `requests`.


### 10. Time for an interview!
**File:** `100-github_commits.py`  
**Description:** Python script that lists the 10 most recent comments of a given GitHub repository using the GitHub API using `requests`.
