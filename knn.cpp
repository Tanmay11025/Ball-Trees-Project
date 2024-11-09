#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <limits>
#include <algorithm>
#include <fstream>
#include <sstream>
#include "point.h"
#include "node.h"
#include "construct.h"
#include "NN.h"
#include <bits/stdc++.h>

vector<Point> loadPointsFromCSV(const string &filename, int dimensions);

// Function to load points from a CSV file
vector<Point> loadPointsFromCSV(const string &filename, int dimensions) {
    vector<Point> points;
    ifstream file(filename);
    string line;

    while (getline(file, line)) {
        stringstream ss(line);
        string value;
        Point point(dimensions);
        int i = 0;
        
        // Read each comma-separated value
        while (getline(ss, value, ',') && i < dimensions) {
            point.coords[i++] = stod(value);  // Convert string to double and store
        }

        if (i == dimensions)  // Only add the point if it has the correct number of dimensions
            points.push_back(point);
    }
    
    return points;
}

int main() {
    int dimensions = 2;
    int k = 5;
    int leafSize = 5;

    // Load points from a CSV file
    vector<Point> points = loadPointsFromCSV("points.csv", dimensions);
    if (points.empty()) {
        cout << "Error: CSV file is empty or not formatted correctly.\n";
        return -1;
    }

    // Build the ball tree
    BallTreeNode *root = buildBallTree(points, leafSize, 0);

    // Query point
    Point query(dimensions);
    query.coords = {50, 50};  // Example query point coordinates

    // Find k-nearest neighbors
    vector<Point> neighbors = findKNearestNeighbors(root, query, k);

    // Output results
    cout << "Query Point: (" << query.coords[0] << ", " << query.coords[1] << ")\n";
    cout << "k-Nearest Neighbors:\n";
    for (const auto &neighbor : neighbors) {
        cout << "(" << neighbor.coords[0] << ", " << neighbor.coords[1] << ")\n";
    }

    return 0;
}



