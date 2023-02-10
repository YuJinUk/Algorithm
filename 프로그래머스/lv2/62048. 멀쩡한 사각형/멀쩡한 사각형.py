from math import gcd # 최대공약수
def solution(w,h):
    w, h = min(w,h), max(w,h)
    wh_gcd = gcd(w,h)
    a, b = w//wh_gcd , h//wh_gcd 
    # if w == h: # 정사각형일 경우
    #     return w*(h-1)
    
    return w*h - (b+a-1) * wh_gcd