# tansa

`tansa` is a simple **multi-threaded TCP port scanner** written in Python.  
It scans a target host for open ports (defaults to ports **1–1024**) and prints a scan report. Optionally, it can save the report to a `.txt` file.

> Educational use only. Scan only hosts you own or have explicit permission to test.

## Features
- Fast scanning using Python `threading`
- Scan **default ports (1–1024)** if no ports are specified
- Scan **specific ports** with `-p`
- Optional output report saved to a text file with `-o`
- Colored ASCII banner using `pyfiglet` + `colorama`

## Requirements
- Python 3.x
- Dependencies:
  - `pyfiglet`
  - `colorama`

Install dependencies:
```bash
pip install pyfiglet colorama
```

## Usage

### 1) Scan default ports (1–1024)
```bash
python tansa.py -t 127.0.0.1
```

### 2) Scan specific ports
Provide one or more ports after `-p`:
```bash
python tansa.py -t 127.0.0.1 -p 22 80 443 8080
```

### 3) Save results to a file
```bash
python tansa.py -t 127.0.0.1 -o report.txt
```

You can also combine `-p` and `-o`:
```bash
python tansa.py -t example.com -p 21 22 80 443 -o scan_report.txt
```

## Output
- Prints each open port found as it scans:
  - `Port 80 is open`
- Prints a final summary report:
  - Target
  - List of open ports
- If `-o` is provided, it writes a small “Scan Report” section to the file.

## Notes
- The script uses a default socket timeout of **0.2s**, which makes scanning faster but may miss ports on slow networks.

## License
Add a license if you plan to share/redistribute (MIT is common).
