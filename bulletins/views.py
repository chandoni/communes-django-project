from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from .models import Community, CommunityBulletins, CommunityMembers, Bulletin
from .forms import BulletinForm

def bulletin_search(request):
    return render(request, 'search.html', {})

def searchfor(request):
    if request.method == 'POST':
        searchname = request.POST['searchname']
        try:
            com = Community.objects.get(name=searchname)
        except ObjectDoesNotExist:
            not_found = slugify(searchname, allow_unicode=True)
            return redirect('not-found', not_found)

        searchname = slugify(searchname, allow_unicode=True)
        return redirect('searched', searchname, 1)

def get_not_found(request, notfound):
    return render(request, 'community_not_found.html', {'not_found':notfound})



def searched(request, searchname, pg):
    communities_found = Community.objects.filter(name__icontains=searchname)
    results_found = communities_found.count()
    paginator = Paginator(communities_found,  3)
    total_pages = paginator.num_pages
    communities = paginator.page(pg)

    return render(request, 'searched.html', {'searchname':searchname,
                                                'communities_found':communities,
                                                'results_found':results_found,
                                                'total_pages':total_pages,
                                                'cur_page':pg,
                                                })

    return render(request, 'searched.html', {'communities_found':communities_found, 'results_found':results_found})

def join_community(request, commname):
    if request.user.is_authenticated:
        try:
            mem_com = Community.objects.get(name=commname)
            mem = CommunityMembers.objects.get(community=mem_com, members=request.user)
            # delete record
            mem.delete()
            return redirect('bullet', commname)
        except ObjectDoesNotExist:
            # not member, add record
            com = Community.objects.get(name=commname)
            new_mem = CommunityMembers(community=com, members=request.user)
            new_mem.save()
            return redirect('bullet', commname)

def get_community_bulletin(request, commname):
    is_member = False
    if request.user.is_authenticated:
        try:
            com = Community.objects.get(name=commname)
            mem = CommunityMembers.objects.get(community=com, members=request.user)
            is_member = True
        except ObjectDoesNotExist:
            is_member = False

    comm = Community.objects.get(name=commname)
    community_bulletins = CommunityBulletins.objects.filter(community=comm)
    bulletin_list = [b.bulletins for b in community_bulletins]

    return render(request, 'community_bulletin.html', {'commname':commname, 'bulletin_list':bulletin_list, 'is_member':is_member})


def create_bulletin(request, commname):
    form = BulletinForm(request.POST or None)
    if request.method == 'POST':
        post_title = request.POST['title']
        post_caption = request.POST['caption']

        bulletin = Bulletin(title=post_title, caption=post_caption, user_account=request.user)
        bulletin.save()
        get_community = Community.objects.get(name=commname)
        comm_bulletin = CommunityBulletins(community=get_community, bulletins=bulletin)
        comm_bulletin.save()

        return redirect('create_bulletin', commname)
    return render(request, 'create_new_bulletin.html', {'commname':commname, 'form':form})
