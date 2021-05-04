from django.shortcuts import render, redirect, HttpResponse
from leave.models import Addm, Dept, Gender, Hr_login, Addemp, Job, Man_login, E_login, Ltype, Eleave, Viewleave, \
    Acceptreject, Mleave, Viewleave1, Acceptreject1

from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def employee(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Addemp.objects.filter(eid=eid)
        return render(request, 'employee.html', {'res': s})
    else:
        redirect('e_login')


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
                    request.session['email'] = email
                    return redirect('manager')

                else:
                    messages.error(request, "invalid credential,please try again")
                    return redirect('m_login')

    return render(request, 'm_login.html')


def hr_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        n_pass = request.POST['n_pass']
        user = Hr_login.objects.filter(email=email)
        if user.count() == 0:
            messages.error(request, "Invalid credential,please try again")
            return redirect('hr_login')
        else:
            for h in user:
                if email == h.email and n_pass == h.n_pass:
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
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = Addm.objects.filter(email=email)
        return render(request, 'manager.html', {'res': s})
    else:
        redirect('m_login')


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
        log = Man_login(email=email, mid=mid, f_name=f_name, man_pass=man_pass)
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
        log = E_login(eid=eid, f_name=f_name, e_pass=e_pass)
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
        f_name = request.POST['f_name']
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
        s = Acceptreject.objects.filter(eid=eid)
        return render(request, 'myleave.html', {'res': s})
    else:
        redirect('e_login')


def myleave1(request):
    if request.method == 'POST':
        mid = request.POST['mid']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        ltype = request.POST['ltype']
        status1 = request.POST['status1']
        if request.session.has_key('mid'):
            mid = request.session.get('mid')
            s2 = Mleave.objects.filter(mid=mid)
        for record in s2:
            record.status1 = status1
            record.save(update_fields=['status1'])
            messages.success(request, "Profile Updated Successflly")
    if request.session.has_key('mid'):
        mid = request.session.get('mid')
        s = Acceptreject1.objects.filter(mid=mid)
        return render(request, 'myleave1.html', {'res': s})
    else:
        redirect('m_login')


def reg(request):
    return render(request, 'reg.html')


def viewleave(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Eleave.objects.values_list('status').filter(status='pending')
        messages.success(request, "Successfully added")
        return render(request, 'viewleave.html', {'res': s})
    else:
        return redirect('e_login')


def viewleave1(request):
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = Mleave.objects.filter()
        messages.success(request, "Successfully added")
        return render(request, 'viewleave1.html', {'res': s})
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


def status1(request):
    if request.session.has_key('mid'):
        mid = request.session.get('mid')
        s = Mleave.objects.all()
        if request.method == 'POST':
            s = Mleave.objects.get(mid=request.POST.get('mid'))
            s.status1 = request.POST.get('status1')
            s.save()
            messages.success(request, "Successfully added")
        lty = Ltype.objects.all()
        return render(request, 'status1.html', {'lty': lty, 'res': s})
    else:
        redirect('m_login')


def accept(request):
    if request.POST.get('eid'):
        eid = request.POST.get('eid')
        w = Eleave.objects.get(eid=eid)
        f_name = w.f_name
        sdate = w.sdate
        edate = w.edate
        ltype = w.ltype
        apt = Acceptreject(eid=eid, f_name=f_name, sdate=sdate, edate=edate, ltype=ltype, status='Accepted')
        apt.save()
        w.delete()
        return redirect('viewleave')


def accept1(request):
    if request.POST.get('mid'):
        mid = request.POST.get('mid')
        w1 = Mleave.objects.get(mid=mid)
        f_name = w1.f_name
        sdate = w1.sdate
        edate = w1.edate
        ltype = w1.ltype
        apt1 = Acceptreject1(mid=mid, f_name=f_name, sdate=sdate, edate=edate, ltype=ltype, status1='Accepted')
        apt1.save()
        w1.delete()
        return render(request, 'myleave1.html')


def reject(request):
    if request.POST.get('erid'):
        eid = request.POST.get('erid')
        w = Eleave.objects.get(eid=eid)
        f_name = w.f_name
        sdate = w.sdate
        edate = w.edate
        ltype = w.ltype
        apt = Acceptreject(eid=eid, f_name=f_name, sdate=sdate, edate=edate, ltype=ltype, status='Rejected')
        apt.save()
        w.delete()
        return redirect('viewleave')


def reject1(request):
    if request.POST.get('mrid'):
        mid = request.POST.get('mrid')
        w1 = Mleave.objects.get(mid=mid)
        f_name = w1.f_name
        sdate = w1.sdate
        edate = w1.edate
        ltype = w1.ltype
        apt1 = Acceptreject1(mid=mid, f_name=f_name, sdate=sdate, edate=edate, ltype=ltype, status1='Rejected')
        apt1.save()
        w1.delete()
        return render(request, 'myleave1.html')


def eleave(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = E_login.objects.filter(eid=eid)
        if request.method == 'POST':
            eid = request.POST['eid']
            f_name = request.POST['f_name']
            sdate = request.POST['sdate']
            edate = request.POST['edate']
            ltype = request.POST['ltype']
            request.session['eid'] = eid
            e = Eleave(eid=eid, f_name=f_name, sdate=sdate, edate=edate, ltype=ltype)
            e.save()
            messages.success(request, "Successfully added")
        lty = Ltype.objects.all()
        return render(request, 'eleave.html', {'lty': lty, 'res': s})
    else:
        redirect('e_login')


def mleave(request):
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = Man_login.objects.filter(email=email)
        if request.method == 'POST':
            mid = request.POST['mid']
            f_name = request.POST['f_name']
            sdate = request.POST['sdate']
            edate = request.POST['edate']
            ltype = request.POST['ltype']
            request.session['mid'] = mid
            eleave.total_leaves = 7
            e = Mleave(mid=mid, f_name=f_name, sdate=sdate, edate=edate, ltype=ltype)
            e.save()
            messages.success(request, "Successfully added")
        lty = Ltype.objects.all()
        return render(request, 'mleave.html', {'lty': lty, 'res': s})
    else:
        redirect('m_login')


def aleave(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Acceptreject.objects.filter(status='Accepted')
        return render(request, 'aleave.html', {'res': s})
    else:
        return redirect('e_login')


def aleave1(request):
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = Acceptreject1.objects.filter(status1='Accepted')
        return render(request, 'aleave1.html', {'res': s})
    else:
        return redirect('m_login')


def rleave(request):
    if request.session.has_key('eid'):
        eid = request.session.get('eid')
        s = Acceptreject.objects.filter(status='Rejected')
        return render(request, 'rleave.html', {'res': s})
    else:
        return redirect('e_login')


def rleave1(request):
    if request.session.has_key('email'):
        email = request.session.get('email')
        s = Acceptreject1.objects.filter(status1='Rejected')
        return render(request, 'rleave1.html', {'res': s})
    else:
        return redirect('m_login')
