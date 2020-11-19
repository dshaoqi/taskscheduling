from django.shortcuts import render
from .models import Host,User,Record,Method,Flow,FlowMethodMembership
from django.views import generic
import paramiko
import time
# Create your views here.
from django.http import HttpResponse

def index(request):
    num_hosts=Host.objects.all().count()
    num_records=Record.objects.all().count()
    return render(request,'index.html',context={'num_hosts':num_hosts,'num_records':num_records,})

class HostListView(generic.ListView):
    model = Host
    paginate_by = 10 #分页
    template_name='hosts/list.html'

class RecordListView(generic.ListView):
    model = Record 
    paginate_by = 10 #分页
    template_name='records/list.html'

def StepView(request):
    return render(request,'steps/list.html')

def StepResultView(request):
    if request.method == "POST":
        ip = request.POST.get("ip")
        username = request.POST.get("username")
        command = request.POST.get("command")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,'dsq',timeout=5)
        shell=ssh.invoke_shell()
        time.sleep(0.1)

        shell.send('su - \n')
        buff=''
        while not buff.endswith('Password: '):
            resp=shell.recv(10000)
            buff+=resp.decode('utf-8')
            print("buff:"+buff)
        shell.send('dsq\n')
        buff=''
        while not buff.endswith('# '):
            resp=shell.recv(10000)
            buff+=resp.decode('utf-8')
        print("root reach")

        shell.send(command+'\n')
        shell.close()
        ssh.close()
        response = ip+":"+username+":"+command+":"+buff
        return HttpResponse(response)
    else:
        return HttpResponse("wrong request")

class FlowListView(generic.ListView):
    model = Flow
    template_name = 'flows/list.html'

'''
def FlowView(request):
    method_list=Method.objects.all()
    context={"method_list":method_list}
    return render(request,'flows/list.html',context)
'''

def HostDetailView(request,host_id):
    host = Host.objects.get(id=int(host_id))
    #print ("host:"+host.ip)
    user_list = host.user_set.all() 
    method_list = host.method_set.all()
    record_list = Record.objects.none()
    for method in method_list :
        record_list |= method.record_set.all()
    #print(record_list)
    context={ "user_list":user_list,"method_list":method_list,"record_list":record_list }
    return render(request,'hostdetail/list.html',context)

def FlowDetailView(request,flow_id):
    flow = Flow.objects.get(id=int(flow_id))
    mrank_list = []
    membership = FlowMethodMembership.objects.filter(flow__id=flow_id)
    for member in membership:
        method = Method.objects.get(id=member.method.id)
        ip = method.ip.ip
        username = method.username.username
        command = method.command
        rank = member.rank
        comments = method.comments
        mrank_list.append({ "ip":ip, "username":username, "command":command, "rank":rank, "comments":comments, "methodid":method.id })
    mrank_list.sort(key=(lambda x:x.get('rank')))
    context = { "mrank_list":mrank_list, "flow":flow }
    return render(request,"flowdetail/list.html",context)


def FlowCommitView(request):
    if request.method == 'POST':
        if request.POST:
            flowid = request.POST.get('flowid',0)
            flow = Flow.objects.get(id=int(flowid))
            print(flow)
            membership = flow.flowmethodmembership_set.all()
            membership.sort(key=(lambda x:x.rank))
            for mem in membership:
                method = Method.objects.get(id=mem.id)
                res = CarryOut(method)
                if(res!='ok'):
                    return HttpResponse(res);
            return HttpResponse('ok')
    else:
        return HttpResponse("no")

def FlowStatusView(request):
    if request.method == 'POST':
        return HttpResponse("FlowStatusView() no")
    else:
        return HttpResponse("FlowStatusView() no")
