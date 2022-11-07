
"""

It connects to remote linux device and execute commands 
remotely from local host

"""



# import paramiko

# hostname = '192.168.0.103'
# username = 'shiva'
# password = 'India@123'

# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname= hostname, username=username, password=password)

# print('client connected successfully')

# stdin, stdout, stderr = client.exec_command('hostname ; hostname -i ;  uname ; uname -r ;')

# list = []
# for line in stdout:
#     list.append( line.strip('\n'))

# rec = ({ "hostname" : list[0], "host_ip" : list[1], "os" : list[2], "os_version" : list[3]})
# print(rec)

#         client.close()


class RemoteAgent:

    def __init__(self, hostname, username, password) -> None:
        self.hostname = hostname
        self.username = username
        self.password = password

    def connect_to_remote_host(self):

        """
        
        It establishes connection with remote device

        """

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname= self.hostname, username= self.username, password= self.password)

    def execute_commands(self):

        """
        
        It executes commands in remote device and prints response 
        on local device

        """

        commands = ['top','df -H','uname -a','hostname -i']

        for command in commands:
            print(command)
            print("\n")
            stdin, stdout, stderr = self.exec_command(command)
            print(stdout.read().decode())

    
        

        


if __name__ == "__main__":

    import paramiko

    connection = RemoteAgent('192.168.0.103','shiva','India@123')  
    connection.connect_to_remote_host()
    connection.execute_commands()
    





















