#pragma once

// header inclusion
#include "math.h"
#include "Matrix.h"
#include <vector>
using namespace std;

#include "2DPointMap.h"
#include "3DPointMap.h"

// some constants
#define CALIBRATION_FUZZINESS 16.0
#define ALIGN_FUZZINESS	64.0

//////////////////////////////////////////////////////////
// IMPORTANT! DO NOT modify the declaration of CCamera! //
//////////////////////////////////////////////////////////


// CCamera class's declaration
class __declspec(dllexport) CCamera
{
public:
	// camera calibration using a calibration grid
	virtual BOOL Calibrate(const vector<C2DPoint*>& src2D,
		                     const vector<C3DPoint*>& src3D,
							 const vector<C2DPoint*>& corners,
							 CMatrix<double>& matPrj);

	// decomposition of a projection matrix into K [R T]
	virtual void Decompose(const CMatrix<double>& prjMatrix,
										   CMatrix<double>& prjK,
										   CMatrix<double>& prjRt);

	// triangulation
	virtual void Triangulate(const vector<CMatrix<double>*>& prjMats, 
							 const vector<vector<C2DPoint*>*>& src2Ds,
							 vector<C3DPoint*>& res3D);
};
