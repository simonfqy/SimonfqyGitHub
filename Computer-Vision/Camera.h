// Camera.h : main header file for the Camera DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

// CCameraApp
// See Camera.cpp for the implementation of this class
//

class CCameraApp : public CWinApp
{
public:
	CCameraApp();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
