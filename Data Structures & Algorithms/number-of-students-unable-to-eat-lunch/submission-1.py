# Frequency Implementation

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total_num = len(students)
        cnt = Counter(students)
        remain = total_num

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                remain -=  1
                cnt[sandwich] -= 1
            else:
                break

        return remain

