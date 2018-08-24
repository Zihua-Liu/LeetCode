/*
 * [149] Max Points on a Line
 *
 * https://leetcode.com/problems/max-points-on-a-line/description/
 *
 * algorithms
 * Hard (15.22%)
 * Total Accepted:    99.1K
 * Total Submissions: 651.3K
 * Testcase Example:  '[[1,1],[2,2],[3,3]]'
 *
 * Given n points on a 2D plane, find the maximum number of points that lie on
 * the same straight line.
 * 
 * Example 1:
 * 
 * 
 * Input: [[1,1],[2,2],[3,3]]
 * Output: 3
 * Explanation:
 * ^
 * |
 * |        o
 * |     o
 * |  o  
 * +------------->
 * 0  1  2  3  4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 * Output: 4
 * Explanation:
 * ^
 * |
 * |  o
 * |     o        o
 * |        o
 * |  o        o
 * +------------------->
 * 0  1  2  3  4  5  6
 * 
 * 
 */
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point>& points) {
        if (points.empty()) return 0;
        int res = 1;
        for (int i = 0; i < points.size(); i ++ )
        {
            unordered_map<long double, int> map;
            int duplicates = 0, verticals = 1;

            for (int j = i + 1; j < points.size(); j ++ )
                if (points[i].x == points[j].x)
                {
                    verticals ++ ;
                    if (points[i].y == points[j].y) duplicates ++ ;
                }

            for (int j = i + 1; j < points.size(); j ++ )
                if (points[i].x != points[j].x)
                {
                    long double slope = (long double)(points[i].y - points[j].y) / (points[i].x - points[j].x);
                    if (map[slope] == 0) map[slope] = 2;
                    else map[slope] ++ ;
                    res = max(res, map[slope] + duplicates);
                }

            res = max(res, verticals);
        }
        return res;
    }
};

