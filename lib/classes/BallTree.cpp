#ifndef BLT
#define BLT

#include <bits/stdc++.h>
#include "BallTreeNode.cpp"
using namespace std;

class BallTree {
private:
    void setTreeDepth(BallTreeNode* root, int dep) {
        if(root == NULL) {
            if(dep > this->depth) {
                this->depth = dep-1;
            }
            return;
        }
        setTreeDepth(root->left, dep+1);
        setTreeDepth(root->right, dep+1);
    }

public:
    BallTreeNode* root;
    int depth;

    BallTree() {
        root = NULL;
        depth = 0;
    }

    int getTreeDepth() {
        setTreeDepth(root, 0);
        return depth;
    }
};

#endif