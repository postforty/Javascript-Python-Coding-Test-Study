# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# 스킬트리

# 실패(일부 통과)
# def solution(skill, skill_trees):
#     answer = 0

#     new_skill = "_" + skill

#     for skill_tree in skill_trees:
#         idx = 0
#         for skill in skill_tree:
#             if new_skill.find(skill) == -1:
#                 continue
#             if idx - new_skill.find(skill) == -1:
#                 idx = new_skill.find(skill)
#         if idx > 1:
#             answer += 1

#     return answer

# 실패(일부만 성공)
# def solution(skill, skill_trees):
#     answer = 0

#     new_skill = "_" + skill

#     for skill_tree in skill_trees:
#         idx = 0
#         for skill in skill_tree:
#             if new_skill.find(skill) == -1:
#                 continue
#             if idx - new_skill.find(skill) == -1:
#                 idx = new_skill.find(skill)
#             if idx - new_skill.find(skill) > 0: # 순서가 꼬인 경우에 대한 처리
#                 idx = 0
#                 break
#         if idx > 1:
#             answer += 1

#     return answer


# 성공
# def solution(skill, skill_trees):
#     answer = 0

#     for skill_tree in skill_trees:
#         temp = ""
#         for ch in skill_tree:
#             if ch in skill:
#                 temp += ch

#         if skill[:len(temp)] == temp:
#             answer += 1

#     return answer

# 성공
# def solution(skill, skill_trees):
#     answer = 0

#     for skill_tree in skill_trees:
#         temp = ""
#         for ch in skill_tree:
#             if ch in skill:
#                 temp += ch

#         if skill.startswith(temp):
#             answer += 1

#     return answer

# 성공
# def solution(skill, skill_trees):
#     def is_valid_skill_tree(skill, skill_tree):
#         filtered_skills = [ch for ch in skill_tree if ch in skill]
#         return skill.startswith(''.join(filtered_skills))

#     return sum(is_valid_skill_tree(skill, skill_tree) for skill_tree in skill_trees)

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)

        for ch in skill_tree:
            if ch in skill:
                if ch != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
