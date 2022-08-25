Tsize = int(input())
Hash_value_d = {}
hash_table = [None for _ in range(Tsize)]

def hash_(key):
    i = 0
    while hash_table[(key%Tsize+i)%Tsize] is not None:
        i += 1
    return (key%Tsize+i)%Tsize

if __name__ == "__main__":
    keys_l = list(map(int, input().split()))
    for Hash_value, key in zip(range(Tsize), keys_l):
        if key >= 0:
            Hash_value_d[key] = Hash_value
    
    input_l = []
    keys_l = list(Hash_value_d.keys())
    keys_l.sort()
    while keys_l:                        # 直到所有的key都放进hash_table
        for key in keys_l:               # 每次都从还没放进hash_table的值中选最小的key出来
            value = hash_(key)
            if value == Hash_value_d[key]:    # 如果散列值刚好和原散列表的散列值相等
                hash_table[value] = key       # 就把key放入hash_table
                input_l.append(key)           # 记录顺序
                keys_l.remove(key)            # 去掉key
                break                         # break出来,下次再从最小的开始
            else:
                continue                      # 不相等就往后找次小的
    
    print(' '.join(map(str, input_l)))
