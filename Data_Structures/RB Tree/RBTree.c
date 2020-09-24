//_______________________________________LIBRARIES____________________________________________

#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include "RBTree.h"

//_______________________________________DECELERATIONS____________________________________________



// 					____________________ Insert Functions ___________________________

static void fixUpInsert(Node **node, RBTree *tree);

static void fixUpIns4LR(Node **node, Node **grand, Node **par, RBTree *tree);

static void fixUpIns4RL(Node **node, Node **grand, Node **par, RBTree *tree);

static void fixUpIns4(Node **node, Node **grand, Node **par, RBTree *tree);

static void fixUpIns3(Node **grand, Node **par, Node **uncle);

// 			_____________________________ Delete Functions ___________________________

static int deleteNodeFromTree(RBTree *tree, Node **deletedNode);

static int deleteTwoChildrenCase(RBTree *tree, Node **deletedNode);

static int deleteOneChildCase(RBTree *tree, Node **deletedNode);

static int deleteZeroChildrenCase(RBTree *tree, Node **deletedNode);

// 			_____________________ Balance after Delete Functions ___________________________

static int getCaseOfFixUpCase3(RBTree *tree, Node **nodeC, Node **nodeP, Node **nodeS);

static void updateDBPointers(Node **nodeC, Node **nodeP, Node **nodeS);

static void dbCaseSAndFarAreBlack(Node **nodeP, Node **nodeS, RBTree *tree);

static void dbCaseSAndCloseAreBlack(Node **nodeP, Node **nodeS, RBTree *tree);

static void doubleBlackCases
		(int caseNum, RBTree *tree, Node **nodeC, Node **nodeP, Node **nodeS);

static void deleteFixUp(RBTree *tree, Node **nodeM, int sideNodeC, bool skipOneAndTwoCases);

static int deleteOneLeftChildCase(RBTree *tree, Node **deletedNode);

static int deleteOneRightChildCase(RBTree *tree, Node **deletedNode);

static void dbCasePBlack(RBTree *tree, Node **nodeC, Node **nodeP, Node **nodeS);

static void dbCaseSRed(RBTree *tree, Node **nodeC, Node **nodeP, Node **nodeS);

static int getCaseOfFixUp
		(RBTree *tree, Node **nodeM, Node **nodeC, Node **nodeP, Node **nodeS,
		 bool skipOneAndTwoCases);

// _____________________________ Tree Functions ___________________________
static void successor(Node **node);

static void findMin(Node **cur);

static int find(Node **cur, const void *data, CompareFunc compare);

static int setRoot(RBTree *tree, void *data);

static Node *setNewLeaf(Node *parent, int childSide, void *data);

static void leftRotate(Node **grand, Node **par, RBTree *tree);

static void rightRotate(Node **grand, Node **par, RBTree *tree);

// _____________________________ Tools ___________________________

static void swapData(Node **first, Node **second);

static int numChildren(Node *node);

static void helperFreeRBTree(Node **node, FreeFunc freeData);

static int isNodeIsRightChild(const Node *node);

static int isNodeIsLeftChild(const Node *node);

static int isBlackColor(const Node *node);

static int isRedColor(const Node *node);

static void setUncle(Node **uncle, const Node *grand, const Node *par);

static int isNodeIsRoot(const Node *node, const RBTree *t);

static void setNodeAsCloseChild(Node **dest, const Node *nodeS, const Node *nodeP);

static void setNodeAsFarChild(Node **dest, const Node *nodeS, const Node *nodeP);


static void swapColors(Node **a, Node **b);


// _____________________________ Memory Management ___________________________

static void freeNode(Node **freedNode, FreeFunc freeData);

static Node *allocateNode(void *data);






//_______________________________________MACROS____________________________________________

// Functions return Macros
#define FUNC_FAIL (0)
#define FUNC_SUCCESS (1)

// Signs for readable code
#define OR ||
#define AND &&


// Compare Macros
#define LESS (-1)
#define EQUAL (0)
#define GREATER (1)

//Child Macros
#define LEFT (-1)
#define DATA_FOUND (0)
#define RIGHT (1)

#define ZERO_CHILDREN (0)
#define ONE_CHILD (1)
#define TWO_CHILDREN (2)

// Cases in fix up tree after delete
#define M_RED (-1)
#define M_BLACK_C_RED (0)
#define C_IS_ROOT (2)
#define P_RED (4)
#define P_BLACK (5)
#define S_RED (6)
#define S_RED (6)
#define S_AND_FAR_BLACK (7)
#define S_AND_FAR_RED (8)

//General Macros
#define DO_NOTHING -10


//__________________________________RB TREE FUNCTIONS_____________________________________________


/**
 * constructs a new RBTree with the given CompareFunc.
 * comp: a function two compare two variables.
 */
RBTree *newRBTree(CompareFunc compFunc, FreeFunc freeFunc)
{
	RBTree *newTree = (RBTree *) malloc(sizeof(RBTree));
	// In case that the malloc failed:
	if (newTree == NULL)
	{
		return NULL;
	}
	// Set Default attributes for RB tree.
	newTree->root = NULL;
	newTree->compFunc = compFunc;
	newTree->freeFunc = freeFunc;
	newTree->size = 0;
	return newTree;
}

/**
 * Activate a function on each item of the tree. the order is an ascending order. if one of the
 * activations of the function returns 0, the process stops.
 * @param tree: the tree with all the items.
 * @param func: the function to activate on all items.
 * @param args: more optional arguments to the function (may be null if the given function support).
 * @return: 0 on failure, other on success.
 */
int forEachRBTree(const RBTree *tree, forEachFunc func, void *args)
{
	if (tree == NULL)
	{
		return FUNC_FAIL;
	}
	Node *cur = tree->root;
	findMin(&cur);
	while (cur != NULL)
	{
		// Check if the activation fail:
		if (func(cur->data, args) == FUNC_FAIL)
		{
			return FUNC_FAIL;
		}
		successor(&cur);
	}
	return FUNC_SUCCESS;
}

/**
 * check whether the tree RBTreeContains this item.
 * @param tree: the tree to add an item to.
 * @param data: item to check.
 * @return: 0 if the item is not in the tree, other if it is.
 */
int RBTreeContains(const RBTree *tree, const void *data)
{
	if (tree == NULL || tree->root == NULL || data == NULL)
	{
		return FUNC_FAIL;
	}
	Node *cur = tree->root;
	if (find(&cur, data, tree->compFunc) == DATA_FOUND)
	{
		return FUNC_SUCCESS;
	}
	// Return FUNC_FAIL = (0) if the item is not in the tree.
	return FUNC_FAIL;
}
//_______________________________________INSERT____________________________________________________

/**
 * add an item to the tree - add to specific place and than balance the tree
 * @param tree: the tree to add an item to.
 * @param data: item to add to the tree.
 * @return: 0 on failure, other on success. (if the item is already in the tree - failure).
 */
int insertToRBTree(RBTree *tree, void *data)
{
	if (tree == NULL || data == NULL)
	{
		return FUNC_FAIL;
	}
	// If the tree is empty:
	if (tree->root == NULL)
	{
		if (setRoot(tree, data) == FUNC_FAIL)
		{
			return FUNC_FAIL;
		}
	}
	else // The tree is not empty:
	{
		// Step 1: Find the place to put new leaf by find function.
		Node *cur = tree->root;
		//Data found: 0,  Right: 1,  Left: -1
		int childSide = find(&cur, data, tree->compFunc);
		if (childSide == DATA_FOUND) // If the data already exists in the tree)
		{
			return FUNC_FAIL;
		}
		// Step 2: Set the new Leaf
		Node *leaf = setNewLeaf(cur, childSide, data);
		if (leaf == NULL)
		{
			return FUNC_FAIL;
		}
		// Step 3: Fix up the Balance of the tree:
		fixUpInsert(&leaf, tree);
	}

	tree->size += 1;  //Increase the size of the tree.
	return FUNC_SUCCESS;
}


/**
 * After insert Fix up the balance of the tree.
 * There is  4 optional cases.- depeand on the colors of situation of the parent of new node.
 * @param node
 */
static void fixUpInsert(Node **const node, RBTree *const tree)
{
	if ((*node)->parent == NULL)
	{
		(*node)->color = BLACK;
		return;
	}
	// Case 2 (case 1 is insert root).
	if (isBlackColor((*node)->parent))
	{
		return;
	}
	Node *par = (*node)->parent;
	Node *grand = (*node)->parent->parent;
	Node *uncle = NULL;
	setUncle(&uncle, grand, par);
	// Case 4
	if ((isRedColor(par)) AND (isBlackColor(uncle)))
	{
		fixUpIns4(node, &grand, &par, tree);
	}
		// Case 3
	else if (isRedColor(par) AND uncle->color == RED)
	{
		fixUpIns3(&grand, &par, &uncle);
		fixUpInsert(&grand, tree);
	}
}

/**
 * Case num 3 - Change colors
 * @param grand
 * @param par
 * @param uncle
 */
static void fixUpIns3(Node **const grand, Node **const par, Node **const uncle)
{
	// Change color of U and P to black.
	(*par)->color = BLACK;
	(*uncle)->color = BLACK;
	// Change color of grand to red.
	(*grand)->color = RED;
}


/**
 * There is 4 optional subcases.
 * @param node
 * @param grand
 * @param par
 * @param uncle
 * @param tree
 */
static void fixUpIns4(Node **const node, Node **const grand, Node **const par, RBTree *const tree)
{
	// Check if node is right child of left child.
	if ((*node == (*par)->right) AND (*par == (*grand)->left))
	{
		fixUpIns4RL(node, grand, par, tree);
	}
		// Check if node is left child of rihgt child.
	else if (*node == (*par)->left AND *par == (*grand)->right)
	{
		fixUpIns4LR(node, grand, par, tree);
	}
		// if The node is left child of left child
	else if (*node == (*par)->left AND *par == (*grand)->left)
	{
		rightRotate(grand, par, tree);
		(*par)->color = BLACK, (*grand)->color = RED;
	}
		// if The node is right child of right child
	else if ((*node == (*par)->right) AND (*par == (*grand)->right))
	{
		leftRotate(grand, par, tree);
		(*par)->color = BLACK, (*grand)->color = RED;
	}


}

/**
 *  * Fix up the balance tree: if node is left child of par and par is right child of grand.
 * Case Left Right
 * @param node
 * @param grand
 * @param par
 * @param tree
 */
static void fixUpIns4RL(Node **const node, Node **const grand, Node **const par, RBTree *const tree)
{
	// Step 1: Rotation
	(*par)->parent = (*node);
	// New
	(*par)->right = (*node)->left;
	if ((*node)->left)
	{
		(*node)->left->parent = (*par);
	}
	// End
	(*node)->left = *par;
	(*grand)->left = *node;
//	(*par)->right = NULL;
	(*node)->parent = *grand;
	// Step 2: Rotate Right
	rightRotate(grand, node, tree);
	// Step 3:
	(*node)->color = BLACK, (*grand)->color = RED;
}

/**
 * Fix up the balance tree: if node is right child of par and par is left child of grand.
 * Case Right Left
 * @param node
 * @param grand
 * @param par
 * @param tree
 */
static void fixUpIns4LR(Node **const node, Node **const grand, Node **const par, RBTree *const tree)
{
	(*par)->parent = (*node);
	// New
	(*par)->left = (*node)->right;
	if ((*node)->right)
	{
		(*node)->right->parent = (*par);
	}
	// End
	(*node)->right = *par;
	(*grand)->right = *node;
//	(*par)->left = NULL;
	(*node)->parent = *grand;
	leftRotate(grand, node, tree);
	(*node)->color = BLACK, (*grand)->color = RED;
}

//_______________________________________DELETE____________________________________________________

/**
 * remove an item from the tree
 * @param tree: the tree to remove an item from.
 * @param data: item to remove from the tree.
 * @return: 0 on failure, other on success. (if data is not in the tree - failure).
 */
int deleteFromRBTree(RBTree *tree, void *data)
{
	if (tree == NULL OR tree->root == NULL OR data == NULL)
	{
		return FUNC_FAIL;
	}
	Node *deletedNode = tree->root;
	if (find(&deletedNode, data, tree->compFunc) != DATA_FOUND)
	{
		return FUNC_FAIL;
	}
	// Step 1 - Delete Node
	int sideNodeC = deleteNodeFromTree(tree, &deletedNode);

	// Step 2 - Save pointer to M node
	Node *freedNode = deletedNode;
	// Step 3 - Fix up the tree - Only if the updated deleteNode is not the root
	if (sideNodeC != C_IS_ROOT)
	{
		deleteFixUp(tree, &deletedNode, sideNodeC, false);
	}
	// Step 4 - Free node and his data.
	// Just for tests!!!!
	freeNode(&freedNode, tree->freeFunc);
	// Step 5 - Update size of tree.
	tree->size -= 1;
	return FUNC_SUCCESS;
}


/**
 * Delete one node from the tree
 * @param tree
 * @param deletedNode
 */
int deleteNodeFromTree(RBTree *const tree, Node **const deletedNode)
{
	switch (numChildren(*deletedNode))
	{
		case ZERO_CHILDREN:
			return deleteZeroChildrenCase(tree, deletedNode);
		case ONE_CHILD:
			return deleteOneChildCase(tree, deletedNode);
		case TWO_CHILDREN:
			return deleteTwoChildrenCase(tree, deletedNode);
	}
	//TODO DO_NOTHING - handle it
	return DO_NOTHING;
}


/**
 * Delte node in the tree- In case that deleted node has zero children.
 * @param tree
 * @param deletedNode
 * @return
 */
static int deleteZeroChildrenCase(RBTree *const tree, Node **const deletedNode)
{
	// If the deleted node is the root.
	if ((*deletedNode) == tree->root)
	{
		tree->root = NULL;
		return C_IS_ROOT;
	}
	else
	{
		if (isNodeIsLeftChild(*deletedNode)) // If node is left child.
		{
			(*deletedNode)->parent->left = NULL;
			return LEFT;
		}
		else  // If node is right child;
		{
			(*deletedNode)->parent->right = NULL;
			return RIGHT;
		}
	}
}

/**
 * Return The side of the one child.
 * @param tree
 * @param deletedNode
 * @return
 */
static int deleteOneChildCase(RBTree *const tree, Node **const deletedNode)
{
	if ((*deletedNode)->left)
	{
		return deleteOneLeftChildCase(tree, deletedNode);
	}
	else
	{
		return deleteOneRightChildCase(tree, deletedNode);
	}
}

/**
 *
 * @param tree
 * @param deletedNode
 * @return
 */
static int deleteTwoChildrenCase(RBTree *const tree, Node **const deletedNode)
{
	Node *deletedSuccessor = *deletedNode;
	successor(&deletedSuccessor);
	swapData(deletedNode, &deletedSuccessor);
	// Change the deleted node to the successor.
	(*deletedNode) = deletedSuccessor;
	// Do one more time deleteNodeFromTree - only case ZERO_CHILDREN or ONE_CHILD are optional.
	return deleteNodeFromTree(tree, &deletedSuccessor);
}


/**
 * * Delete node when it is  got only one child and his child is LEFT
 * @param tree
 * @param deletedNode
 * @return
 */
static int deleteOneLeftChildCase(RBTree *const tree, Node **const deletedNode)
{
	if (isNodeIsRoot(*deletedNode, tree))  // If the deletedNode is the root of the tree
	{
		tree->root = (*deletedNode)->left;
		(*deletedNode)->left->parent = NULL;
		return LEFT;
	}
	else
	{
		if (isNodeIsLeftChild(*deletedNode))    // Parent is left child
		{
			(*deletedNode)->parent->left = (*deletedNode)->left;
			(*deletedNode)->left->parent = (*deletedNode)->parent;
			return LEFT;
		}
		else    // If the parent is right child of the grandfather:
		{
			(*deletedNode)->parent->right = (*deletedNode)->left;
			(*deletedNode)->left->parent = (*deletedNode)->parent;
			return RIGHT;
		}
	}
}

/**
 * Delete node when the node has only one child and his child is RIGHT
 * @param tree
 * @param deletedNode
 * @return
 */
static int deleteOneRightChildCase(RBTree *const tree, Node **const deletedNode)
{
	if (isNodeIsRoot(*deletedNode, tree))  // If the deletedNode is the root of the tree
	{
		tree->root = (*deletedNode)->right;
		(*deletedNode)->right->parent = NULL;
		return RIGHT;
	}
	else
	{
		if (isNodeIsLeftChild(*deletedNode))
		{
			(*deletedNode)->parent->left = (*deletedNode)->right;
			(*deletedNode)->right->parent = (*deletedNode)->parent;
			return LEFT;
		}
		else
		{
			(*deletedNode)->parent->right = (*deletedNode)->right;
			(*deletedNode)->right->parent = (*deletedNode)->parent;
			return RIGHT;
		}
	}
}

//____________________________________DELETE- FIX UP_______________________________________________

/**
 * After delete node the function balance the tree that it will be still a RB Tree.
 * @param tree
 * @param nodeM : The deleted node.
 * @param nodeC The Child of deleted Node.
 */
static void deleteFixUp
		(RBTree *const tree, Node **const nodeM, const int sideNodeC, const bool skipOneAndTwoCases)
{
	Node *nodeC = ((*nodeM)->right) ? (*nodeM)->right : (*nodeM)->left;
	Node *nodeP = (*nodeM)->parent;
	Node *nodeS = NULL;
	// Set nodeS
	if (nodeP)
	{
		nodeS = (sideNodeC == LEFT) ? nodeP->right : nodeP->left;
	}

	int caseNum = getCaseOfFixUp(tree, nodeM, &nodeC, &nodeP, &nodeS, skipOneAndTwoCases);
	switch (caseNum)
	{
		case M_RED:
			break;
		case M_BLACK_C_RED:
			nodeC->color = BLACK;
			break;
		default:
//			nodeC = *nodeM;
			doubleBlackCases(caseNum, tree, &nodeC, &nodeP, &nodeS);
			break;
	}
}


/**
 * Menu of double black cases
 * @param caseNum : the num of the case.
 * @param tree :
 * @param nodeC : the db pointer
 * @param nodeP : parent of the db pointer
 * @param nodeS : the brother of db pointer
 */
static void doubleBlackCases
		(const int caseNum, RBTree *const tree, Node **const nodeC, Node **const nodeP,
		 Node **const nodeS)
{
	switch (caseNum)
	{
		case C_IS_ROOT:
			break;

		case P_RED:
			(*nodeP)->color = BLACK;
			(*nodeS)->color = RED;
			break;

		case P_BLACK:
			dbCasePBlack(tree, nodeC, nodeP, nodeS);
			break;

		case S_RED:
			dbCaseSRed(tree, nodeC, nodeP, nodeS);
			break;

		case S_AND_FAR_BLACK:
			dbCaseSAndFarAreBlack(nodeP, nodeS, tree);
			break;

		case S_AND_FAR_RED:
			dbCaseSAndCloseAreBlack(nodeP, nodeS, tree);
			break;
		default:
			return;
	}
}

/**
 *  Double Black Case: S is Red
 * @param caseNum
 * @param tree
 * @param nodeC
 * @param nodeP
 * @param nodeS
 */
static void dbCaseSRed
		(RBTree *const tree, Node **const nodeC, Node **const nodeP, Node **const nodeS)
{
	(*nodeS)->color = BLACK;
	(*nodeP)->color = RED;
	if ((*nodeP)->right == *nodeS)
	{
		leftRotate(nodeP, nodeS, tree);
	}
	else
	{
		rightRotate(nodeP, nodeS, tree);
	}
//	updateDBPointers(nodeC, nodeP, nodeS);
	if (numChildren(*nodeP) == 2)
	{
		*nodeS = ((*nodeP)->right == *nodeC) ? (*nodeP)->left : (*nodeP)->right;
	}
	else
	{
		*nodeS = ((*nodeP)->right) ? (*nodeP)->right : (*nodeP)->left;
	}

	int caseNum = getCaseOfFixUpCase3(tree, nodeC, nodeP, nodeS);
	doubleBlackCases(caseNum, tree, nodeC, nodeP, nodeS);
}

/**
 * Double Black Case: P is Black
 * @param caseNum: Case num
 * @param tree:  Tree
 * @param nodeC: child node.
 * @param nodeP: parent node.
 * @param nodeS: sibling node.
 */
static void dbCasePBlack
		(RBTree *const tree, Node **const nodeC, Node **const nodeP, Node **const nodeS)
{
	(*nodeS)->color = RED;
	updateDBPointers(nodeC, nodeP, nodeS);
	int caseNum = getCaseOfFixUpCase3(tree, nodeC, nodeP, nodeS);
	doubleBlackCases(caseNum, tree, nodeC, nodeP, nodeS);
}

/**
 * Double Black Case: S and S.Far from C are black.
 * @param nodeC: child node.
 * @param nodeP: parent node.
 * @param nodeS: sibling node.
 * @param tree
 */
static void dbCaseSAndFarAreBlack(Node **const nodeP, Node **const nodeS, RBTree *const tree)
{
	Node *nodeSc = NULL;
	Node *nodeSf = NULL;
	setNodeAsCloseChild(&nodeSc, *nodeS, *nodeP);
	setNodeAsFarChild(&nodeSf, *nodeS, *nodeP);
	nodeSc->color = BLACK;
	(*nodeS)->color = RED;
	if (*nodeS == (*nodeP)->right)
	{
		rightRotate(nodeS, &nodeSc, tree);
	}
	else
	{
		leftRotate(nodeS, &nodeSc, tree);
	}
	// Move to step dB
//	updateDBPointers(nodeC, nodeP, nodeS);
	dbCaseSAndCloseAreBlack(nodeP, &nodeSc, tree);
}

/**
 * S and S.Close from C are black.
 * @param nodeC: child node.
 * @param nodeP: parent node.
 * @param nodeS: sibling node.
 * @param tree
 */
static void dbCaseSAndCloseAreBlack(Node **const nodeP, Node **const nodeS, RBTree *const tree)
{
	// Swap Colors:
	swapColors(nodeS, nodeP);

	if (*nodeS == (*nodeP)->right)
	{
		(*nodeS)->right->color = BLACK;
		leftRotate(nodeP, nodeS, tree);
	}
	else
	{
		(*nodeS)->left->color = BLACK;
		rightRotate(nodeP, nodeS, tree);
	}
}


/**
 * Get the specific case to bal the tree after delete.
 * Check Case 1/ Case 2/ Case3 (and specific case in 3).
 * @param tree: Tree object
 * @param nodeM: Deleted Node
 * @param nodeC: child node.
 * @param nodeP: parent node.
 * @param nodeS: sibling node.
 * @param skipOneAndTwoCases: Boolean varible - if the function has to check first case and
 * second case to skip directly to case 3.
 * @return
 */
static int getCaseOfFixUp
		(RBTree *const tree, Node **const nodeM, Node **const nodeC, Node **const nodeP,
		 Node **const nodeS, const bool skipOneAndTwoCases)
{
	if (skipOneAndTwoCases == false)
	{
		if (isRedColor(*nodeM))
		{
			return M_RED;
		}
		else if ((isBlackColor(*nodeM)) AND (isRedColor(*nodeC)))
		{
			return M_BLACK_C_RED;
		}
		*nodeC = *nodeM;
	}
	if (isBlackColor(*nodeM) AND isBlackColor(*nodeC))
	{
		return getCaseOfFixUpCase3(tree, nodeC, nodeP, nodeS);
	}
	//TODO DO_NOTHING case = check in the function if DO_NOTHING returned!!!!
	return DO_NOTHING;
}

/**
 * Check the current situation of the tree - After delete and if Case 1 and Case 2 are not the
 * cases so the case is that M is Black and C is black.
 * return the specific case.
 * @param tree: Tree.
 * @param nodeC: child node.
 * @param nodeP: parent node.
 * @param nodeS: sibling node.
 * @return
 */
static int getCaseOfFixUpCase3
		(RBTree *const tree, Node **const nodeC, Node **const nodeP, Node **const nodeS)
{
	if (tree->root == *nodeC)
	{
		return C_IS_ROOT;
	}
		// Check if S and his children are black:
	else if (((*nodeS) == NULL) OR
			 ((isBlackColor(*nodeS)) AND
			 ((isBlackColor((*nodeS)->left)) AND
			 (isBlackColor((*nodeS)->right)))))
	{
		if (isRedColor(*nodeP))
		{
			return P_RED;
		}
		else if (isBlackColor(*nodeP))
		{
			return P_BLACK;
		}
	}
	else if (isRedColor(*nodeS))
	{
		return S_RED;
	}
	Node *farChildOfSToC = NULL;
	setNodeAsFarChild(&farChildOfSToC, *nodeS, *nodeP);
	if ((isBlackColor(*nodeS)) AND (isBlackColor(farChildOfSToC)))
	{
		return S_AND_FAR_BLACK;
	}
	else if (isRedColor(farChildOfSToC))
	{
		return S_AND_FAR_RED;
	}
	return DO_NOTHING;
}

/**
 * Move the DB to the parent of C node and update all Family to the relavent pointers.
 * @param nodeC
 * @param nodeP
 * @param nodeS
 */
static void updateDBPointers(Node **const nodeC, Node **const nodeP, Node **const nodeS)
{
	*nodeC = *nodeP;
	*nodeP = (*nodeC)->parent;
	if (*nodeP)  // In case that C is not Root
	{
		*nodeS = ((*nodeP)->right == *nodeC) ? (*nodeP)->left : (*nodeP)->right;
	}
}

//__________________________________RB Tree tools__________________________________________________

/**
 * Rotate Right Function
 * @param grand
 * @param par
 * @param tree
 */
static void rightRotate(Node **const grand, Node **const par, RBTree *const tree)
{
	(*grand)->left = (*par)->right;
	if ((*par)->right)
	{
		(*par)->right->parent = *grand;
	}
	// In case that the grandfather is the root of the tree.
	if ((*grand) == tree->root)
	{
		tree->root = *par;
		(*par)->parent = NULL;
	}
	else // In case that grand has parent.
	{
		if (isNodeIsRightChild(*grand) == true)
		{
			(*grand)->parent->right = *par;
			(*par)->parent = (*grand)->parent;
		}
		else
		{
			(*grand)->parent->left = *par;
			(*par)->parent = (*grand)->parent;
		}
	}
	(*grand)->parent = *par;
	(*par)->right = (*grand);
	//Change colors to default.
//	(*par)->color = BLACK, (*grand)->color = RED;
}

/**
 * Left Rotate.
 * @param grand
 * @param par
 * @param tree
 */
static void leftRotate(Node **const grand, Node **const par, RBTree *const tree)
{
	(*grand)->right = (*par)->left;
	if ((*par)->left)
	{
		(*par)->left->parent = *grand;
	}
	// In case that the grandfather is the root of the tree.
	if ((*grand) == tree->root)
	{
		tree->root = *par;
		(*par)->parent = NULL;
	}
	else // In case that grand has parent.
	{
		if (isNodeIsRightChild(*grand))
		{
			(*grand)->parent->right = *par;
			(*par)->parent = (*grand)->parent;
		}
		else
		{
			(*grand)->parent->left = *par;
			(*par)->parent = (*grand)->parent;
		}
	}
	(*grand)->parent = *par;
	(*par)->left = (*grand);
}

/**
 * Gets a and b nodes and swap their colors.
 * @param a
 * @param b
 */
static void swapColors(Node **const a, Node **const b)
{
	int color = (*a)->color;
	(*a)->color = (*b)->color;
	(*b)->color = color;
}

/**
 * Checks if the color if the node is Black.
 * @param node
 * @return
 */
static int isBlackColor(const Node *node)
{
	if (node == NULL || node->color == BLACK)
	{
		return true;
	}
	return false;
}

/**
 * Checks if the color of node is red.
 * @param node
 * @return
 */
static int isRedColor(const Node *node)
{
	if (node == NULL || node->color == BLACK)
	{
		return false;
	}
	return true;
}

/**
 * Set uncle pointer.
 * @param uncle
 * @param grand
 * @param par
 */
static void setUncle(Node **uncle, const Node *grand, const Node *par)
{
	*uncle = (grand->left == par) ? grand->right : grand->left;
}

/**
 * Set dest node as the close child to P node of S node
 * @param dest: Pointer to Dest node.
 * @param nodeS: Sibling of C node - child of P.
 * @param nodeP: Parent of C node.
 */
static void setNodeAsCloseChild(Node **dest, const Node *nodeS, const Node *nodeP)
{
	*dest = (nodeS == nodeP->left) ? nodeS->right : nodeS->left;
}

/**
 * Set dest node as the close child to P node of S node
 * @param dest: Pointer to Dest node.
 * @param nodeS: Sibling of C node - child of P.
 * @param nodeP: Parent of C node.
 */
static void setNodeAsFarChild(Node **dest, const Node *nodeS, const Node *nodeP)
{
	*dest = (nodeS == nodeP->left) ? nodeS->left : nodeS->right;
}



//__________________________________BASIC BST FUNCTIONS____________________________________________

/**
 * Function that gets a pointer to a node and change the poiner to point on the successor of node
 * @param node
 */
static void successor(Node **node)
{
	if (node == NULL OR *node == NULL)
	{
		return;
	}
	Node *cur = NULL;
	// Go to right subtree - if there is one
	if ((*node)->right != NULL)
	{
		cur = (*node)->right;
		findMin(&cur);
		*node = cur;
	}
		// Claim up until you get to parent from his left child.
	else
	{
		cur = *node;
		while (cur->parent)
		{
			if (cur->parent->left == cur)
			{
				*node = cur->parent;
				return;
			}
			cur = cur->parent;
		}
		*node = NULL;    // In case that node is the max element.
	}
}

/**
 * Function that gets a pointer to node and change to pointer to point on the min node.
 * @param cur
 */
static void findMin(Node **cur)
{
	if (cur == NULL OR *cur == NULL)
	{
		return;
	}
	//Go left until there is no more left child.
	while ((*cur)->left != NULL)
	{
		*cur = (*cur)->left;
	}
}

/**
 * Set a new root for the tree.
 * @param tree
 * @param data
 * @return
 */
static int setRoot(RBTree *const tree, void *const data)
{
	tree->root = allocateNode(data);
	if (tree->root == NULL)  // Allocate Failed
	{
		return FUNC_FAIL;
	}
	// Always the color of the root is black.
	tree->root->color = BLACK;
	return FUNC_SUCCESS;
}

/**
 *
 * @param cur
 * @param data
 * @param compare
 * @return
 */
static int find(Node **cur, const void *data, const CompareFunc compare)
{
	while (*cur != NULL)  // Travel on the tree
	{
		int comp = compare(data, (*cur)->data);
		if (comp == EQUAL)
		{
			return EQUAL;
		}
		else if (comp >= GREATER)
		{
			if ((*cur)->right == NULL)
			{
				return GREATER;
			}
			*cur = (*cur)->right;
		}
		else
		{
			if ((*cur)->left == NULL)
			{
				return LESS;
			}
			*cur = (*cur)->left;
		}
	}
	return DO_NOTHING;
}

/**
 * Set new leaf.
 * @param parent - the parent of the new leaf
 * @param childSide - Left or
 * @param data
 * @return
 */
static Node *setNewLeaf(Node *parent, int childSide, void *const data)
{

	Node *leaf = allocateNode(data);
	if (leaf == NULL) // Allocate Failed
	{
		return NULL;
	}
	leaf->parent = parent;

	if (childSide == LEFT)
	{
		parent->left = leaf;
	}
	else
	{
		parent->right = leaf;
	}
	return leaf;
}


/**
 * Swap Data between 2 Nodes - Swap only the data
 * @param a : First Node
 * @param b : Second Node
 */
static void swapData(Node **first, Node **second)
{
	Node *data = (*first)->data;
	(*first)->data = (*second)->data;
	(*second)->data = data;
}


/**
 * Fucntion that gets a node and return how many children the node has
 * @param node
 * @return -1 if node is null, else amount of children - {0,1,2}
 */
static int numChildren(Node *const node)
{
	if (node == NULL)
	{
		return -1;
	}
	if ((node->right != NULL) && (node->left != NULL))
	{
		return TWO_CHILDREN;
	}
	else if ((node->right != NULL) || (node->left != NULL))
	{
		return ONE_CHILD;
	}
	return ZERO_CHILDREN;
}

/**
 *
 * @param node
 * @return
 */
static int isNodeIsRightChild(const Node *node)
{
	if (node->parent->right == node)
	{
		return true;
	}
	return false;
}

/**
 *
 * @param node
 * @return
 */
static int isNodeIsLeftChild(const Node *node)
{
	if (node->parent->left == node)
	{
		return true;
	}
	return false;
}

/**
 *
 * @param node
 * @param t
 * @return
 */
static int isNodeIsRoot(const Node *node, const RBTree *t)
{
	if (node == t->root)
	{
		return true;
	}
	return false;
}



//____________________________________MEMORY MANAGEMENT____________________________________________
/**
 * Functions that gets a data and create a new node by MALLOC!
 * set the default parms of new node and return the node.
 * @param data: data for the new node.
 * @return: New node if malloc succeeded otherwise NULL
 */
static Node *allocateNode(void *data)
{
	Node *newNode = (Node *) malloc(sizeof(Node));
	if (newNode == NULL)
	{
		return NULL;
	}
	newNode->left = NULL;
	newNode->right = NULL;
	newNode->parent = NULL;
	newNode->color = RED;
	newNode->data = data;
	return newNode;
}


/**
 * free all memory of the RB tree:
 * 1. tree.
 * 2. Nodes.
 * 3. Data of nodes.
 * @param tree: pointer to the tree to free.
 */
void freeRBTree(RBTree **tree)
{
	if (tree == NULL OR (*tree) == NULL)
	{
		return;
	}
	helperFreeRBTree(&((*tree)->root), (*tree)->freeFunc);
	//Free tree
	(*tree)->root = NULL;
	free(*tree);
	*tree = NULL;
}

/**
 * Free in recursive all nodes in tree - Left->Parent->Right recursive.
 * @param node 
 * @param tree 
 */
static void helperFreeRBTree(Node **node, const FreeFunc freeData)
{
	if (node == NULL OR (*node) == NULL)
	{
		return;
	}
	//Recursive Left
	helperFreeRBTree(&((*node)->left), freeData);
	// Save right child
	Node *right = (*node)->right;
	// Free node
	freeNode(node, freeData);
	*node = NULL;
	//Recursive Right
	helperFreeRBTree(&right, freeData);
}

/**
 * Function that free node - gets an freedata func to free the data of the node.
 * @param freedNode: Node that has to be freed.
 * @param freeData : function that frees the data of the node.
 */
static void freeNode(Node **freedNode, const FreeFunc freeData)
{
	if (freedNode AND *freedNode)
	{
		if ((*(freedNode))->data)
		{
			freeData((*(freedNode))->data);
		}
		free(*(freedNode));
//		(*freedNode) = NULL;
	}
}
