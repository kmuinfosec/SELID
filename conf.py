"""
remain 처리 옵션 (remain flag)
- 0: remain 데이터 각각을 하나의 클러스터라고 생각하고 샘플링 수행
- 1: remain(-1)을 하나의 클러스터라고 생각하고 샘플링 수행
- 2: remain을 모두 제거하고 샘플링 수행

입력 문자열 AE청킹 윈도우 사이즈 (window size)

AE청크 피처 해싱 벡터 사이즈 (vector size)

Prototype clustering 유사도 임계값 (th)

클러스터 내 데이터 샘플링 개수 (sampling n)
"""

config =\
    {
        'remain flag' : 2,
        'window size' : 4,
        'vector size' : 512,
        'th' : 0.6,
        'sampling n' : 1,
    }