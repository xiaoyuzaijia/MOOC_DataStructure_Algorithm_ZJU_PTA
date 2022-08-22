import math

MSize, N = map(int, input().split())
Hash_table = []
Hashvalue_l = []


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    if n%2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i == 0:
                return False
        return True

def hash_(key):
    if Hash_table[key%MSize] is None:
        Hash_table[key%MSize] = key
        return key%MSize
    else:
        i = 1
        while i <= MSize:
            rehash_value = key%MSize+int(math.pow(i,2))
            if Hash_table[rehash_value%MSize] is None:
                Hash_table[rehash_value%MSize] = key
                return rehash_value%MSize
            i += 1
        return '-'


if __name__ == "__main__":
    while not is_prime(MSize):
        MSize += 1
    
    Hash_table = [None for _ in range(MSize)]
    
    insert_l = list(map(int, input().split()))    # 去掉list()会导致最大测试点过不了,推测可能是数据量大的时候map对象迭代时会丢失原列表的顺序
    for key in insert_l:
        Hashvalue_l.append(hash_(key))
    
    print(' '.join(map(str, Hashvalue_l)))