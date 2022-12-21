with open('data.txt', 'r') as f:
    data = f.readlines()

for i in data:
    print(i)

message = 'Hello World'
print(message.replace('Hello', 'Bonjour'))