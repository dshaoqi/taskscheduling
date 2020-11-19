import paramiko
from app.models import Method
def CarryOut(method):
    username = method.username.username
    ip = method.ip.ip
    command = method.command
    password = User.objects.filter(ip__ip=ip,username=username)[0].password
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if username !='root':
         ssh.connect(ip,22,username,password,timeout=5)
         stdin,stdout,stderr = ssh.exec_command(command)
         out,err=stdout.read().decode('utf-8'),stderr.read().decode('utf-8')
         status=stdout.channel.recv_exit_status()
         ssh.close()
#        return HttpResponse("out:"out+"\nerr:"+err+"\nstatus=%d"%status)
    else:
        ssh.connect(ip,22,'myroot','abcd1234',timeout=5)
        shell=ssh.invoke_shell()
        time.sleep(0.1)
        shell.send('su - \n')
        buff=''
        while not buff.endswith('Password: '):
            resp=shell.recv(10000)
            buff+=resp.decode('utf-8')

        shell.send(password+'\n')
        buff=''
        while not buff.endswith('# '):
            resp=shell.recv(10000)
            buff+=resp.decode('utf-8')
        print(ip+":root reach")

        shell.send(command+'\n')
        buff=''
        while not buff.endswith('# '):
            resp = shell.recv(10000)
            buff += resp.decode('utf-8')
        shell.close()
        ssh.close()
    return 1
#           return HttpResponse(ip+":"+username+":"+command+'\n'+buff)

