#pragma once

// header inclusion
#include "math.h"
#include "cimage.h"
#include <vector>
using namespace std;

#include "2DPointMap.h"
#include "3DPointMap.h"

// some constants
#define CALIBRATION_FUZZINESS 16.0
#define ALIGN_FUZZINESS	64.0

///////////////////////////////////
// CCorner class's declaration
///////////////////////////////////

///////////////////////////////////
// IMPORTANT!
//
// Don't modify the declaration of
// CCorner!
//
///////////////////////////////////
class __declspec(dllexport) CCorner
{
public:

	// convert a colored CImage to a grayscale one (CMatrix)
	virtual void RGBToGrayScale(CImage* pIn, CImage* pOut);

	// corner detection
	virtual void ObtainCorners(CImage* pIn, double sigma, double threshold, vector<C2DPoint*>* pResultCorners);
};
