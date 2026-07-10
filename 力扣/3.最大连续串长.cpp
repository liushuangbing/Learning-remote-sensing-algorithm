#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        for (int i = 0; i < nums.size(); i++) {
            st.insert(nums[i]);
        }
        int maxLen = 0;
        // 补充int类型
        for (int num : st) {
            // num‑1不存在说明是序列起点
            if (st.find(num - 1) == st.end()) {
                int count = 1;
                int target = num;
                while (st.find(target + 1) != st.end()) {
                    count++;
                    target++;
                }
                if (count > maxLen) {
                    maxLen = count;
                }
            }
        }
        return maxLen;
    }
};
