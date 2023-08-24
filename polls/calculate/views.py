from django.shortcuts import render

def calculate(request):
    total_score = 0
    if request.method == 'POST':
        home = int(request.POST.get('home'))
        family = int(request.POST.get('family'))
        bankbook = float(request.POST.get('bankbook'))

        # 무주택 기간 산정
        home_score = 0
        for i in range(1, home + 1):
            home_score = 2 * home + 2
            if home > 15:
                home_score = 32

        # 부양 가족 수
        family_score = 0
        for i in range(1, family + 1):
            family_score = 5 * (family + 1)
            if family > 6:
                family_score = 35

        # 청약 통장 가입 기간
        bankbook_score = 0
        for i in range(int(0.5 * 10), int(bankbook * 10)):
            bankbook_score = bankbook + 2
            if bankbook < 0.5:
                bankbook_score = 1
            elif bankbook >= 0.5 and bankbook < 1:
                bankbook_score = 2
            elif bankbook > 15:
                bankbook_score = 17

        total_score = home_score + family_score + int(bankbook_score)

    context = {'total_score': total_score}

    return render(request, 'calculate/calculate.html', context)
