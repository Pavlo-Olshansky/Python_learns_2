# import Crypto
# import paramiko
import pysftp as sftp  # Secure File Transtort Protocol

'''
Often troubles :

Bad Authentication

if username and pass correct, ftp installed in your server, uncomment smth like this:
sudo nano /stc/ssh/sshd_config
#PasswordAuthentification = yes

ssh-keygen

# paramico do cool key generator
'''


def sftp_example():
    try:
        s = sftp.Connection(host='HKinsley.com', username='user', password='pass')

        remote_path = '/var/www/html/example.txt'
        local_path = 'example.txt'  # full path
        s.put(local_path, remote_path)
        # s.get(remote_path, local_path)
        s.close()

    except Exception as e:
        print(str(e))
