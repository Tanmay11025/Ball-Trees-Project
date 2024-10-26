#include <bits/stdc++.h>
#include "lib/classes/Point.cpp"
using namespace std;

/* Returns the Euclidean distance between two points. */
float EuclideanDistance(Point* A, Point* B) {
    float ed = 0.0f;
    for(int i = 0; i < DIMENSION; i++) {
        ed += pow(A->coordinate[i] - B->coordinate[i], 2);
    }
    return sqrt(ed);
}

/* Returns the Manhattan distance between two points. */
float ManhattanDistance(Point* A, Point* B) {
    float md = 0.0f;
    for(int i = 0; i < DIMENSION; i++) {
        md += abs(A->coordinate[i] - B->coordinate[i]);
    }
    return md;
}

/* Computes the median of a given set of points. */
Point* computeMedian(vector<Point*>& coordinateSet) {
    
    Point* median = new Point(); 
    int m = coordinateSet.size();
    vector<float> temp(m);
    
    for(int dim = 0; dim < DIMENSION; dim++) {
        for(int i = 0; i < m; i++) {
            temp[i] = coordinateSet[i]->coordinate[dim];
        }
        sort(temp.begin(), temp.end());

        if(m & 1) {
            median->coordinate[dim] = temp[m/2];
        }
        else {
            median->coordinate[dim] = (temp[m/2-1] + temp[m/2]) / 2;
        }
    }

    return median;
}

/* Returns the farthest point from a given point in a set as pair (Point,Distance). */
pair<Point*,float> findFarthestPoint(vector<Point*> univSet, Point* P) {
    pair<Point*,float> result;
    float maxDist = 0;
    float m;
    for(int i = 0; i < univSet.size(); i++) {
        m = max(maxDist, EuclideanDistance(P, univSet[i]));
        if(m > maxDist) {
            result.first = univSet[i];
            maxDist = m;
        }
    }
    result.second = maxDist;
    return result;
}

