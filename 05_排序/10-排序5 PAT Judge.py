N, K, M = map(int, input().split())
full_mark_l = list(map(int, input().split()))
user_info = {}
rank_l = []

if __name__ == "__main__":
    for _ in range(M):
        id_, p, s = map(int, input().split())
        p -= 1
        if id_ not in user_info:
            user_info[id_] = [None for _ in range(K)]
        if user_info[id_][p] is None:
            user_info[id_][p] = s
        elif user_info[id_][p] < s:
            user_info[id_][p] = s
    
    for id_ in user_info.keys():
        score_l = user_info[id_].copy()
        perfect_p_nums = 0
        for i in range(K):
            if score_l[i] == full_mark_l[i]:
                perfect_p_nums += 1
        
        score_l = list(filter(lambda x: x is not None, score_l)) # 去掉score_l中的None
        if all(i == -1 for i in  score_l):                       # 没有一个提交通过编译的人不进入排名
            continue
        
        score_l = [(0 if i == -1 else i) for i in score_l]        # 把未通过编译的-1换成0,表示这题得0分
        rank_l.append((-sum(score_l), -perfect_p_nums, id_))

    rank_l.sort()
    
    rank = 1
    last_score = -rank_l[0][0]
    same_rank_nums = 0
    for line in rank_l:
        score, id_ = -line[0], line[2]
        if score == last_score:
            print(rank, f"{id_:05d}", score, ' '.join(map(str, user_info[id_])).replace("None", '-').replace('-1', '0'))
            same_rank_nums += 1
        else:
            rank += same_rank_nums
            print(rank, f"{id_:05d}", score, ' '.join(map(str, user_info[id_])).replace("None", '-').replace('-1', '0'))
            same_rank_nums = 1
        last_score = score


'''
4 最大随机测试，有满分的题目重复提交 运行超时 0 -- 5028 KB
'''