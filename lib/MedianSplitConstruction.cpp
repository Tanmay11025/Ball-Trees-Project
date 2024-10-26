#include <bits/stdc++.h>
#include "classes/BallTree.cpp"
#include "util/mathematicalFunctions.cpp"
using namespace std;

// creates a ball tree from a root containing all points
void constructBallTree(BallTreeNode* root, vector<Point*> univSet) {

    // return if set size falls below threshold
    if(univSet.size() <= LEAF_POINT_COUNT_THRESHOLD) {
        return;
    }

    //compute median
    Point* median = computeMedian(univSet);

    //find farthest point from median say p1
    Point* P1 = findFarthestPoint(univSet, median).first;

    //find farthest point from p1, say p2
    Point* P2 = findFarthestPoint(univSet, P1).first;

    // delete median, no longer required
    delete median;

    //create ball around p1 and p2
    BallTreeNode* leftChild = root->left = new BallTreeNode();
    leftChild->parent = root;
    BallTreeNode* rightChild =  root->right = new BallTreeNode();
    rightChild->parent = root;

    //assign points
    for(int i = 0; i < univSet.size(); i++) {
        if(EuclideanDistance(univSet[i], P1) <= EuclideanDistance(univSet[i], P2)) {
            leftChild->ball->containedPoints.push_back(univSet[i]);
        }
        else {
            rightChild->ball->containedPoints.push_back(univSet[i]);
        }
    }
    
    //resize leftChild ball
    Point* leftChildBallMedian = computeMedian(leftChild->ball->containedPoints);
    leftChild->ball->center = leftChildBallMedian;
    leftChild->ball->radius = findFarthestPoint(leftChild->ball->containedPoints, leftChildBallMedian).second;
    
    //resize rightChild ball
    Point* rightChildBallMedian = computeMedian(rightChild->ball->containedPoints);
    rightChild->ball->center = rightChildBallMedian;
    rightChild->ball->radius = findFarthestPoint(rightChild->ball->containedPoints, rightChildBallMedian).second;

    // recursively continue the process until threshold is met
    constructBallTree(leftChild, leftChild->ball->containedPoints);
    constructBallTree(rightChild, rightChild->ball->containedPoints);
}


BallTreeNode* initialiseRootNode(BallTreeNode* root, vector<Point*> completePointSet) {
    root = new BallTreeNode(completePointSet);
    return root;
}





