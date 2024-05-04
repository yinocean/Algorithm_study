def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        # 등차수열인 경우 마지막 값 common[-1]에 +r 하여 리턴
        return common[-1] + (common[1] - common[0])
        # 등비수열인 경우 마지막 값에 common[-1]에 *n 하여 리턴
    return common[-1] * (common[1] / common[0])