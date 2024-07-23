from django.shortcuts import render
from datetime import datetime, timedelta
import calendar

def home(request):
    today = datetime.today()
    month = today.month
    year = today.year
    today_day = today.day

    # 달력의 첫 요일을 일요일로 설정
    calendar.setfirstweekday(calendar.SUNDAY)

    # 현재 달의 첫날과 마지막 날
    first_day_of_month = datetime(year, month, 1)
    last_day_of_month = (first_day_of_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)

    # 이전 달과 다음 달의 날짜 계산
    start_date = first_day_of_month - timedelta(days=first_day_of_month.weekday() + 1)  # 일요일 이전으로 설정
    last_day_of_week = last_day_of_month + timedelta(days=(5 - last_day_of_month.weekday() + 7) % 7) # 다음 월의 마지막 토요일까지
    end_date = last_day_of_week

    # 달력 데이터 생성
    cal_data = []
    current_date = start_date
    while current_date <= end_date:
        week_data = []
        for _ in range(7):
            if current_date.month == month:
                # 현재 달의 날짜
                day = current_date.day
                day_class = 'current-month'
            else:
                # 이전 또는 다음 달의 날짜
                day = current_date.day
                day_class = 'other-month'
            week_data.append((day, day_class))
            current_date += timedelta(days=1)
        cal_data.append(week_data)

    context = {
        'month': month,
        'year': year,
        'today_day': today_day,
        'cal_data': cal_data,
    }

    return render(request, 'cal/home.html', context)
