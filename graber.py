file = open('/home/srb/sda_devops/pytest', 'w')
file.write('To jest tex ktory bedzie w pliku')
file.close()

with open('/home/srb/sda_devops/pytest', 'w') as file_handler:
    pass

print(file_handler.closed)
