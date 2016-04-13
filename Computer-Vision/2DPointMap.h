#pragma once

//for CTypedPtrList
#include <afxtempl.h>

///////////////////////////
// Class C2DPoint        //
///////////////////////////

enum C2DPNT_STYLE
{
	P2D_NULL = 0x0,
	P2D_CANDIDATE = 0x1,
	P2D_NORMAL = 0x2,
	P2D_KNOWN = 0x4,
	P2D_MATCHED = 0x8,
	P2D_ALL = 0xF
};

class C2DPoint : public CObject
{
	DECLARE_SERIAL(C2DPoint)

public:
	// attributes
	double x, y;
	int flag; // see enum P2D_STYLE

	// useful when archival the points, served as the index
	double vdata; //voldatile data, will not be serialized

public:
	//constructors
	C2DPoint(double x=0.0, double y=0.0, int flag = P2D_NORMAL);
	C2DPoint(const C2DPoint& c);

	// destructors
	virtual ~C2DPoint();

	// operators
	const C2DPoint& operator = (const C2DPoint& c);

	// serializations
	virtual void Serialize(CArchive& ar);
};

