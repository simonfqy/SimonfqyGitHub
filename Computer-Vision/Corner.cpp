// Corner.cpp : Defines the initialization routines for the DLL.
//

#include "stdafx.h"
#include "Corner.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// CCornerApp

BEGIN_MESSAGE_MAP(CCornerApp, CWinApp)
END_MESSAGE_MAP()


// CCornerApp construction

CCornerApp::CCornerApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}


// The one and only CCornerApp object

CCornerApp theApp;


// CCornerApp initialization

BOOL CCornerApp::InitInstance()
{
	CWinApp::InitInstance();

	return TRUE;
}