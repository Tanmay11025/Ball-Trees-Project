#ifndef BLTN
#define BLTN
#include <bits/stdc++.h>
#include "Ball.cpp"
using namespace std;

class BallTreeNode {
public:
    Ball* ball;
    BallTreeNode* left;
    BallTreeNode* right;
    BallTreeNode* parent;

    BallTreeNode(vector<Point*> pointSet) {
        ball = new Ball(pointSet);
        left = right = parent = NULL;
    }

    BallTreeNode(Ball* b) {
        ball = b;
        left = right = parent = NULL;
    }
    
    BallTreeNode() {
        ball = new Ball();
        left = right = parent = NULL;
    }
};

#endif