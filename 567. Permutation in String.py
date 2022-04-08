class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1 = ''.join(sorted(s1))
#         l1 , l2= len(s1), len(s2)
#         r1, r2 = 0, l1
        
#         while r2 <= l2:            
#             if s1  == ''.join(sorted(s2[r1:r2])):
#                 return True
#             r1+=1
#             r2+=1
#         return False
        #approach 2
        def checkInclusion(self, s1: str, s2: str) -> bool:
            hash1 = {}
            # for i in range(97,123):
            #     hash1[chr(i)] = 0
            for i in s1:                
                if i in hash1:
                    hash1[i] += 1
                else:
                    hash1[i] = 1
            # print(hash1)
            
            l1 , l2= len(s1), len(s2)
            r1, r2 = 0, l1
            while r2 <= l2:   
                hash2 = {}
                x = s2[r1 : r2]
                for i in range(r1,r2):
                    
                    if s2[i] in hash2:
                        hash2[s2[i]] += 1
                    else:
                        hash2[s2[i]] = 1                    
                c=0
                # for i in s1:
                #     if i not in hash2.keys():
                #         break
                #     elif hash1[i] == hash2[i]:
                #         c+=1
                # if c == l1:
                #     return True
                # or simply
                if hash1==hash2:
                    return True
                        
                r1+=1
                r2+=1
            return False