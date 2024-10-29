#include <bits/stdc++.h>
#include "lib/classes/Point.cpp"
using namespace std;

/* Returns the Euclidean distance between two points. */
float EuclideanDistance(const Point* A, const Point* B) {
    float ed = 0.0f;
    for(int i = 0; i < DIMENSION; i++) {
        ed += pow(A->coordinate[i] - B->coordinate[i], 2);
    }
    return sqrt(ed);
}

/* Returns the Manhattan distance between two points. */
float ManhattanDistance(const Point* A, const Point* B) {
    float md = 0.0f;
    for(int i = 0; i < DIMENSION; i++) {
        md += abs(A->coordinate[i] - B->coordinate[i]);
    }
    return md;
}

/* Returns the mean point of a given set of points. */
Point* computeMean(const vector<Point*>& coordinateSet) {
    Point* mean = new Point();
    int pointCount = coordinateSet.size();
    float sum;

    for(int dim = 0; dim < DIMENSION; dim++) {
        sum = 0;
        for(int i = 0; i < pointCount; i++) {
            sum += coordinateSet[i]->coordinate[dim];
        }
        sum /= pointCount;
        mean->coordinate[dim] = sum;
    }
    return mean;
}

/* Returns the median point of a given set of points. */
Point* computeMedian(const vector<Point*>& coordinateSet) {
    
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
pair<Point*,float> findFarthestPoint(const vector<Point*> univSet, const Point* P) {
    pair<Point*,float> result;
    float m, maxDist = 0;
    
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


/* Returns the set of points shifted to have the pivot as the origin. */
vector<Point*> shiftOrigin(vector<Point*>& coordinateSet, const Point* pivot) {
    for(int i = 0; i < coordinateSet.size(); i++) {
        for(int dim = 0; dim < DIMENSION; dim++) {
            coordinateSet[i]->coordinate[dim] -= pivot->coordinate[dim];
        }
    }
    return coordinateSet;
}


/* Returns the multiplication of two matrices. */
vector<vector<float>> multiplyMatrices(const vector<vector<float>>& mat1, const vector<vector<float>>& mat2) {

    int rows1 = mat1.size();
    int cols1 = mat1[0].size();
    int rows2 = mat2.size();
    int cols2 = mat2[0].size();

    // Check if multiplication is possible (number of columns in mat1 == number of rows in mat2)
    if (cols1 != rows2) {
        throw invalid_argument("Matrix dimensions do not match for multiplication.");
        // return NULL;
    }

    vector<vector<float>> result(rows1, vector<float>(cols2, 0.0));

    for (int i = 0; i < rows1; ++i) {
        for (int j = 0; j < cols2; ++j) {
            for (int k = 0; k < cols1; ++k) {
                result[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }

    return result;
}

/* Returns a matrix multiplied by specified scalar. */
vector<vector<float>> multiplyMatrixWithScalar(vector<vector<float>> mat, float num) {
    vector<vector<float>> result(mat);
    for(int i = 0; i < mat.size(); i++) {
        for(int j = 0; j < mat[0].size(); j++) {
            mat[i][j] *= num;
        }
    }
    return result;
}

/* Returns the transpose of a given matrix. */
vector<vector<float>> transposeMatrix(const vector<vector<float>>& mat) {
    
    int rows = mat.size();
    int cols = mat[0].size();
    vector<vector<float>> transpose(cols, vector<float>(rows, 0.0));
    
    for(int i = 0; i < rows; rows++) {
        for(int dim = 0; dim < DIMENSION; dim++) {
            transpose[dim][i] = mat[i][dim];
        }
    }

    return transpose;
}


/* Returns the matrix representation of a dataset. */
vector<vector<float>> createMatrix(const vector<Point*>& coordinateSet) {
    vector<vector<float>> mat;

    for(int i = 0; i < coordinateSet.size(); i++) {
        for(int dim = 0; dim < DIMENSION; dim++) {
            mat[i].push_back(coordinateSet[i]->coordinate[dim]);
        }
    }

    return mat;
}


/* Computes the covariance of a dataset in n-dimensional space. WARNING: This method may be incorrect. */
vector<vector<float>> computeCovarianceMatrixOfNFeatures(vector<Point*> coordinateSet, const Point* mean) {
    if(DIMENSION == 1) {
        cout << "INVALID DIMENSION." << endl;
        return {{}};
    }
    
    // obtain mean-centered dataset
    coordinateSet = shiftOrigin(coordinateSet, computeMean(coordinateSet));

    // compute the covariance matrix using S = 1/n-1 . D^T.D, WARNING: FORMULA NOT VERIFIED.
    vector<vector<float>> D = createMatrix(coordinateSet);
    vector<vector<float>> DT = transposeMatrix(D);

    vector<vector<float>> covarianceMatrix = multiplyMatrices(DT, D);
    covarianceMatrix = multiplyMatrixWithScalar(covarianceMatrix, 1/DIMENSION-1);

    return covarianceMatrix;
}


vector<vector<float>> computeCovarianceMatrix(vector<Point*> coordinateSet, const Point* mean) {

}

/* Returns the standard deviation of the given set of points. */
float computeStandardDeviation(vector<Point*> coordinateSet, const Point* mean) {


}
