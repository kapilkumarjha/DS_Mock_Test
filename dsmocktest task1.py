# def move_zero(nums):
#  n = len(nums)
#  j = 0
#  for i in range(n):
#   if nums[i] != 0:
#    nums[i], nums[j] = nums[j], nums[i]
#    j += 1
#
# nums = [0,1,0,3,12]
# move_zero(nums)
# print(nums)
############################################################################################################################
def firstUniqChar(s):
 char_freq = {}
 for char in s:
  char_freq[char] = char_freq.get(char, 0) + 1

 for i, char in enumerate(s):
  if char_freq[char] == 1:
   return i

 return -1

s = "leetcode"
print(firstUniqChar(s))

s = "loveleetcode"
print(firstUniqChar(s))

s = "aabbcc"
print(firstUniqChar(s))
