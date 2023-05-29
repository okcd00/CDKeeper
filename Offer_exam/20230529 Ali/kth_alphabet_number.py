
#      root
#  0 1(? counts) 2v 3 4 5 6 7 8 9
#  0 1 2v 3 4 5 6 7 8 9
#  0 1v ... 9
#  0 1 2 3


def get_counts(cur_node_index, max_node_count):
  # return how many nodes in this subtree
  # 10 - 19, 100 - 199, 1000 - 1999
  # 20 + 
  ret = 0
  lef, rig = cur_node_index, cur_node_index
  while lef < max_node_count:
    ret += rig - lef + 1 if rig < max_node_count \
      else max_node_count - lef + 1
    lef *= 10
    rig *= 10
    rig += 9
  return ret

def get_kth_number(n, k):
  if k == 1:
    return 0

  cur = 1 
  k -= 1  # 第 1 小是 index 0
  while k > 0:
    counts = get_counts(cur, n) 
    print(counts, "at", k)
    if counts <= k:
      k -= counts  # drop all candidates in this subtree
      cur += 1
    else:
      cur *= 10
      k -= 1
  return cur


if __name__ == "__main__":
  n = 100
  k = 5  # 1 10 11 12 13
  print(get_kth_number(n, k))
  