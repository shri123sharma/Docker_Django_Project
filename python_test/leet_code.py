# list1 = [1,2,4]
# list2 = [1,3,4]
# list1=[]
# list2=[]
# list1=[]
# list2=[0]
# # Output: [1,1,2,3,4,4]
# list1.extend(list2)
# list1.sort()
# print(list1)

# Example 1:
# nums = [2,2,1]
# Output: 1
# Example 2:

# nums = [4,1,2,1,2]
# l1=[]
# for i in  nums:
#     if nums.count(i)==1:
#         print(i)

# nums=[4,1,2,1,2]
# d1={}
# count=0
# min_key=None
# for i in nums:
#     if i not in d1:
#         d1[i]=1
#     else:
#         d1[i]+=1
        
# for k,v in d1.items():
#     if v==1:
#         print(k)

# s ="bbbaaaba"
# s1=len(set(list(s)))
# t="aaabbbba"
# s2=len(set(list(t)))
# s3=len(set(zip(s,t)))
# print(s1==s3==s2)

# nums = [1,2,3,1]
# k = 3
# for i in range(len(nums)):
#     print(nums[i])
#     for j in range(i+1,len(nums)):
#         print(nums[i+1])
#         if nums[i]==nums[j] and abs(i-j)<=k:
#             print(True)
#         else:
#             print(False)

n=1
if n**2==0:
    print('true')
else:
    print('false')

