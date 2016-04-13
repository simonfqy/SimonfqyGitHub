// 3DPointMap.cpp : implementation file
//

#include "stdafx.h"
#include "3DPointMap.h"

//////////////////////
// C3DPoint         //
//////////////////////

IMPLEMENT_SERIAL(C3DPoint, CObject, 0)

C3DPoint::C3DPoint(double x, double y, double z, int flag)
{
	this->x = x;
	this->y = y;
	this->z = z;
	this->flag = flag;
}

C3DPoint::C3DPoint(const C3DPoint& c)
{
	x = c.x;
	y = c.y;
	z = c.z;
	flag = c.flag;
}

C3DPoint::~C3DPoint()
{

}

const C3DPoint& C3DPoint::operator = (const C3DPoint &c)
{
	x = c.x;
	y = c.y;
	z= c.z;
	flag = c.flag;

	return *this;
}

void C3DPoint::Serialize(CArchive& ar)
{
	CObject::Serialize(ar);

	if (ar.IsStoring())
	{
		ar << x << y << z << flag;
	}
	else
	{
		ar >> x >> y >> z >> flag;
	}
}