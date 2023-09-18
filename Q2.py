
# Q2: A队在比赛中进球数少于或等于B队进球数的比赛总数

# def count_matches(teamA_scores,teamB_scores):
#     count = 0
#     for i in range(len(teamA_scores)):
#         for j in range(len(teamB_scores)):
#             if teamA_scores[i] <= teamB_scores[j]:
#                 count += 1
#     return count
#
#
# if __name__=="__main__":
#     teamA_scores = [1,2,3,]
#     teamB_scores = [2,4]
#     matches = count_matches(teamA_scores,teamB_scores)
#     print("A队在比赛中进球数少于或等于B队进球数的比赛总数：",matches)



# 法2
def compute_matches(teamA, teamB):
    matches = []
    for goalsB in teamB:
        count = 0
        for goalsA in teamA:
            if goalsA <= goalsB:
                count += 1
        matches.append(count)
    return matches

# 示例用法
teamA = [1, 2, 3]
teamB = [2, 4]
results = compute_matches(teamA, teamB)
print(results)
