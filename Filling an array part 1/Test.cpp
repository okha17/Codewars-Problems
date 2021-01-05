#include <vector>
typedef std::vector<int> V;

Describe(Example_Tests)
{
    It(example_tests)
    {
        Assert::That(arr(), Equals(V {} ));
        Assert::That(arr(4), Equals( V{0,1,2,3} ));
    }
};
