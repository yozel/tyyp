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

## TODO
- Add checker for URL based censorship for HTTP requests
- Add checker for SNI based censorship for HTTPS requests
- Add checker for IP based censorship
- Make outputs more verbose (and use logging instead of print?)
- Create one sentence summary for whats going on
- Suggest actions for anti censorship
- Make tyyp and it's checkers configurable with config.yaml file
