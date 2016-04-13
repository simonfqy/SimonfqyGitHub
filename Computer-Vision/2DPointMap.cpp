// 2DPointMap.cpp : implementation file
//

#include "stdafx.h"
#include "2DPointMap.h"

//////////////////////
// C2DPoint         //
//////////////////////

IMPLEMENT_SERIAL(C2DPoint, CObject, 0)

C2DPoint::C2DPoint(double x, double y, int flag)
{
	this->x = x;
	this->y = y;
	this->flag = flag;
}

C2DPoint::C2DPoint(const C2DPoint& c)
{
	x = c.x;
	y = c.y;
	flag = c.flag;
}

C2DPoint::~C2DPoint()
{

}

const C2DPoint& C2DPoint::operator = (const C2DPoint &c)
{
	x = c.x;
	y = c.y;
	flag = c.flag;

	return *this;
}

void C2DPoint::Serialize(CArchive& ar)
{
	CObject::Serialize(ar);

	if (ar.IsStoring())
	{
		ar << x << y << flag;
	}
	else
	{
		ar >> x >> y >> flag;
	}
}