//
// Created by Lior Kesten on 05/08/2020.
//

#ifndef C___VLVECTOR_HPP
#define C___VLVECTOR_HPP


#include <stdexcept>
#include <algorithm>

/**
 * Class VLVector : Container that exactly like vector cotainer , but the container jumps from
 * the stack to the heap - more efficient.
 * c is the constant memory static that
 * @tparam T : type of object such that the VLVector holds this objects
 * @tparam c : Constant Static memory
 */
template<class T, int c = 16>
class VLVector
{

	// __________________________ Public API ____________________________________________
public:

	// Typedef for API

	// API Vector container:
	typedef T value_type;
	typedef value_type &reference;
	typedef const value_type &const_reference;
	typedef value_type *pointer;
	typedef std::ptrdiff_t difference_type;

	// Iterators
	typedef T *iterator;  // Iterator - using pointer arithmetic
	typedef const T *const_iterator;  // ConstIterator - using pointer arithmetic


	// _________________________ Constructors ____________________________________
	/**
	 * Default Constructor
	 */
	inline VLVector() : _size(0), _cap(c), _memType(Stack), _heapContainer(nullptr),
						_begin(_stackContainer)
	{}

	/**
	 * Consrtuctor that gets an iterator of some input that at least it is a forward iterator and
	 * insert the values from the first to the last to the container.
	 * @tparam InputIterator
	 * @param first Input iterator - First element that should be inserted.
	 * @param last Input iterator - Last element that should be inserted.
	 */
	template<class InputIterator>
	inline VLVector(InputIterator first, InputIterator last) : VLVector()
	{ insert(begin(), first, last); }

	/**
	 * Copy Constructor
	 * @param other : another object.
	 */
	inline VLVector(const VLVector &other) : VLVector()
	{ *this = other; }

	/**
	 * Destructor - Free memory only if the array is on the Heap!
	 */
	inline ~VLVector()
	{
		if (_memType == Heap)
		{ delete[] _heapContainer; }
	}

	// __________________________________ Methods ____________________________________________
	/**
	 * @return number of elements that are in the array.
	 */
	inline size_t size() const noexcept
	{ return _size; }

	/**
	 * @return Capacity of the container - size of the array that can fill the elements.
	 */
	inline size_t capacity() const noexcept
	{ return _cap; }

	/**
	 * @return True or False if the array is empty (no elemnets)
	 */
	inline bool empty() const noexcept
	{ return _size == 0; }

	/**
	 * Function that returns the i' element. In case of index out of error there is an exception
	 * @param i : index
	 * @return : The i'th elemnent in the array by reference
	 */
	inline reference at(size_t i) noexcept(false)
	{
		if (i >= _size)
		{ throw std::out_of_range("Index out of error"); }
		return _begin[i];
	}

	/**
	 * returns the i' element in const reference. In case of index out of error there is an
	 * exception
	 * @param i index
	 * @return The i'th elemnent in the array by const reference
	 */
	inline const_reference at(size_t i) const noexcept(false)
	{
		if (i >= _size)
		{ throw std::out_of_range("Index out of error"); }
		return _begin[i];
	}

	/**
 	* function that clear the container - pop back all items.
 	*/
	void clear() noexcept
	{
		while (!empty())
		{ pop_back(); }
	}

	/**
	 * @return the pointer to the first element in the array - Type of the container- Heap or Stack
	 */
	inline pointer data() noexcept
	{ return _begin; }

	/**
	 * Const Data
	 * @return the pointer to the first element in the array - Type of the container- Heap or Stack
	 */
	inline const pointer data() const noexcept
	{ return _begin; }


	//  ___________________ Begin Iterators ______________________
	/**
	 * @return iterator of VLVector that is point to the first element.
	 */
	inline iterator begin() noexcept
	{ return _begin; }

	/**
	 * @return const_iterator of VLVector that is point to the first element
	 */
	inline const_iterator begin() const noexcept
	{ return _begin; }

	/**
	 * @return const_iterator of VLVector that is point to the first element
	 */
	inline const_iterator cbegin() const noexcept
	{ return _begin; }
	// ___________________ End Iterators ______________________
	/**
	 * @return iterator of VLVector that is point to the last element +1
	 */
	inline iterator end() noexcept
	{ return _begin + _size; }

	/**
	 * @return const_iterator of VLVector that is point to the last element +1
	 */
	inline const_iterator end() const noexcept
	{ return _begin + _size; }

	/**
	 * @return onst_iterator of VLVector that is point to the last element +1
	 */
	inline const_iterator cend() const noexcept
	{ return _begin + _size; }

	// ________________________ Add Methods ________________________________________

	/**
	 * Function that add new item to the container, in case that need to change the memory to
	 * stack from heap or from heap to larger size in the heap it allocate new memory (handle
	 * with the delete)
	 * @param new_item - Object T that should inserted to the container.
	 */
	void push_back(const value_type new_item)
	{
		// If we have to increase the capacity:
		if (_size == _cap)
		{
			pointer p = _begin;  // Keep a pointer for free.
			_updateContainer();  // Update container
			if (_memType == Heap)  // delete in case the already memory allocated.
			{
				delete[] p;
			}
			_memType = Heap; // Update the memory type.
		}
		_begin[_size] = new_item;  // Add new item.
		++_size;  // Increase the size of the container.
	}

	/**
	 * Insert new item to the container before the pos position (pos is a iterator that point the
	 * some object in the container), Handle  with memory like push_back.
	 * @param pos - iterator that points to some object in the array
	 * @param new_item - New object T.
	 */
	iterator insert(const_iterator pos, const_reference new_item)
	{
		difference_type diffFromStart = pos - _begin;  // Keep the delta between the pointers.
		push_back(new_item); // Insert item to the container.
		// Set iterator that points to the pos in the new container
		auto nonConstPos = _begin + diffFromStart;
		for (auto it = end() - 1; it > nonConstPos; --it)
		{
			*it = *(it - 1);
		}
		*(_begin + diffFromStart) = new_item;
		return _begin + diffFromStart;
	}

	/**
	 * Function that gets position of some object in the container (iterator) and First and Last
	 * Iterators that points to some container. The function insert all elements from [firs,last)
	 * to the position.
	 * @tparam InputIterator : Some iterator (at least input iterator type)
	 * @param position : Iterator that points to some element in the array.
	 * @param first : Iterator of InputIterator object that points to the first element that
	 * would be inserted.
	 * @param last : Iterator of InputIterator object that points to the last element (this
	 * element won't be added to the array)
	 * @return Iterator that points to the first element that was inserted.
	 */
	template<class InputIterator>
	iterator insert(const_iterator position, InputIterator first, InputIterator last)
	{
		difference_type diffFromStart = position - _begin;
		// Step 1: count elements in the range [first,last)-> k and insert k random values to array
		size_t k = 0;
		for (auto it = first; it != last; ++it, ++k)
		{
			push_back(*first);
		}
		// Step 3: copy the data from pos to n-k index:
		for (auto it = end() - k - 1; it >= _begin + diffFromStart; --it)
		{
			*(it + k) = *(it);
		}
		// Step 4: insert the k items from the new container to the VLVector:
		auto secIt = begin() + diffFromStart;
		for (size_t i = 0; i < k; ++i, ++first, ++secIt)
		{
			*secIt = *first;
		}
		return _begin + diffFromStart;
	}
	// ________________________ Delete Methods ________________________________________

	/**
	 * Function that pop_back the last element from the container.
	 * If the capacity is less than c, it change the container to the Stack.
	 */
	void pop_back()
	{
		if (_size > 0)
		{
			--_size;  // Decrease size

			if (_size <= c && _memType == Heap)    // Checks if need to change to Stack
			{
				// Copy values from heap container to stack container
				std::copy(begin(), end(), iterator(_stackContainer));
				delete[] _heapContainer;    // delete heap container
				_begin = _stackContainer;  // Move the ptr to the stack
				_updateMembers(_size, c, Stack); // Update members
			}
		}
	}

	/**
	 * Erase the element that pos is point to.
	 * @param pos Iterator that points to some elements in the array.
	 * @return Iterator that points to element that is next to the element that was erased
	 */
	iterator erase(const_iterator pos)
	{
		difference_type diffFromStart = pos - begin();  // Keep the delta between the pointers.
		for (auto it = _begin + diffFromStart; it < end() - 1; ++it)
		{
			*it = *(it + 1);
		}
		pop_back();
		return _begin + diffFromStart;  // Return the element from the right to the remove element.
	}

	/**
	 * Erase elements - erase all the elemnets in the range [first,last).
	 * @param first Iterator that points to the first element that should be erased
	 * @param last Iterator that points to the last element in the container that won't deleted
	 * @return Iterator to the element that is right to the elements that erased.
	 */
	iterator erase(const_iterator first, const_iterator last)
	{
		difference_type diffFromStart = first - begin();
		difference_type diffFromEnd = last - first;

		for (auto nonConstFirst = begin() + diffFromStart; last < end(); ++last, ++nonConstFirst)
		{
			*nonConstFirst = *last;
		}
		for (int i = 0; i < diffFromEnd; ++i)
		{
			pop_back();
		}
		return _begin + diffFromStart;
	}

	// ______________________ Operators ____________________________________________
	/**
	 * Assignment operator.
	 * @param other
	 * @return VLVector by reference.
	 */
	VLVector &operator=(const VLVector &other)
	{
		if (this != &other)
		{
			if (_memType == Heap)  // In case that memory has to be deleted.
			{
				delete[] _heapContainer;
			}

			_updateMembers(other._size, other._cap, other._memType);
			if (other._memType == Heap)  // Allocate new memory in case that
			{
				_heapContainer = new T[other._cap];
			}
			// Set begin to heap memory if already memory allocated.
			_begin = (_memType == Heap) ? _heapContainer : _stackContainer;
			std::copy(other.cbegin(), other.cend(), begin());
		}
		return *this;
	}

	/**
	 * Brackets operator - non const version
	 * @param i index
	 * @return  i'th element - with limits check
	 */
	inline reference operator[](size_t i) noexcept
	{ return _begin[i]; }

	/**
	 * Brackets operator - non const version
	 * @param i index
	 * @return  i'th element - with limits check
	 */
	inline const_reference operator[](size_t i) const noexcept
	{ return _begin[i]; }

	/**
	 * @param rhs : VLVector object.
	 * @return True or False if two elements are equal
	 */
	bool operator==(const VLVector<T, c> &rhs) const
	{
		if (_size != rhs._size)
		{
			return false;
		}
		for (size_t i = 0; i < _size; ++i)
		{
			if (!(_begin[i] == rhs._begin[i]))
			{
				return false;
			}
		}
		return true;
	}

	/**
	 * @param rhs : VLVector object.
	 * @return True or False if two elements are not equal
	 */
	inline bool operator!=(const VLVector<T, c> &rhs) const
	{ return !(*this == rhs); }


	// _________________________ Private API __________________________________
private:
	/**
	 * Enumerate for memory Type : Sign to where the array is now saved
	 */
	enum MemoryType
	{
		Heap,  // Sign for Heap
		Stack  // Sign for Stack
	};
	// _______________ Private Members ______________________
	size_t _size = 0;  // Number of elements in the container
	size_t _cap = c;   // Size That were allocated to the container
	MemoryType _memType = Stack;  // Type of memory - Heap or Stack
	pointer _heapContainer;  // Dynamic array - Heap
	value_type _stackContainer[c]; // Static array - Heap
	// Pointer to the start of the array - switching between heap and stack container
	pointer _begin;

	// ____________________ Private API _______________________
	/**
	 * Private function that update the members of the object.
	 * @param newSize
	 * @param newCap
	 * @param newMemType
	 */
	inline void _updateMembers(size_t newSize, size_t newCap, MemoryType newMemType) noexcept
	{
		_size = newSize;
		_cap = newCap;
		_memType = newMemType;
	}

	/**
	 * Update the container from stack to heap or from heap to heap.
	 */
	inline void _updateContainer()
	{
		iterator first = begin(), last = end();
		_cap = _capC();  // Update capacity
		_heapContainer = new T[_cap];  // Allocate new memory
		_begin = _heapContainer; // Change the begin of the container.
		std::copy(first, last, begin());  // Copy the values.
	}

	/**
	 * Function that calculate the capC.
	 * @return new Capacity.
	 */
	static inline size_t _calCapC(size_t s) noexcept
	{ return ((3 * (s + 1)) / 2); }

	/**
	 * Function that return the new capacity of the container: c or new cap by the latter formula.
	 * @return new capacity
	 */
	inline size_t _capC() noexcept
	{
		if (_size + 1 < c)
		{
			return c;
		}
		return _calCapC(_size);
	}
};


#endif //C___VLVECTOR_HPP
