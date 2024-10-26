#include <bits/stdc++.h>
#include "Point.cpp"
using namespace std;

class Ball {
public:
    vector<Point*> containedPoints;
    float radius;
    Point* center;

    Ball() {
        // is this rlly necessary??
    }

    Ball(vector<Point*> pointSet) {
        containedPoints = pointSet;
    }

    Ball(Point* center, float radius) {
        this->center = center;
        this->radius = radius;
    }
};