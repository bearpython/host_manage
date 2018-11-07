from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import HttpResponse
from MPhost import init_db
#import init_db
from sqlalchemy.orm import sessionmaker,relationship

Session_class = sessionmaker(bind=init_db.engine)
session = Session_class()

def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("user",None)
        pwd = request.POST.get("pwd",None)
        error_msg = ""
        db_pwd = session.query(init_db.User).filter_by(name=user).all()
        if db_pwd:
            if pwd == str(db_pwd[0]):
                #去跳转
                return redirect("/index")
            else:
                error_msg = "用户名或密码错误"
        else:
            error_msg = "用户名或密码错误"
    return render(request,"login.html",{"error_msg":error_msg})


def index(request):
    return render(request,"index.html")


def introduce(request):
    return render(request, "introduce.html")

def host_list(request):
    HOST_LIST = []
    host_info = session.query(init_db.Host).all()
    for i in host_info:
        temp = {"hostname": i.hostname, "hostid": i.hostid, "ip": i.ip,"port":i.port,"operation":i.operation,"status":i.status,"hostaddr":i.hostaddr,"hosttype":i.hosttype}
        HOST_LIST.append(temp)
    return render(request, "host_list.html",{"host_list":HOST_LIST})

def host_add(request):
    HOST_LIST = []
    host_info = session.query(init_db.Host).all()
    for i in host_info:
        temp = {"hostname": i.hostname, "hostid": i.hostid, "ip": i.ip,"port":i.port,"operation":i.operation,"status":i.status,"hostaddr":i.hostaddr,"hosttype":i.hosttype}
        HOST_LIST.append(temp)
    return render(request, "host_add.html",{"host_list":HOST_LIST})

def add_win(request):
    error_msg = ""
    if request.method == "POST":
        #获取用户提交的数据，POST请求
        hostname = request.POST.get("hostname")
        hostid = request.POST.get("hostid")
        ip = request.POST.get("ip")
        port = request.POST.get("port")
        operation = request.POST.get("operation")
        status = request.POST.get("status")
        hostaddr = request.POST.get("hostaddr")
        hosttype = request.POST.get("hosttype")
        # print(hostid,hostname,ip,port,operation,status,hostaddr,hosttype)
        if hostname and hostid and ip and port and operation and status and hostaddr and hosttype:
            data = init_db.Host(hostname=hostname,hostid=hostid,ip=ip,port=port,operation=operation,status=status,hostaddr=hostaddr,hosttype=hosttype)
            session.add(data)
            session.commit()
        else:
            error_msg = "所有填写项目均不能为空"
        return render(request, "add_win.html", {"error_msg": error_msg})
    return render(request, "add_win.html")


def del_host(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        # print(nid)
        session.query(init_db.Host).filter(init_db.Host.id == nid).delete()
        session.commit()
    return redirect("/host_list")