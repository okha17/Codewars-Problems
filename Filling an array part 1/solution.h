#include <vector>

std::vector<int> arr(int n = 0) {
  if (n < 0)
  {
    return {};
  }
  else if (n == 0)
  {
    return {};
  }
  std::vector<int> myarray;
  for (int i = 0; i <n; i++)
  {
    myarray.push_back(i);
  }
  return myarray;
  // the numbers 0 to N-1
}