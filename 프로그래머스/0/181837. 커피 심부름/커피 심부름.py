def solution(order):
    answer = 0
    for i in order:
        if i == 'iceamericano' or i == 'americanoice' or i == 'hotamericano' or i == 'americanohot' or i == 'americano' or i == 'anything':
            answer += 4500
        elif i == 'icecafelatte' or i == 'cafelatteice' or i == 'hotcafelatte' or i == 'cafelattehot' or i == 'cafelatte':
            answer += 5000
    return answer