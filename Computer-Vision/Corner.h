// Corner.h : main header file for the Corner DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

// CCornerApp
// See Corner.cpp for the implementation of this class
//

class CCornerApp : public CWinApp
{
public:
	CCornerApp();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
