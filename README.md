# IP Range to CIDR Calculator

## Introduction
This tool is built on Python 3.8 and is designed to convert IP ranges into CIDR notation. 
You can provide the starting and ending IP addresses in the 'ip_ranges.txt' file. 

The format should be as follows:
```
196.0.0.0     196.0.255.255     196.0.0.0/16     65536
196.43.128.0  196.43.191.255  196.43.128.0/18  16384
197.239.0.0    197.239.63.255    197.239.0.0/18    16384
41.210.128.0  41.210.191.255  41.210.128.0/18  16384
197.157.0.0    197.157.63.255    197.157.0.0/18    16384
```

## How to Use
1. Make sure you have Python 3.8 or later installed on your system.

2. Create or edit the 'ip_ranges.txt' file, adding your IP ranges in the specified format.

3. Run the script to calculate the CIDR notation for each IP range.

```
python ip_range_to_cidr.py
```
The results will be displayed on the console.

## Example
Suppose you have an 'ip_ranges.txt' file with the following entries:
```
196.0.0.0     196.0.255.255     196.0.0.0/16     65536
196.43.128.0  196.43.191.255  196.43.128.0/18  16384
```
Running the script will output:
```
IP Range: 196.0.0.0 - 196.0.255.255  CIDR: 196.0.0.0/16  Size: 65536
IP Range: 196.43.128.0 - 196.43.191.255  CIDR: 196.43.128.0/18  Size: 16384
```
