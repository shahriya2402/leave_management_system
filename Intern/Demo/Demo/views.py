from django.shortcuts import render, redirect, HttpResponse
from leave.models import Addm, Dept, Gender, Hr_login, Addemp, Job, Man_login, E_login, Ltype, Eleave, Viewleave, Status, Accept

from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def employee(request):
    return render(request, 'employee.html')


def e_login(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        e_pass = request.POST['e_pass']
        user = E_login.objects.filter(eid=eid)
        if user.count() == 0:
            messages.error(request, "Invalid credential,please try again")
            return redirect('e_login')
        else:
            for e in user:
                if eid == e.eid and e_pass == e.e_pass:
                    request.session['eid'] = eid
                    return redirect('employee')
                else:
                    messages.error(request, "invalid credential,please try again")
                    return redirect('e_login')

    return render(request, 'e_login.html')


def m_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        man_pass = request.POST['man_pass']
        user = Man_login.objects.filter(email=email)
        if user.count() == 0:
            messages.error(request, "Invalid credential,please try again")
            return redirect('m_login')
        else:
            for m in user:
                if email == m.email and man_pass == m.man_pass:
                    return redirect('manager')
                else:
                    messages.error(request, "invalid credential,please try again")
                    return redirect('m_login')

    return render(request, 'm_login.html')


def hr_login(request):
    if request.method == 'POST':
        hrid = request.POST['hrid']
        n_pass = request.POST['n_pass']
        user = Hr_login.objects.filter(hrid=hrid)
        if user.count() == 0:
            messages.error(request, "Invalid credential,please try again")
            return redirect('hr_login')
        else:
            for h in user:
                if hrid == h.hrid and n_pass == h.n_pass:
                    return redirect('hr')
                else:
                    messages.error(request, "invalid credential,please try again")
                    return redirect('hr_login')

    return render(request, 'hr_login.html')


def registration(request):
    return render(request, 'registration.html')


def hr(request):
    return render(request, 'hr.html')


def manager(request):
    return render(request, 'manager.html')


def addmanager(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        mid = request.POST['mid']
        email = request.POST['email']
        fdate = request.POST['fdate']
        cno = request.POST['cno']
        dept = request.POST['dept']
        gender = request.POST['gender']
        man_pass = request.POST['man_pass']
        a = Addm(f_name=f_name, l_name=l_name, mid=mid, email=email,
                 fdate=fdate, cno=cno, dept=dept, gender=gender, man_pass=man_pass)
        a.save()
        log = M_login(mid=mid, man_pass=man_pass)
        log.save()
        messages.success(request, "Successfully added")

    dept = Dept.objects.all()
    gen = Gender.objects.all()
    return render(request, 'addmanager.html', {'dept': dept, 'gen': gen})


def addemployee(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        eid = request.POST['eid']
        email = request.POST['email']
        fdate = request.POST['fdate']
        cno = request.POST['cno']
        job = request.POST['job']
        gender = request.POST['gender']
        e_pass = request.POST['e_pass']
        e = Addemp(f_name=f_name, l_name=l_name, eid=eid, email=email,
                   fdate=fdate, cno=cno, job=job, gender=gender, e_pass=e_pass)
        e.save()
        log = E_login(eid=eid, e_pass=e_pass)
        log.save()
        messages.success(request, "Successfully added")

    job = Job.objects.all()
    gen = Gender.objects.all()
    return render(request, 'addemployee.html', {'job': job, 'gen': gen})


def gallery(request):
    return render(request, 'gallery.html')


def firstindex(request):
    return render(request, 'firstindex.html')


def myleave(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        ltype = request.POST['ltype']
        status = request.POST['status']
        if request.session.has_key('eid'):
            eid = request.session.get('eid')
            s1 = Eleave.objects.filter(eid=eid)
        for record in s1:
            record.status = status
            record.save(update_fields=['status'])
            messages.success(request, "Profile Updated Successflly")
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Accept.objects.filter(eid=eid)
        return render(request, 'myleave.html', {'res': s})
    else:
        redirect('e_login')


def reg(request):
    return render(request, 'reg.html')




def viewleave(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Eleave.objects.filter()
        messages.success(request, "Successfully added")
        return render(request, 'viewleave.html', {'res': s})
    else:
        return redirect('e_login')


def status(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Eleave.objects.all()
        if request.method == 'POST':
            s = Eleave.objects.get(eid=request.POST.get('eid'))
            s.status = request.POST.get('status')
            s.save()
            messages.success(request, "Successfully added")
        lty = Ltype.objects.all()
        return render(request, 'status.html', {'lty': lty, 'res': s})
    else:
        redirect('e_login')


def accept(request):
    if request.POST.get('eid'):
        eid = request.POST.get('eid')
        print(eid)
        w = Eleave.objects.get(eid=eid)

        sdate=w.sdate
        edate=w.edate
        ltype=w.ltype
        rsn=w.rsn
        print(sdate, edate, ltype, rsn)
        apt = Accept(eid=eid, sdate=sdate, edate=edate, ltype=ltype, rsn=rsn)
        apt.save()
        w.delete()
        return render(request, 'myleave.html')

def eleave(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Eleave.objects.filter(eid=eid)
        if request.method == 'POST':
            eid = request.POST['eid']
            sdate = request.POST['sdate']
            edate = request.POST['edate']
            ltype = request.POST['ltype']
            rsn = request.POST['rsn']
            request.session['eid'] = eid
            e = Eleave(eid=eid, sdate=sdate, edate=edate, ltype=ltype, rsn=rsn)
            e.save()
            messages.success(request, "Successfully added")
        lty = Ltype.objects.all()
        return render(request, 'eleave.html', {'lty': lty, 'res': s})
    else:
        redirect('e_login')

