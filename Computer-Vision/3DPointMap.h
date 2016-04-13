
#pragma once

///////////////////////////
// Class CVG3DPoint      //
///////////////////////////

enum C3DPNT_STYLE
{
	P3D_NULL = 0x0,
	P3D_NORMAL = 0x2,
	P3D_AUTO = 0x4
};

class C3DPoint : public CObject
{
	DECLARE_SERIAL(C3DPoint)

public:
	// attributes
	double x, y, z;
	int flag; // see enum P2D_STYLE

	// useful when archival the points, served as the index
	double vdata; //voldatile data, will not be serialized

public:
	//constructors
	C3DPoint(double x=0.0, double y=0.0, double z=0.0, int flag = P3D_NORMAL);
	C3DPoint(const C3DPoint& c);

	// destructors
	virtual ~C3DPoint();

	// operators
	const C3DPoint& operator = (const C3DPoint& c);

	// serializations
	virtual void Serialize(CArchive& ar);
};
