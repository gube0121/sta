import random

# 스타포스 확률 테이블 (간략화)
# [성공확률, 실패확률, 파괴확률]
starforce_table = {
    0: [95, 5, 0],
    1: [90, 10, 0],
    2: [85, 15, 0],
    3: [85, 15, 0],
    4: [80, 20, 0],
    5: [75, 25, 0],
    6: [70, 30, 0],
    7: [65, 35, 0],
    8: [60, 40, 0],
    9: [55, 45, 0],
    10: [50, 50, 0],
    11: [45, 55, 0],
    12: [40, 60, 0],
    13: [35, 65, 0],
    14: [30, 70, 0],
    15: [30, 67.9, 2.1],
    16: [30, 67.2, 2.8],
    17: [30, 66.3, 3.7],
    18: [30, 65.2, 4.8],
    19: [30, 63.0, 7.0],
    20: [30, 60.0, 10.0],
    21: [30, 57.0, 13.0],
    22: [3.0, 77.6, 19.4],  # 매우 낮은 확률
    23: [2.0, 77.0, 21.0],
    24: [1.4, 77.3, 21.3]
}

MAX_STAR = 25

def attempt_starforce(star):
    if star >= MAX_STAR:
        return star, "최대치 도달"

    success, fail, destroy = starforce_table.get(star, [0, 0, 100])
    rand = random.uniform(0, 100)

    if rand <= success:
        return star + 1, "성공"
    elif rand <= success + fail:
        # 일부 단계에서는 실패 시 하락
        if star >= 15:
            return star - 1, "실패(하락)"
        return star, "실패(유지)"
    else:
        return -1, "파괴"

def simulate_enhancement(target=17):
    star = 0
    count = 0
    logs = []

    while 0 <= star < target:
        count += 1
        star, result = attempt_starforce(star)
        logs.append(f"{count}회차: {result} → 현재 {star}성")
        if star == -1:
            logs.append("장비 파괴됨. 시뮬레이션 종료.")
            break

    return logs, count, star

if __name__ == "__main__":
    target_star = int(input("목표 스타 수를 입력하세요 (예: 17): "))
    logs, tries, result = simulate_enhancement(target_star)
    print("\n[강화 결과 로그]")
    for log in logs:
        print(log)
    print(f"\n총 시도 횟수: {tries}회, 최종 스타 수: {result}성")
