# terminal-flag-banner
A Python package to display a country banner (the flag and country name) in the terminal.

#### To run
```sh
usage: python -m terminal_flag_banner --country-code COUNTRY_CODE

Display a flag banner in the terminal.

options:
  -h, --help            show this help message and exit
  --country-code COUNTRY_CODE
                        The country code of the flag to display.
```

#### Example I/O (Japan)
```sh
python -m terminal_flag_banner --country-code JP
```
![Japan expected output](images/expected_output_japan.png)