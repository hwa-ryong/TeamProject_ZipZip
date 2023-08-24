from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import UserForm, SignupForm, UserInformationUpdateForm

from django.contrib.auth import authenticate, login, logout

import pytesseract
from PIL import Image

from community.models import Free_Board
from review.models import Review_Board


# 회원 가입
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            is_business = form.cleaned_data.get('is_business')

            if is_business:
                business_license = form.cleaned_data.get('business_license')
                # 사업자 등록증 파일 처리
                user.business_license = business_license

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user.save()

            user = authenticate(username=username, password=password, last_name=last_name, email=email)
            login(request, user)
            return JsonResponse({'success': True})
        else:
            errors = {
                'form_errors': render_to_string('form_errors.html', {'form': form}),
            }
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'common/signup.html', context)

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #로그인
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "아이디와 비밀번호를 확인해 주세요"
            return render(request, 'common/login.html', {'error': error})
    else:
        return render(request, 'common/login.html')

def signout(request):
    logout(request)
    return redirect('/')

def extract_text_from_image(image_file):
    # 이미지 열기
    image = Image.open(image_file)

    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(image, lang="kor+eng")

    # 추출된 텍스트 반환
    return text

# 마이 페이지
def mypage(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    free_write = Free_Board.objects.filter(user=user_id)
    review_write = Review_Board.objects.filter(user=user_id)

    context = {
        'user': user,
        'free_write': free_write,
        'review_write': review_write,
    }

    return render(request, 'common/mypage.html', context)

# 유저 삭제
def mypage_delete(request, username):
    user_delete = get_object_or_404(User, username=username)
    user_delete.delete()
    return redirect('poll:index')

# 유저 정보 수정
def mypage_update(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        form = UserInformationUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            return redirect('common:mypage')
    else:
        form = UserInformationUpdateForm()

    context = {
        'user': user, 'form': form,
    }
    return render(request, 'common/mypage_update.html', context)