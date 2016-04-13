#include "stdAfx.h"
#include "Assignment4.h"
#include <algorithm>

// Assignment4 Source File 
// Student Name: Feng Qingyuan
// UID: 3035029512

////////////////////////////////////////////////////////////////////////////////
// A brief description of C2DPoint and C3DPoint
//
// class C2DPoint
// {
// public:
//		double x; // stores the x coordinate
//		double y; // stores the y coordinate
// };
//
// class C3DPoint
// {
// public:
//		double x; // stores the x coordinate
//		double y; // stores the y coordinate
//		double z; // stores the z coordinate
// };
//
// Note:
// Although C2DPoint and C3DPoint do contain other data members,
// don't bother with them
//
double getDistSqr(double x1, double y1, double x2, double y2){
		double sqr = pow((x2-x1), 2.0) + pow((y2-y1), 2.0);
		return sqr;
	}

BOOL CCamera::Calibrate(const vector<C2DPoint*>& src2D, const vector<C3DPoint*>& src3D, 
						const vector<C2DPoint*>& corners, CMatrix<double>& matPrj)
{
	// INPUT:
	//     vector<C2DPoint*>& src2D      This contains a list of 2D coordinates for the image points specified 
	//                                   by the user in the image. Each point in this list is in 1-to-1 
	//                                   correspondence with the point having the same index in src3D.
	//
	//     vector<C3DPoint*>& src3D      This contains a list of 3D coordinates for the image points specified
	//                                   by the user in the image. Each point in this list is in 1-to-1 
	//                                   correspondence with the point having the same index in src2D.
	//
	//     vector<C2DPoint*>& corners    This contains a list of 2D coordinates for the detected corners.
	//
	// OUTPUT:
	//     CMatrix<double>& pPrjMatrix   A 3x4 camera projection matrix computed from the detected corners.
	//
	// Please refer to the tutorial for the usage of the related libraries.

	matPrj.SetSize(3,4,0);
	

	//////////////////////////
	// Begin your code here
	
	// Step 1: Classify the input 3D points into points on the x-z planes, points on
	//         the y-z plane, and points not on any calibration plane
	int length;
	//length denotes the length of vector src3D, i.e., the number of points specified by the user.
	//The following two vectors indicate whether a point in src3D belongs to XZ Plane, YZ plane or not.
	vector<boolean> onXZPlane;
	vector<boolean> onYZPlane;
	length = src3D.size();
	double x, y, z;
	for (int i = 0; i < length; i++){
		x = (*src3D[i]).x;
		y = (*src3D[i]).y;
		z = (*src3D[i]).z;
		if (y == 0.0){
			onXZPlane.push_back(true);
		}
		else
			onXZPlane.push_back(false);
		if (x == 0.0){
			onYZPlane.push_back(true);
		}
		else
			onYZPlane.push_back(false);
	}

	// Step 2: Estimate a plane-to-plane projectivity for each of the calibration planes
	//         using the input 2D/3D point pairs
	//First let's do with x-z plane projectivity.
	int n1=0, n2=0;
	//n1 is the number of points on xz plane, n2 is that on yz plane.
	for (int i = 0; i < length; i++){
		n1 = n1 + onXZPlane[i];
		n2 = n2 + onYZPlane[i];
	}
	//Now construct planar projection matrices for xz plane and yz plane repectively.
	CMatrix <double> A1(2*n1, 8, 0), A2(2*n2, 8, 0), b1(2*n1, 1, 0), b2(2*n2, 1, 0), Pxz1, Pyz1, Pxz(3, 3, 0), Pyz(3, 3, 0), A1plus(8, 2*n1, 0), A2plus(8, 2*n2, 0);
	// u1, d1(2*n1, 8), v1, u2, d2(2*n2, 8), v2;
	//now start filling A1 and A2 with elements.
	int i1 = 0, i2 = 0;
	//i1 counts the number of points in x-z plane. i2 counts that for y-z plane.
	double u,v;
	for (int i = 0; i < length; i++){
		if (onXZPlane[i] == 1){
			x = (*src3D[i]).x;
			z = (*src3D[i]).z;
			u = (*src2D[i]).x;
			v = (*src2D[i]).y;
			A1(i1*2, 0) = x;
			A1(i1*2, 1) = z;
			A1(i1*2, 2) = 1;
			A1(i1*2, 3) = A1(i1*2, 4) = A1(i1*2, 5) = 0;
			A1(i1*2, 6) = (-1)*x*u;
			A1(i1*2, 7) = (-1)*z*u;
			b1(i1*2, 0) = u;
			A1(i1*2+1, 0) = A1(i1*2+1, 1) = A1(i1*2+1, 2) = 0;
			A1(i1*2+1, 3) = x;
			A1(i1*2+1, 4) = z;
			A1(i1*2+1, 5) = 1;			
			A1(i1*2+1, 6) = (-1)*x*v;
			A1(i1*2+1, 7) = (-1)*z*v;
			b1(i1*2+1, 0) = v;
			i1++;
		}
		if (onYZPlane[i] == 1){
			y = (*src3D[i]).y;
			z = (*src3D[i]).z;
			u = (*src2D[i]).x;
			v = (*src2D[i]).y;
			A2(i2*2, 0) = y;
			A2(i2*2, 1) = z;
			A2(i2*2, 2) = 1;
			A2(i2*2, 3) = A2(i2*2, 4) = A2(i2*2, 5) = 0;
			A2(i2*2, 6) = (-1)*y*u;
			A2(i2*2, 7) = (-1)*z*u;
			b2(i2*2, 0) = u;
			A2(i2*2+1, 0) = A2(i2*2+1, 1) = A2(i2*2+1, 2) = 0;
			A2(i2*2+1, 3) = y;
			A2(i2*2+1, 4) = z;
			A2(i2*2+1, 5) = 1;			
			A2(i2*2+1, 6) = (-1)*y*v;
			A2(i2*2+1, 7) = (-1)*z*v;
			b2(i2*2+1, 0) = v;
			i2++;
		}
	}
	//Now A1 and A2 are both obtained. Let's do SVD decomposition.
	/*A1.SVD2(u1, d1, v1);
	A2.SVD2(u2, d2, v2);
	CMatrix <double> d1plus(8, 2*n1), d2plus(8, 2*n2), A1plus(8, 2*n1), A2plus(8, 2*n2);
	d1plus = (d1.Transpose()*d1).Inverse()*d1.Transpose();
	d2plus = (d2.Transpose()*d2).Inverse()*d2.Transpose();*/
	A1plus = (A1.Transpose()*A1).Inverse()*A1.Transpose();
	A2plus = (A2.Transpose()*A2).Inverse()*A2.Transpose();
	Pxz1 = A1plus*b1;
	Pyz1 = A2plus*b2;
	for (int i = 0; i < 8; i++){
		Pxz(i/3, i%3) = Pxz1(i, 0);
		Pyz(i/3, i%3) = Pyz1(i, 0);
	}
	Pxz(2, 2) = Pyz(2, 2) = 1;

	// Step 3: Using the estimated plane-to-plane projectivities, assign 3D coordinates
	//         to all the detected corners on the calibration pattern
	vector<C3DPoint*> D3Corners;
	double i3 = 0.5, j3;
	while (i3 <= 9.5){
		j3 = 0.5;
		while (j3 <= 7.5){
			//Here pPnt1 is a point on x-z plane. Likewise for pPnt2.
			C3DPoint* pPnt1 = new C3DPoint(i3, 0.0, j3);
			C3DPoint* pPnt2 = new C3DPoint(0.0, i3, j3);
			//So even index correspond to xz plane corners, odd index correspond to yz plane corners.
			D3Corners.push_back(pPnt1);
			D3Corners.push_back(pPnt2);
			j3 = j3 + 1;
		}
		i3 = i3 + 1;
	}
	//Now the two "corners" vectors store the 3D coordinates of corners.
	//We should find the pixel coordinates from corners for them.
	
	length = D3Corners.size();
	int cornerSize = corners.size(), index;
	vector<double> distSqr;
	vector<C2DPoint*> stdCorners;
	CMatrix <double> imgCoor(3, 1), wldCoor(3, 1);
	double squareDist;
	//This loop aims at finding the corresponding (u,v) coordinates of each corner in D3Corners.
	for (int i = 0; i < length; i++){
		distSqr.clear();
		if (i%2 == 0){
			//Even index, xz plane corners.
			wldCoor(0,0) = (*D3Corners[i]).x;
			wldCoor(1,0) = (*D3Corners[i]).z;
			wldCoor(2,0) = 1.0;
			imgCoor = Pxz*wldCoor;
			u = imgCoor(0,0)/imgCoor(2,0);
			v = imgCoor(1,0)/imgCoor(2,0);
			for (int j = 0; j < cornerSize; j++){
				squareDist = getDistSqr(u, v, (*corners[j]).x, (*corners[j]).y);
				distSqr.push_back(squareDist);
			}
			//Now we already get the squared distance between the calculated corner i and every corner detected.
			//Then we rank them and select the smallest one.
			vector<double>::iterator itr = min_element(distSqr.begin(), distSqr.end());
			index = itr - distSqr.begin();
			//index is the index of the element in corners which is closest to calculated u, v.
			C2DPoint* pPnt = new C2DPoint((*corners[index]).x, (*corners[index]).y);
			stdCorners.push_back(pPnt);
		}
		if (i%2 == 1){
			//Odd index, yz plane corners.
			wldCoor(0,0) = (*D3Corners[i]).y;
			wldCoor(1,0) = (*D3Corners[i]).z;
			wldCoor(2,0) = 1.0;
			imgCoor = Pyz*wldCoor;
			u = imgCoor(0,0)/imgCoor(2,0);
			v = imgCoor(1,0)/imgCoor(2,0);
			for (int j = 0; j < cornerSize; j++){
				squareDist = getDistSqr(u, v, (*corners[j]).x, (*corners[j]).y);
				distSqr.push_back(squareDist);
			}
			//Now we already get the squared distance between the calculated corner i and every corner detected.
			//Then we rank them and select the smallest one.
			vector<double>::iterator itr = min_element(distSqr.begin(), distSqr.end());
			index = itr - distSqr.begin();
			//index is the index of the element in corners which is closest to calculated u, v.
			C2DPoint* pPnt = new C2DPoint((*corners[index]).x, (*corners[index]).y);
			stdCorners.push_back(pPnt);
		}
	}
	//After the above steps, D3Corners stores the pointers to the 3D coordinates of corners, stdCorners stores the pointers
	//to the (u, v) coordinates of corners, elements with the same indices correspond exactly to each other.


	// Step 4: Estimate a 3x4 camera projection matrix from all the detected corners on
	//         the calibration pattern using linear least squares
	CMatrix<double> P(12, 1), A3(2*length, 12), U, D, V;
	for (int i = 0; i < length; i++){
		u = (*stdCorners[i]).x;
		v = (*stdCorners[i]).y;
		x = (*D3Corners[i]).x;
		y = (*D3Corners[i]).y;
		z = (*D3Corners[i]).z;
		A3(2*i, 11) = (-1)*u;
		A3(2*i+1, 11) = (-1)*v;
		A3(2*i, 0) = A3(2*i+1, 4) = x;
		A3(2*i, 1) = A3(2*i+1, 5) = y;
		A3(2*i, 2) = A3(2*i+1, 6) = z;
		A3(2*i, 3) = A3(2*i+1, 7) = 1.0;
		A3(2*i, 4) = A3(2*i, 5) = A3(2*i, 6) = A3(2*i, 7) = 0;
		A3(2*i+1, 0) = A3(2*i+1, 1) = A3(2*i+1, 2) = A3(2*i+1, 3) = 0;
		A3(2*i, 8) = (-1)*x*u;
		A3(2*i, 9) = (-1)*y*u;
		A3(2*i, 10) = (-1)*z*u;
		A3(2*i+1, 8) = (-1)*x*v;
		A3(2*i+1, 9) = (-1)*y*v;
		A3(2*i+1, 10) = (-1)*z*v;
	}
	A3.SVD2(U, D, V);
	//V is a 12*12 matrix
	P = V.SubMat(0, 11, 11, 11);
	for (int i = 0; i < 12; i++){
		P(i, 0) = P(i, 0)/P(11, 0);
		matPrj(i/4, i%4) = P(i, 0);
	}
	
	return TRUE;
}

void CCamera::Decompose(const CMatrix<double>& prjMatrix, CMatrix<double>& prjK, CMatrix<double>& prjRt)
{
	// INPUT:
	//     CMatrix<double>& prjMatrix    This is a 3x4 camera projection matrix to be decomposed.
	//
	// OUTPUT:
	//     CMatrix<double>& prjK         This is the 3x3 camera calibration matrix K.
	//
	//     CMatrix<double>& prjRt        This is the 3x4 matrix composed of the rigid body motion of the camera.
	//
	// Please refer to the tutorial for the usage of the related libraries.

	prjK.SetSize(3,3,0);
	prjRt.SetSize(3,4,0);

	//////////////////////////
	// Begin your code here
	
	// Step 1: Decompose the 3x3 sub-matrix composed of the first 3 columns of
	//         prjMatrix into the product of K and R using QR decomposition
	CMatrix<double> KR(3, 3), P3, Q, Rprime, K, R, T(3, 1);
	KR = prjMatrix.SubMat(0, 2, 0, 2);
	P3 = prjMatrix.SubMat(0, 2, 3, 3);
	KR.Transpose().QR2(Q, Rprime);
	R = Q.Transpose();
	K = Rprime.Transpose();
	//K is a 3*3 matrix.
	//If K00 is negative, multiply the 1st column of K and 1st row of R by -1.
	if (K(0, 0) < 0){
		for (int i = 0; i < 3; i++){
			K(i, 0) = (-1)*K(i, 0);
			R(0, i) = (-1)*R(0, i);
		}
	}
	//If K11 is negative, do it analogously for 2nd column of K and 2nd row of R.
	if (K(1, 1) < 0){
		for (int i = 0; i < 3; i++){
			K(i, 1) = (-1)*K(i, 1);
			R(1, i) = (-1)*R(1, i);
		}
	}
	//If both K02 and K12 are negative, do it similarly for 3rd col of K and 3rd row of R.
	if (K(0, 2) < 0 && K(1, 2) < 0){
		for (int i = 0; i < 3; i++){
			K(i, 2) = (-1)*K(i, 2);
			R(2, i) = (-1)*R(2, i);
		}
	}
	double alpha = K(2, 2);
	for(int i = 0; i < 9; i++){
		K(i/3, i%3) = K(i/3, i%3)/alpha;
	}

	// Step 2: Compute the translation vector T from the last column of prjMatrix
	T = (1/alpha)*K.Inverse()*P3;
	
	// Step 3: Normalize the 3x3 camera calibration matrix K
	// It is already done in step 1.
	prjK = K;
	for (int i = 0; i < 12; i++){
		if (i < 9)
			prjRt(i%3, i/3) = R(i%3, i/3);
		else
			prjRt(i%3, i/3) = T((i-9)%3, (i-9)/3);
	}

	return;
}

void CCamera::Triangulate(const vector<CMatrix<double>*>& prjMats, const vector<vector<C2DPoint*>*>& src2Ds,
							vector<C3DPoint*>& res3D)
{
	// INPUT:
	//     vector<CMatrix<double>*> prjMats 	A list of pointers to projection matrices
	//
	//     vector<vector<C2DPoint*>*> src2Ds	A list of image point lists, each image point list is in 1-to-1
	//                                          correspondence with the projection matrix having the same index in prjMats.
	//
	// OUTPUT:
	//     vector<C3DPoint*> res3D				A list of 3D coordinates for the triangulated points.
	//
	// Note:
	//    - src2Ds can be considered as a 2D array with each 'column' containing the image positions 
	//      for the same 3D point in different images. If any of the image does not contain the image for a particular
	//      point, the corresponding element in src2Ds will be a Null vector. For example, if there are two images, 
	//      and we know 8 pairs of corresponding points, then
	//      
	//			prjMats.size() = 2
	//			src2Ds.size() = 2
	//			src2Ds[k]->size() = 8           // k >= 0 and k < no. of images - 1
	//    
	//    - If for any reason the 3D coordinates corresponding to a 'column' in src2Ds cannot be computed,
	//      please push in a NULL as a place holder. That is, you have to make sure that each point in res3D
	//      must be in 1-to-1 correspondence with a column in src2Ds, i.e., 
	//      
	//			src2Ds[k]->size() == src3D.size()	// k >= 0 and k < no. of images - 1
	//
	// Please refer to the tutorial for the usage of related libraries.

	//////////////////////////
	// Begin your code here
	int imgCount = prjMats.size();
	int pntCount = (*src2Ds[0]).size(), valid;
	CMatrix<double> coord(4, 1), Prj, U, D, V;
	double x, y, z, u, v;
	//Set the rule: i is the index for a point, j is the index of projection matrix, or image.
	//We need to consider cases where there are not enough valid points for triangulation.
	for (int i = 0; i < pntCount; i++){
		valid = 0;
		CMatrix<double> Puv(2*imgCount, 4, 0);
		//"valid" means the number of valid 2D coordinates for a particular point.
		for (int j = 0; j < imgCount; j++){
			Prj = *prjMats[j];
			if ((*src2Ds[j])[i]!= NULL){
				//valid is also useful for subsetting the matrix to get rid of unfilled entries.
				valid++;
				u = (*src2Ds[j])[i]->x;
				v = (*src2Ds[j])[i]->y;
				//Fill in two rows of matrix Puv.
				for (int t = 0; t < 4; t++) {
					Puv((valid-1)*2, t) = Prj(0, t)-Prj(2,t)*u;
					Puv((valid-1)*2 + 1, t) = Prj(1, t) - Prj(2,t)*v;
				}
			}
		}
		if (valid < 2){
			//Not enough points to triangulate. Can only push back a null element.
			C3DPoint * pPnt = NULL;
			res3D.push_back(pPnt);
		}
		else{
			//>=2 valid points, could proceed to further calculation.
			Puv = Puv.SubMat(0, valid*2-1, 0, 3);
			Puv.SVD2(U, D, V);
			coord = V.SubMat(0, 3, 3, 3);
			x = coord(0, 0)/coord(3, 0);
			y = coord(1, 0)/coord(3, 0);
			z = coord(2, 0)/coord(3, 0);
			C3DPoint *pPnt = new C3DPoint(x, y, z);
			res3D.push_back(pPnt);
		}
	}

	return;
}
