# 프로그래머스
# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    check_num = 0

    for tree in skill_trees:
        for i in range(len(tree)):
            if tree[i] in skill and check_num != -1:
                if skill.find(tree[i]) == check_num:
                    check_num += 1
                else:
                    check_num = -1

        if check_num != -1:
            answer += 1

        check_num = 0

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
