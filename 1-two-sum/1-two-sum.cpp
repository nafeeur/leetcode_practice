class Solution {
public:
vector<int> twoSum(vector<int>& nums, int target) {
      map<int, int> map;
      vector<int> pairs;
      for(int i = 0; i < nums.size(); i++) {
          int comp = target - nums[i];
          if(map.find(comp) != map.end()) {
              pairs.push_back(map.find(comp)->second);
              pairs.push_back(i);
              break;
          }
          map.insert(pair<int, int>(nums[i], i));
      }
      return pairs;
}
};