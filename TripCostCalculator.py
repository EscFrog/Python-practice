# 호텔 비용
def hotel_cost(nights):
    return nights * 140

# 비행기 비용
def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
    else:
        return

# 차 렌트 비용
def rental_car_cost(day):
    if day >= 7:
        return day * 40 - 50
    elif 7 > day >= 3:
        return day * 40 - 20
    else:
        return day * 40

# 종합 비용
def trip_cost(city,days,spending_money):
    total = plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money
    return total

print (trip_cost('Los Anjeles',4,600))


