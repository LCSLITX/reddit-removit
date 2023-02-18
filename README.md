# Reddit-Removit

Reddit-Removit is a script application to remove comments from Reddit accounts.

## Requirements

- Reddit account, API client_id and client_secret.
- Python3 installed.
- Docker (optional)

## How to use it

- Clone this repository;
- Edit `.example.env` file with your account data, choose the appropriate options and rename file to `.env`;
- Pass `True` as parameter to `rmvit()` function in `src/main.py`;
- Execute command `make install_dependencies` to install dependencies;
- Execute with `make execute_script`.