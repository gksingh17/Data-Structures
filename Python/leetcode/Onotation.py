
print('''''''O(n^2)''''''')
print('Traverse a square grid ')
nums = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])

print('get every pair of elements in array') 
numspair = [1,2,3,4]
for i in range(len(numspair)):
    for j in range(i+1, len(numspair)):
        print(numspair[i], numspair[j])


print('''''''O(n*m)''''''')
print('get every pair of elements from two arrays') 
nums1, nums2 = [1,2,3] , [4,5]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        print(nums1[i], nums2[j])

print('traverse rectangle grid')
numsrec =[[1,2,3], [4,5,6]]
for i in range(len(numsrec)):
    for j in range(len(numsrec[i])):
        print(numsrec[i][j])

print('''''''O(n^3)''''''')
print('Get every triplet of elements in array')
numscube = [1,2,3]
for i in range(len(numscube)):
    for j in range(i+1, len(numscube)):
        for k in range(j + 1, len(numscube)):
            print(numscube[i], numscube[j], numscube[k])
  




