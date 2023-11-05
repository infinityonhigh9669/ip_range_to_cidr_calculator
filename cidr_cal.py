import ipaddress

with open("ip_ranges.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split("\t")
    first_ip = parts[0]
    last_ip = parts[1]
    count = int(parts[2])

    first_ip_obj = ipaddress.IPv4Address(first_ip)
    last_ip_obj = ipaddress.IPv4Address(last_ip)
    network = ipaddress.summarize_address_range(first_ip_obj, last_ip_obj)
    cidr = next(network)

    print(cidr)
