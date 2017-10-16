from django.db.models import Q
from django.shortcuts import render, get_object_or_404, HttpResponse,\
                            HttpResponseRedirect
from members.forms import MemberForm
from members.models import Member
from django.urls import reverse
# Create your views here.

def member_list(request):
    all_member = Member.objects.all().order_by('full_name')

    # SEARCH 
    query_string = request.GET.get('members')
    if query_string:
        all_member = all_member.filter(
            Q(full_name__icontains = query_string)|
            Q(bio__icontains = query_string)
            # Q(alt__icontains = query_string)|
            
            ).distinct()
    template_name = 'members/list.html'
    context = {
        'all_member': all_member
    }
    return render(request, template_name, context)

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    template_name = 'members/detail.html'
    context = {
        'member':member
    }
    return render(request, template_name, context)

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Member List', args = []))
    else:
        form = MemberForm()
    template_name = 'members/new_member.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)

def update_member_info(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance = member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Member Detail', 
                kwargs = {'pk':pk}))
    else:
        form = MemberForm(instance = member)
    template_name = 'members/new_member.html'
    context = {
    'form':form
    }
    return render(request, template_name, context)