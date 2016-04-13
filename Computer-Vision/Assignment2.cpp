#include "stdAfx.h"
#include "Assignment2.h"

/////////////////////////////
// CCorner Source File //
/////////////////////////////


// this function convert a given CImage to a GrayScale image
void CCorner::RGBToGrayScale(CImage* pIn, CImage* pOut)
{
	//
	// INPUT:
	//     CImage* pIn:		The input image with 24bit depth
	//
	// OUTPUT:
	//     CImage* pOut:	The output image. It has ALREADY been initialized
	//                      with the same dimension as the input image (pIN) and 
	//                      formatted to 8bit depth (256 gray levels). So, please
	//                      use 'SetIndex' instead of 'SetRGB'.
	//
	
	// Begin your code here: //
	// It has been a big challenge for me to do this assignment. I will feel great sense of achievement when I finish.
	// Move on!
	int width = (*pIn).GetWidth();
	int height = (*pIn).GetHeight();
	byte *r = new byte;
	byte *g = new byte;
	byte *b = new byte;
	//byte ind;
	for (int x = 0; x <= width - 1; x++){
		for(int y = 0; y <= height - 1; y++){
			(*pIn).GetRGB(x, y, r, g, b);
			//ind = (*r)*0.299 + (*g)*0.587 + (*b)*0.114;
			(*pOut).SetIndex(x, y, (*r)*0.299 + (*g)*0.587 + (*b)*0.114);
		}
	}	

}

// this function obtains the corners from a given GrayScale image
void CCorner::ObtainCorners(CImage* pIn, double sigma, double threshold, vector<C2DPoint*>* pResultCorners)
{
//
	// INPUT:
	//     CImage* pIn:		The input grayscale image, which is exactly the output of
	//                      RGBToGrayScale function.
	//     double sigma:    The sigma value for your Gaussian filter.
	//     double threshold: The minimum value for qualifying a corner. Please refer to the lecture notes
	//
	// OUTPUT:
	//     vector<C2DPoint*>* pResultCorners:	
	//                      A std::vector object that holds all detected corners. Each corner is represented by
	//                      a C2DPoint structure. An example is given below, showing how a corner object is
	//                      initialized and stored in pResultCorners:
	//                      
	//                      	C2DPoint* pPnt = new C2DPoint(x, y);
	//                      	pResultCorners.push_back(pPnt);
	//
	//
	
	// Begin your code here: //

	////
	// Step 1: Compute a proper size for Gaussian filter
	int n;
	n = floor(sigma*sqrt(2*log(1000.0)));
	int w = 2*n+1;

	////
	// Step 2: Define the Gaussian filter and partial filter
	double *gaussFilt = new double[w];
	double sum = 0;
	int x,i,j,p;
	for(i = 0; i < w; i++){
		x = i - n;
		gaussFilt[i] = exp(-(x*x)/(2*sigma*sigma));
		sum = sum + gaussFilt[i];
	}
    for (i = 0; i < w; i++){
		gaussFilt[i] = gaussFilt[i]/sum;
	}
	//partFilt1 is aligned from left to right at left end, while partFilt2 is at the right end.
	double **partFilt1 = new double*[n];
	double **partFilt2 = new double*[n];
	for (i = 0; i < n; i++){
		partFilt1[i] = new double[n + i + 1];
		partFilt2[i] = new double[w - 1 - i];
	}

	//Fill the two partial filters
	for (i = 0; i < n; i++){
		sum = 0;
		for (j = 0; j < n + i + 1; j++){
			x = j - i;
			partFilt1[i][j] = exp(-(x*x)/(2*sigma*sigma));
			sum = sum + partFilt1[i][j];
		}
		for (j = 0; j < n + i + 1; j++){
			partFilt1[i][j] = partFilt1[i][j]/sum;
		}
	}

	//Now fill the "mirror": partFilt2
	for (i = 0; i < n; i++){
		int mirrorI = n - 1 - i;
		int length = 2*n - i;
		for (j = 0; j < w - i - 1; j++){
			int mirrorJ = length - j - 1;
			partFilt2[i][j] = partFilt1[mirrorI][mirrorJ];
		}
	}

	////
	// Step 3: Compute Ix, Iy
	int width = (*pIn).GetWidth();
	int height = (*pIn).GetHeight();
	double **Ix = new double*[width];
	double **Iy = new double*[width];
	for (i = 0; i < width; i++){
		Ix[i] = new double[height];
		Iy[i] = new double[height];
	}
	for (i = 0; i < width; i++){
		for (j = 0; j < height; j++){
			if (i==0)
				Ix[i][j] = (*pIn).GetIndex(i+1,j) - (*pIn).GetIndex(i,j);
			else if (i==width - 1)
				Ix[i][j] = (*pIn).GetIndex(i, j) - (*pIn).GetIndex(i-1, j);
			else{
				Ix[i][j] = 0.5*((*pIn).GetIndex(i+1, j) - (*pIn).GetIndex(i-1, j));
			}
			
			if (j==0)
				Iy[i][j] = (*pIn).GetIndex(i,j+1) - (*pIn).GetIndex(i,j);
			else if (j==height - 1)
				Iy[i][j] = (*pIn).GetIndex(i, j) - (*pIn).GetIndex(i, j - 1);
			else{
				Iy[i][j] = 0.5*((*pIn).GetIndex(i, j+1) - (*pIn).GetIndex(i, j-1));
			}
		}
	}

	////
	// Step 4: Compute Ix^2, Iy^2, IxIy
	double **Ix2 = new double*[width];
	double **Iy2 = new double*[width];
	double **Ixy = new double*[width];
	double **SIx2 = new double*[width];
	double **SIy2 = new double*[width];
	double **SIxy = new double*[width];
	for (i = 0; i < width; i++){
		Ix2[i] = new double[height];
		Iy2[i] = new double[height];
		Ixy[i] = new double[height];
		SIx2[i] = new double[height];
		SIy2[i] = new double[height];
		SIxy[i] = new double[height];
		for (j = 0; j < height; j++){
			Ix2[i][j] = Ix[i][j]*Ix[i][j];
			Iy2[i][j] = Iy[i][j]*Iy[i][j];
			Ixy[i][j] = Ix[i][j]*Iy[i][j];
		}
	}

	////
	// Step 5: Smooth Ix^2, Iy^2, IxIy
	double result1, result2, result3;
	int k, ind;
	for (i = 0; i < width; i++){
		for (j = 0; j < height; j++){
			result1 = 0;
			result2 = 0;
			result3 = 0;
			if (i > n-1 && i < width - n){
				for (k = 0; k < w; k++){
					result1 = result1 + gaussFilt[k]*Ix2[i - n + k][j];
					result2 = result2 + gaussFilt[k]*Iy2[i - n + k][j];
					result3 = result3 + gaussFilt[k]*Ixy[i - n + k][j];
				}
			}
			else if (i <= n - 1){				
				for (k = 0; k < n + i + 1; k++){
					result1 = result1 + partFilt1[i][k]*Ix2[k][j];
					result2 = result2 + partFilt1[i][k]*Iy2[k][j];
					result3 = result3 + partFilt1[i][k]*Ixy[k][j];
				}
			}
			else if ( i >= width - n){
				ind = i - (width - n);
				for (k = 0; k < w - 1 - ind; k++){
					result1 = result1 + partFilt2[ind][k]*Ix2[i - n + k][j];
					result2 = result2 + partFilt2[ind][k]*Iy2[i - n + k][j];
					result3 = result3 + partFilt2[ind][k]*Ixy[i - n + k][j];
				}
			}
			SIx2[i][j] = result1;
			SIy2[i][j] = result2;
			SIxy[i][j] = result3;
		}		
	}

	//Implement the y-convolution.
	for (i = 0; i < width; i++){
		for (j = 0; j < height; j++){
			result1 = 0;
			result2 = 0;
			result3 = 0;
			if (j > n-1 && j < height - n){
				for (k = 0; k < w; k++){
					result1 = result1 + gaussFilt[k]*SIx2[i][j - n + k];
					result2 = result2 + gaussFilt[k]*SIy2[i][j - n + k];
					result3 = result3 + gaussFilt[k]*SIxy[i][j - n + k];
				}
			}
			else if (j <= n - 1){
				for (k = 0; k < n + j + 1; k++){
					result1 = result1 + partFilt1[j][k]*SIx2[i][k];
					result2 = result2 + partFilt1[j][k]*SIy2[i][k];
					result3 = result3 + partFilt1[j][k]*SIxy[i][k];
				}
			}
			else if (j >= height - n){
				ind = j - (height - n);
				for (k = 0; k < w - 1 - ind; k++){
					result1 = result1 + partFilt2[ind][k]*SIx2[i][j - n + k];
					result2 = result2 + partFilt2[ind][k]*SIy2[i][j - n + k];
					result3 = result3 + partFilt2[ind][k]*SIxy[i][j - n + k];
				}
			}
			Ix2[i][j] = result1;
			Iy2[i][j] = result2;
			Ixy[i][j] = result3;
		}		
	}

	////
	// Step 6: Compute R
	for (i = 0; i < width; i++){
		for (j = 0; j < height; j++){
			//Now let SIx2 store the R values.
			SIx2[i][j] = Ix2[i][j] * Iy2[i][j] - pow(Ixy[i][j], 2) - 0.04 *pow( (Ix2[i][j] + Iy2[i][j]), 2);
			SIy2[i][j] = 0;
		}
	}

	////
	// Step 7: Locate maxima in R
	bool maximum;
	for (i = 1; i < width - 1; i++){
		for (j = 1; j < height - 1; j++){
			maximum = true;
			for (k = -1; k < 2; k++){
				for (p = -1; p < 2; p++){
					//if ((i + k >=0 && i +k < width)&&( j + p >= 0 && j + p < width)){
						if (SIx2[i][j] < SIx2[i+k][j+p]){
							maximum = false;
							break;
						}
					//}
				}
				if (!maximum)
					break;
			}
			if (maximum)
				SIy2[i][j] = 1;							
		}
	}
	//At the end SIy2 stores the values of local maxima at corresponding locations, others are 0.

	////
	// Step 8: Compute corner candidates up to sub-pixel accuracy and interpolate R value for corner candidates
	double a, b, c;
	//positions and values of corner candidates, created by x and y interpolating respectively.
	double fx, fy, ix, iy;
	//Storing the position and value of corner candidates. Expected to be double values.
	vector<double> cornerX;
	vector<double> cornerY;
	vector<double> cornerVal;
	for (i = 1; i < width - 1; i++){
		for (j = 1; j < height - 1; j++){
			if (SIy2[i][j] == 0)
				continue;
			//First do it horizontally.
			a = (SIx2[i+1][j] + SIx2[i-1][j] - 2*SIx2[i][j])/2;
			b = (SIx2[i+1][j] - SIx2[i-1][j])/2;
			c = SIx2[i][j];
			ix = -1*(b/(2*a));
			fx = a*pow(ix, 2) + b*ix + c;
			a = (SIx2[i][j+1] + SIx2[i][j-1] - 2*SIx2[i][j])/2;
			b = (SIx2[i][j+1] - SIx2[i][j-1])/2;
			iy = -1*(b/(2*a));
			fy = a*pow(iy, 2) + b*iy + c;
			if (fx > fy){
				cornerX.push_back(ix + i);
				cornerY.push_back(j);
				cornerVal.push_back(fx);
			}
			else{
				cornerY.push_back(iy + j);
				cornerX.push_back(i);
				cornerVal.push_back(fy);
			}
		}
	}

	////
	// Step 9: Use the threshold value to identify strong corners for output
	vector<double>::iterator itr1, itr2, itr3;
	itr1 = cornerX.begin();
	itr2 = cornerY.begin();
	for (itr3 = cornerVal.begin(); itr3 != cornerVal.end(); itr3++){
		if (*itr2 >= threshold){
			C2DPoint* pnt = new C2DPoint(*itr1, (height - *itr2 - 1));
			(*pResultCorners).push_back(pnt);
		}
		itr1++;
		itr2++;
	}

	delete []gaussFilt;
	for (i = 0; i < n; i++){
		delete []partFilt1[i];
		delete []partFilt2[i];
	}
	delete []partFilt1;
	delete []partFilt2;
	for (i = 0; i < width; i++){
		delete []Ix[i];
		delete []Iy[i];
		delete []Ix2[i];
		delete []Iy2[i];
		delete []Ixy[i];
		delete []SIx2[i];
		delete []SIy2[i];
		delete []SIxy[i];
	}
	delete []Ix;
	delete []Iy;
	delete []Ix2;
	delete []Iy2;
	delete []Ixy;
	delete []SIx2;
	delete []SIy2;
	delete []SIxy;
}


