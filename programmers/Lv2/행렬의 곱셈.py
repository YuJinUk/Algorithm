import numpy as np
def solution(arr1, arr2):
    return (np.array(arr1) @ np.array(arr2)).tolist() # numpy의 array에서 @을 통해 행렬의 곱을 구하고 리스트로 형변환을 시켜준다.