# tyyp
Internet censorship analyzer. **WORK IN PROGRESS**

## Usage
```bash
$ ./tyyp.py imgur.com
imgur.com TURKTELEKOM 195.175.39.49 Timeout
imgur.com TURKTELEKOM 195.175.39.50 Timeout
imgur.com KABLONET 62.248.80.161 Timeout
imgur.com KABLONET 62.248.80.162 Ok

$ ./tyyp.py google.com
google.com TURKTELEKOM 195.175.39.49 Ok
google.com TURKTELEKOM 195.175.39.50 Ok
google.com KABLONET 62.248.80.161 Ok
google.com KABLONET 62.248.80.162 Ok
```