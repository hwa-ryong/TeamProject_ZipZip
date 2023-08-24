from django.shortcuts import render

def notice(request):
    return render(request, 'notice/notice_list.html')  # 공지사항

def notice_view1(request):
    return render(request, 'notice/notice_view1.html') # 1 번 게시판

def notice_view2(request):
    return render(request, 'notice/notice_view2.html') # 2 번 게시판

def notice_view3(request):
    return render(request, 'notice/notice_view3.html') # 3 번 게시판

def notice_view4(request):
    return render(request, 'notice/notice_view4.html') # 4 번 게시판

def notice_view5(request):
    return render(request, 'notice/notice_view5.html') # 5 번 게시판