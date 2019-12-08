# Directory Listings

A simple python script that checks for links that might possibly lead to a directory listing. 

[![asciicast](https://asciinema.org/a/MvWbcv8dPVOxXHwVVaOoc4fX9.svg)](https://asciinema.org/a/MvWbcv8dPVOxXHwVVaOoc4fX9)

Set `CHECK_LINKS` in `run.py` to true to make the script check if the links it finds are valid. 
This usually takes a minute or so.

Directory Listings may contain sensitive information that can in cases be exploited. The easiest way to prevent this is
to disable Indexing in your web server, and only enable them for required directories.
