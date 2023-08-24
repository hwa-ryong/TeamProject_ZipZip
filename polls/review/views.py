from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import FreeForm, AnswerForm
from .models import Review_Board, Answer_Review

def review_list_main(request):
    question_list = Review_Board.objects.order_by('-r_regdate')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_main.html', context) # 거래후기 게시판

def review_recommend(request):
    question_list = Review_Board.objects.order_by('-r_recommend')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_main.html', context) # 거래후기 게시판

def review_list_jan(request):
    question_list = Review_Board.objects.filter(r_type='전/월세').order_by('-r_regdate')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_jan.html', context) #전세게시판

def review_list_jan_recommend(request):
    question_list = Review_Board.objects.filter(r_type='전/월세').order_by('-r_recommend')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_jan.html', context)

def review_list_mama(request):
    question_list = Review_Board.objects.filter(r_type='매매').order_by('-r_regdate')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_mama.html', context)

def review_list_mama_recommend(request):
    question_list = Review_Board.objects.filter(r_type='매매').order_by('-r_recommend')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_mama.html', context)

def review_list_subscription(request):
    question_list = Review_Board.objects.filter(r_type='청약').order_by('-r_regdate')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_subscription.html', context)

def review_list_subscription_recommend(request):
    question_list = Review_Board.objects.filter(r_type='청약').order_by('-r_recommend')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'review/review_list_mama.html', context)


#########################      함수시작영역  ############################################


def review_detail(request, review_board_id): # 게시글 상세보기
    review_board = get_object_or_404(Review_Board, id=review_board_id)


    # 게시글 추천 테스트
    if request.method == 'POST':
        # 게시글 추천처리
        review_board.r_recommend += 1
        review_board.save()
        return redirect('review:review_detail', review_board_id=review_board_id)
    else:
        review_board.r_hit += 1
        review_board.save()

    # AnswerForm과 연관된 데이터 필터링
    answers_list = Answer_Review.objects.filter(board_id=review_board_id)

    context = {'review_board': review_board, 'answers_list':answers_list}
    return render(request, 'review/review_detail.html', context)



def review_write(request): # 게시글 작성
    if request.method == "POST":
        form = FreeForm(request.POST)

        if form.is_valid():
            free = form.save(commit=False)
            free.user = request.user
            free.r_regdate = timezone.now()
            free.save()

            return redirect('review:review_main')
    else:
        form = FreeForm()

    context = {'form': form, 'free_board': {'user': request.user, 'r_regdate': timezone.now()}}
    return render(request, 'review/review_write.html', context) # 게시판 작성

def comment_create(request, review_board_id):
    # 댓글 등록
    review_board = get_object_or_404(Review_Board, pk=review_board_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # 세션
            comment.create_date = timezone.now()
            comment.question = review_board
            comment.board_type = 'Review_Board'
            comment.board_id = review_board.pk
            comment.save()
            return redirect('review:review_detail',review_board_id=review_board_id)
    else:
        form=AnswerForm
    context = {'review_board' : review_board, 'form' : form}
    return render(request, 'review/review_detail.html',context)


@login_required(login_url='community:signin')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Answer_Review, pk=comment_id)
    comment.delete()
    return redirect('review:review_detail', review_board_id=comment.board_id) # 댓글 삭제


@login_required(login_url='community:signin')
def comment_update(request, comment_id):
    comment = get_object_or_404(Answer_Review, pk=comment_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('review:review_detail', review_board_id=comment.board_id)

    else:
        form = AnswerForm(instance=comment)
    context = {'form': form}
    return render(request, 'review/review_comment_update.html', context) # 댓글 수정

# 게시판 삭제
@login_required(login_url='community:signin')
def review_delete(request, comment_id):
    comment = get_object_or_404(Review_Board, pk=comment_id)
    comment.delete()
    return redirect('review:review_main')

# 게시판 수정

# views.py

@login_required(login_url='community:signin')
def review_update(request, review_board_id):
    review_board = get_object_or_404(Review_Board, pk=review_board_id)

    if request.method == "POST":
        form = FreeForm(request.POST, instance=review_board)

        if form.is_valid():
            review = form.save(commit=False)
            review.r_modifydate = timezone.now()
            review.user = request.user
            review.save()

            return redirect('review:review_detail', review_board_id=review_board_id)
    else:
        form = FreeForm(instance=review_board)

    context = {'form': form, 'review_board': review_board}
    return render(request, 'review/review_update.html', context)





