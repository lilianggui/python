import operator


with(open('article.txt', 'r+')) as f:
    count_map = {}
    while 1:
        line = f.readline()
        if not line:
            break
        else:
            strs = line.strip('\n').split()
            for s in strs:
                count = count_map.get(s)
                if count:
                    count_map[s] = count+1
                else:
                    count_map.setdefault(s, 1)
    count_map = sorted(count_map.items(), key=operator.itemgetter(1), reverse=True)
    for kv in count_map:
        print(kv[0], kv[1])

