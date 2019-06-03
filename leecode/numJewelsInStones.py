# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 下午4:35
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows

# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:


# class Solution:
#     def numJewelsInStones(self , J , S):
#         num = 0
#         for i in S:
#             if i in J:
#                 num += 1
#         return num
#
# class Solution:
#     def numJewelsInStones(self , J , S):
#         return sum(S.count(i) for i in J)
#
# class Solution:
#     def numJewelsInStones(self , J , S):
#         q = list(J)
#         w = list(S)
#         u = 0
#         for i in q:
#             for r in w:
#                 if i == r: u += 1
#         return u
#
#
# J = "aA"
# S = "aAAbbbb"
# print(Solution().numJewelsInStones(J , S))

# alist= [22,21,34,65,12,89,3,9,66]
#
# def qucik_sort(alist,low, high):
#     # 退出递归条件
#     # left=right
#     while low>high:
#         return alist
#
#     left = low
#     right = high
#     base_value = alist[right]
#
#     while left < right:
#         while left<right and alist[left] < base_value:
#             left += 1
#         # 跳出循环条件
#         # alist[left]>=base_value
#         alist[right]=alist[left]
#         while right>left and alist[right]>base_value:
#             right -= 1
#         # 跳出循环条件
#         # alist[right]<=base_value
#         alist[left]=alist[right]
#     # 把基准值赋值给游标停留的元素
#     alist[right] = base_value
#   # 继续对游标左右的队列递归快速排序
#     qucik_sort(alist,low,left-1)
#     qucik_sort(alist,left+1,len(alist)-1)
#     print(alist)
#
# if __name__ == '__main__':
#
#     low = 0
#     high = len(alist)-1
#     qucik_sort(alist,low,high)


# class Solution:
#     def flipAndInvertImage(self, A):
#         B = []
#         for row in A:
#             len_row = len(row)
#             tmp = list(range(len_row))
#             for i in range(len_row):
#                 result = row[len_row-i-1]
#                 result = 1 if (result ==0) else 0
#                 tmp[i] = result
#
#             B.append(tmp)
#         return B
#
# A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# print Solution().flipAndInvertImage(A)

# class Solution:
#     def uniqueMorseRepresentations(self, words):
#         table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#         tmp = []
#         for i in words:
#             code_tmp = ''
#             for j in i:
#                 code = table[ord(j)-97]
#                 code_tmp += code
#             tmp.append(code_tmp)
#
#         return len(set(tmp))
#
# words = ["gin", "zen", "gig", "msg"]
# print Solution().uniqueMorseRepresentations(words)

# class Solution:
#     def numUniqueEmails(self, emails):
#         result = []
#         for i in emails:
#             tmp = i.split('+')[0].replace('.','') + '@' +i.split('+')[-1].split('@')[-1]
#             result.append(tmp)
#
#         return len(set(result))
#
#
# class Solution:
#     def numUniqueEmails(self, emails):
#         return len(set([i.split('+')[0].replace('.','') + '@' +i.split('+')[-1].split('@')[-1] for i in emails]))
#
#
# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# print Solution().numUniqueEmails(emails)


# class Solution:
#     def sortArrayByParity(self, A):
#         return [i for i in A if i%2 ==0 ]+ [i for i in A if i%2 ==1 ]


# class Solution:
#     def repeatedNTimes(self, A):
#         dict = {}
#         for num in A:
#             try:
#                 dict[num] += 1
#                 if dict[num] >= len(A)/2:
#                     return num
#             except:
#                 dict[num] = 1
# A = [1,2,3,3]
# Solution().repeatedNTimes(A)


# class Solution:
#     def judgeCircle(self, moves):
#         U_count = moves.count("U")
#         D_count = moves.count("D")
#         L_count = moves.count("L")
#         R_count = moves.count("R")
#         if U_count - D_count == 0 and L_count - R_count == 0:
#             return True
#         else:
#             return False
#
# Solution().judgeCircle("UD")

# class Solution:
#     def hammingDistance(self, x , y):
#         return bin(x^y).count('1')
#
#
# print Solution().hammingDistance(1,4)

# class Solution:
#     def mergeTrees(self, t1, t2):
# class Solution:
#     def mergeTrees(self, t1, t2):
#         if t1 and t2:
#             t1.val += t2.val
#             t1.left = self.mergeTrees(t1.left , t2.left)
#             t1.right = self.mergeTrees(t1.right , t2.right)
#             return t1
#         return t1 or t2
#
# t1 = [1,3,2,5]
# t2 = [2,1,3,None,4,None,7]
# print  Solution().mergeTrees(t1 , t2)

# def feb(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return feb(n-1) + feb(n-2)
#
# print feb(6)
#
#
#
# def cheng(n):
#     if n == 1:
#         return 1
#     return n*cheng(n-1)
#
# print cheng(5)

# class Solution:
#     def minDeletionSize(self, A):
#         count = 0
#         for i in range(len(A[1])):
#             tmp = [j[i] for j in A]
#             for j in range(len(tmp)):
#                 if j+1 == len(tmp):
#                     break
#                 if ord(tmp[j]) > ord(tmp[j+1]):
#                     count += 1
#                     break
#         return count
#
# print Solution().minDeletionSize(["rrjk","furt","guzm"])

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         def rec(root):
#             if not root:
#                 return res
#             res.append(root.val)
#             for c in root.children:
#                 rec(c)
#             return res
#         rec(root)
#         return res
#
# class Solution:
#     result = []
#     def preorder(self, root: 'Node') -> List[int]:
#         print("root" , root)
#         if root == None:
#             return []
#         self.result.append(root.val)
#         for i in root.children:
#             self.preorder(i)
#         return self.result if self.result else []

# class Solution:
#     def sortArrayByParityII(self, A):
#         tmp = [i for i in A if i%2 == 1]
#         tmp2 = [i for i in A if i%2 == 0]
#         print(tmp , tmp2)
#         _ = []
#         for i in range(len(A)):
#             if i%2 == 1:
#                 _.append(tmp.pop())
#             else:
#                 _.append(tmp2.pop())
#         return _
#
# from itertools import chain
#
# class Solution:
#     def sortArrayByParityII(self, A):
#         """
#         :type A: List[int]
#         :rtype: List[int]
#         """
#         odd = []
#         even = []
#         for i in A:
#             if i & 1:
#                 even.append(i)
#             else:
#                 odd.append(i)
#         print(odd , even)
#         print(chain(*zip(odd, even)))
#         return list(chain(*zip(odd, even)))
#
#
# A = [4,2,5,7]
# print Solution().sortArrayByParityII(A)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         result = []
#
#         def fn(root):
#             if root == None:
#                 return
#             for i in root.children:
#                 fn(i)
#                 result.append(i.val)
#
#         fn(root)
#         if root:
#             result.append(root.val)
#         return result
#
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         result = []
#
#         def fn(root):
#             if root == None:
#                 return
#             for i in root.children:
#                 fn(i)
#             result.append(root.val)
#
#         fn(root)
#         return result
#
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         result = []
#
#         def explore(root):
#             if root != None:
#                 for c in root.children:
#                     explore(c)
#                 result.append(root.val)
#
#         explore(root)
#         return result

# class Solution:
#     def selfDividingNumbers(self, left, right):
#         result = []
#         for num in range(left , right+1):
#             if '0' not in str(num):
#                 tmp = [num%int(i)==0 for i in str(num)]
#                 print num , tmp
#                 if 1 in tmp and 0 not in tmp:
#                     result.append(num)
#         return result
# print Solution().selfDividingNumbers(47 , 85)

# class Solution(object):
#     def canWinNim(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """

#
# class Solution(object):
#     def sumEvenAfterQueries(self, A, queries):
#         """
#         :type A: List[int]
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
#         result = []
#         for i in range(len(A)):
#             val = queries[i][0]
#             index = queries[i][1]
#             A[index] += val
#             result.append(sum([i for i in A if i&1 == 0]))
#         return result

# class Solution(object):
#     def sumEvenAfterQueries(self, A, queries):
#         result = []
#         pre_data = 0
#         for i in range(len(A)):
#             val = queries[i][0]
#             index = queries[i][1]
#             old_val = A[index]
#             A[index] += val
#             new_val = old_val + val
#             if i == 0:
#                 pre_data = sum([i for i in A if i&1 == 0])
#             else:
#                 if old_val &1 ==0 and new_val&1 == 0:
#                     pre_data += (new_val-old_val)
#                 if old_val&1 == 1 and new_val&1 == 1:
#                     pass
#                 if old_val&1 == 0 and new_val&1 == 1:
#                     pre_data -= old_val
#                 if old_val&1 == 1 and new_val&1 == 0:
#                     pre_data += new_val
#             result.append(pre_data)
#         return result
#
#
# A =[1,2,3,4]
# queries =[[1,0],[-3,1],[-4,0],[2,3]]
# print Solution().sumEvenAfterQueries(A , queries)

# class RecentCounter(object):
#
#     def __init__(self):
#
#     def ping(self, t):
#         """
#         :type t: int
#         :rtype: int
#         """

# class RecentCounter(object):
#
#     def __init__(self):
#         self.l = []
#
#     def ping(self, t):
#         if not t:
#             return None
#         self.l.append(t)
#         tmp = 0
#         split_index = 0
#         for index , val in enumerate(self.l):
#             if val >= t - 3000 and val <= t:
#                 tmp += 1
#             if val < t-3000:
#                 split_index = index
#         self.l = self.l[split_index:]
#         return tmp
#
# # 以下是测试用例，及测试方法
# obj = RecentCounter()
# test = [[],[1],[100],[3001],[3002]]
# tmp = []
# for i in test:
#         tmp.append(obj.ping(i[0]) if i else obj.ping(None))
# print "-------"
# print tmp
# """
# 题很难读懂，因为有一些干扰性的东西（也可能是我的理解不对），以下为我的理解：示例输入的第一个inputs = ["RecentCounter","ping","ping","ping","ping"]我把它忽略掉了，感觉没有用。
# 第二个inputs是多个时间，实例化一次对象后，调用多次方法，参数t为这些时间。ping方法内部将每次的t都存在一个list里，下次调用ping方法时，要用到这个list，即统计这个list中 t-3000<=i<=t 的元素的个数，并返回。
# 将每次调用返回的结果存入一个数组中，就是最后的结果。
# """



# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         for i in range(len(s)/2):
#             tmp = s[i]
#             s[i] = s[len(s)-i-1]
#             s[len(s)-i-1] = tmp
#         return s
#
# print Solution().reverseString(["h","e","l","l","o"])


# class Solution(object):
#     def findWords(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         q_line = 'qwertyuiopQWERTYUIOP'
#         a_line = 'asdfghjklASDFGHJKL'
#         z_line = 'zxcvbnmZXCVBNM'
#         line_list = [q_line , a_line , z_line]
#         result = []
#         for word in words:
#             line = word[0]
#             this_line = [i for i in line_list if line in i][0]
#             tmp = True
#             for key in word:
#                 if key not in this_line:
#                     tmp = False
#                     break
#             if tmp:
#                 result.append(word)
#         return result

# class Solution(object):
#     def arrayPairSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # 似乎是要找最小的配对？
#         for i in enumerate


# class Solution(object):
#     def titleToNumber(self, s):
#         res = 0
#         for i,j in enumerate(s):
#             res += (ord(j) - ord('A')) *(len(s)-1)


