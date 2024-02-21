import json

# Load the JSON data from the file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Extract interface information
interfaces = []
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    speed = attributes['speed']
    mtu = attributes['mtu']
    description = attributes['descr'] if attributes['descr'] else ''
    interfaces.append((dn, description, speed, mtu))

# Print the output
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for interface in interfaces:
    print("{:<50} {:<20} {:<8} {:<6}".format(interface[0], interface[1], interface[2], interface[3]))
