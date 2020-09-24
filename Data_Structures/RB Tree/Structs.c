//_______________________________________LIBRARIES____________________________________________
#include <string.h>
#include <stdlib.h>
#include "RBTree.h"
#include "Structs.h"


//_______________________________________DECELERATIONS____________________________________________
//Vector Functions
static int getMinLenVectors(const Vector *v, const Vector *w);

static int isVhasMoreCoordinates(const Vector *v, const Vector *w);

double getNormVector(Vector *vec);

static int newVector(Vector **newVec);

int copyVector(Vector *dest, const Vector *source);

//_______________________________________MACROS___________________________________________________
// Return value - Stat of function
#define FUNC_FAIL (0)
#define FUNC_SUCCESS (1)

// Compare values.
#define LESS (-1)
#define EQUAL (0)
#define GREATER (1)

// Signs for readable code.
#define OR ||
#define AND &&

//__________________________________VECTOR FUNCTIONS______________________________________________

/**
 * CompFunc for Vectors, compares element by element, the vector that has the first larger
 * element is considered larger. If vectors are of different lengths and identify for the length
 * of the shorter vector, the shorter vector is considered smaller.
 * @param a - first vector
 * @param b - second vector
 * @return equal to 0 iff a == b. lower than 0 if a < b. Greater than 0 iff b < a.
 */
int vectorCompare1By1(const void *a, const void *b)
{
	Vector *v = (Vector *) a;
	Vector *w = (Vector *) b;
	int minLen = getMinLenVectors(v, w);
	// Compare each coordinate of first and second vectors - compare only the minLen coordinate.
	for (int i = 0; i < minLen; ++i)
	{
		if (((*(v->vector + i)) < ((*(w->vector + i)))))
		{
			return LESS;
		}
		else if (((*(v->vector + i)) > ((*(w->vector + i)))))
		{
			return GREATER;
		}
	}
	// All the minLen items were equal.
	return isVhasMoreCoordinates(v, w);
}

/**
 * copy pVector to pMaxVector if : 1. The norm of pVector is greater then the norm of pMaxVector.
 * 								   2. pMaxVector->vector == NULL.
 * @param pVector pointer to Vector
 * @param pMaxVector pointer to Vector
 * @return 1 on success, 0 on failure (if pVector == NULL: failure).
 */
int copyIfNormIsLarger(const void *pVector, void *pMaxVector)
{
	// Check if pVector is Null
	if (pVector == NULL)
	{
		return FUNC_FAIL;
	}
		// pMaxVector->vector is null or the norm is larger.
	else if ((((Vector *) pMaxVector)->vector == NULL) OR
			 getNormVector((Vector *) pVector) > getNormVector((Vector *) pMaxVector))
	{
		if (copyVector(pMaxVector, pVector) == FUNC_FAIL)
		{
			return FUNC_FAIL;
		}
	}
	return FUNC_SUCCESS;
}

/**
 * Function that creates new vector - malloc and set the defaults params of new node.
 * @param newVec
 * @return
 */
static int newVector(Vector **const newVec)
{
	*newVec = (Vector *) malloc(sizeof(Vector));
	if (*newVec == NULL)
	{
		return FUNC_FAIL;
	}
	(*newVec)->len = 0;
	(*newVec)->vector = NULL;
	return FUNC_SUCCESS;
}

/**
 * @param tree a pointer to a tree of Vectors
 * @return pointer to a *copy* of the vector that has the largest norm (L2 Norm).
 */
Vector *findMaxNormVectorInTree(RBTree *tree)
{
	if (tree == NULL OR tree->root == NULL)
	{
		return NULL;
	}

	Vector *pMaxVector = NULL;
	if (newVector(&pMaxVector) == FUNC_FAIL)
	{
		return NULL;
	}

	forEachRBTree(tree, copyIfNormIsLarger, pMaxVector);
	return pMaxVector;
}

/**
 * Fucntion that returns the min len of two vectors.
 * @param v
 * @param w
 * @return : min len of 2 vectors
 */
static int getMinLenVectors(const Vector *v, const Vector *w)
{
	int minLen = (v->len < w->len) ? v->len : w->len;
	return minLen;
}

/**
 * Function that checks if first Vector has more coordinate
 * @param v : first vector
 * @param w : second vector
 * @return LESS , GREATER or EQUAL on the query if v has more coordinate than w.
 */
static int isVhasMoreCoordinates(const Vector *v, const Vector *w)
{
	if (v->len < w->len)
	{
		return LESS;
	}
	else if (v->len > w->len)
	{
		return GREATER;
	}
	else
	{
		return EQUAL;
	}
}

/**
 * Function that gets an vector and returns the norm of the vector
 * @param vec
 * @return
 */
double getNormVector(Vector *vec)
{
	double norm = 0;
	for (int i = 0; i < vec->len; ++i)
	{
		norm += (vec->vector[i] * vec->vector[i]);
	}
	return norm;
}

/**
 *Copy vector array from soutce to dest - using realloc
 * @param dest Vector
 * @param source vector
 * @return FUNC_FAIL/FANC_SUCCESS if the malloc succeeded.
 */
int copyVector(Vector *dest, const Vector *source)
{
	// Realloc the dest->vector.
	dest->vector = (double *) realloc(dest->vector, (source->len) * sizeof(double));
	// Check if realloc succeeded!
	if (dest->vector == NULL)
	{
		return FUNC_FAIL;
	}
	// Copy source to dest.
	dest->len = source->len;
	memcpy(dest->vector, source->vector, (source->len) * sizeof(double));
	return FUNC_SUCCESS;
}

/**
 * FreeFunc for vectors
 */
void freeVector(void *pVector)
{
	if (pVector != NULL)
	{
		Vector *freeVec = (Vector *) pVector;
		if (freeVec->vector != NULL)
		{
			free(freeVec->vector);
		}
		free(freeVec);
	}
}


//__________________________________STRING FUNCTIONS______________________________________________

/**
 * CompFunc for strings (assumes strings end with "\0")
 * @param a - char* pointer
 * @param b - char* pointer
 * @return equal to 0 iff a == b. lower than 0 if a < b. Greater than 0 iff b < a. (lexicographic
 * order)
 */
int stringCompare(const void *a, const void *b)
{
	char *first = (char *) a;
	char *second = (char *) b;
	int diff = (int) strcmp(first, second);
	if (diff < 0)
	{
		return LESS;
	}
	else if (diff > 0)
	{
		return GREATER;
	}
	else
	{
		return EQUAL;
	}
}

/**
 * ForEach function that concatenates the given word and \n to pConcatenated. pConcatenated is
 * already allocated with enough space.
 * @param word - char* to add to pConcatenated
 * @param pConcatenated - char*
 * @return 0 on failure, other on success
 */
int concatenate(const void *word, void *pConcatenated)
{
	strcat(pConcatenated, word);
	strcat(pConcatenated, "\n");
	return FUNC_SUCCESS;
}

/**
 * FreeFunc for strings
 */
void freeString(void *s)
{
	if (s != NULL)
	{
		free(s);
	}
}

