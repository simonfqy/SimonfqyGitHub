// Camera.cpp : Defines the initialization routines for the DLL.
//

#include "stdafx.h"
#include "Camera.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// CCameraApp

BEGIN_MESSAGE_MAP(CCameraApp, CWinApp)
END_MESSAGE_MAP()


// CCameraApp construction

CCameraApp::CCameraApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}


// The one and only CCameraApp object

CCameraApp theApp;


// CCameraApp initialization

BOOL CCameraApp::InitInstance()
{
	CWinApp::InitInstance();

	return TRUE;
}