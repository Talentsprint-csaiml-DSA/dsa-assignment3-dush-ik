import heapq

class Node:
  def __init__ (self, char, freq):
    self.freq = freq
    self.char = char
    self.left = None
    self.right = None
  
  def __lt__(self, other):
    return self.freq < other.freq


def build_huffman_tree (freq_map):
  heap = []
  for char, freq in freq_map.items():
    heapq.heappush(heap, Node(char, freq))

  while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    merged = Node(None, left.freq + right.freq)
    merged.left = left
    merged.right = right
    heapq.heappush(heap, merged)
  return heap[0]

def generate_codes(node, prefix="", code_map={}):
  if node.left == None and node.right == None:
    code_map[node.char] = prefix
  else:
    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)
  return code_map

def build_freq_map (string):
  freq_map = {}
  for char in string:
    if char in freq_map:
      freq_map[char] = freq_map[char] + 1
    else:
      freq_map[char] = 1
  return freq_map

def huffman_coding (string):
  freq_map = build_freq_map(string)
  
  root = build_huffman_tree(freq_map)
  code_map = generate_codes(root)
  return ''.join(code_map.values())