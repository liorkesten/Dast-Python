/**
 * a hash-set based on closed-hashing with quadratic probing. Extends SimpleHashSet
 * @author liorkesten
 */
public class ClosedHashSet extends SimpleHashSet {

	// ---------------------------- Private Class members --------------------------
	/* Default size for new object.*/
	private static final int DEFAULT_SIZE = 0;
	/*In case the we need to increase the capacity- multiply by this value*/
	private static final int MULTIPLY_CAPACITY = 2;
	/*Min valid capacity*/
	private static final int MIN_CAPACITY = 1;
	/*This is unique string- by the "new" keyword I've created unique string such that there are no other
	strings that will reference this object too.*/
	private static final String UNIQUE_STRING = new String("The word is doesnt matter - I'm Unique string");

	// ---------------------------- Private data members --------------------------
	/* Size*/
	private int size;
	/* Capacity*/
	private int capacity;

	/**/
	private String[] table;
	// ---------------------------- Constructor --------------------------

	/**
	 * Constructs a new, empty table with the specified load factors, and the default initial capacity (16).
	 * @param upperLoadFactor The upper load factor of the hash table.
	 * @param lowerLoadFactor The lower load factor of the hash table.
	 */
	public ClosedHashSet(float upperLoadFactor, float lowerLoadFactor) {
		super(upperLoadFactor, lowerLoadFactor);
		capacity = INITIAL_CAPACITY;
		size = DEFAULT_SIZE;
		table = new String[capacity];
	}

	/**
	 * A default constructor. Constructs a new, empty table with default initial capacity (16), upper load
	 * factor (0.75) and lower load factor (0.25).
	 */
	public ClosedHashSet() {
		this(DEFAULT_HIGHER_CAPACITY, DEFAULT_LOWER_CAPACITY);

	}

	/**
	 * Data constructor - builds the hash set by adding the elements one by one. Duplicate values should be
	 * ignored. The new table has the default values of initial capacity (16), upper load factor (0.75), and
	 * lower load factor (0.25).
	 * @param data Values to add to the set.
	 */
	public ClosedHashSet(java.lang.String[] data) {
		this();
		for (String str : data) {
			add(str);
		}
	}
	// ---------------------------- Methods --------------------------


	/**
	 * Add a specified element to the set if it's not already in it.
	 * @param newValue - New value to add to the set
	 * @return False iff newValue already exists in the set
	 */
	public boolean add(java.lang.String newValue) {
		if (contains(newValue)) {
			return false;
		}
		if (shouldResize(true)) {
			resize(true);
		}
		++size;
		for (int i = 0; i < capacity; ++i) {
			int indexTable = getIndexTable(newValue, i);
			if (table[indexTable] == null) {
				table[indexTable] = newValue;
				break;
			}
		}
		return true;
	}


	/*
	 * Checks if we have to resize - isAdd true <-> add methods call this func, otherwise delete called.
	 * @return
	 */
	private boolean shouldResize(boolean isAdd) {
		return (isAdd) ?
			   (float) (size + 1) / capacity > getUpperLoadFactor() :
			   (float) size / capacity < getLowerLoadFactor();
	}

	/*
	 * Function that resize the table.
	 * @param increase : Boolean param - if true increase the capacity, else decrease.
	 */
	private void resize(boolean increase) {
		String[] temp = table;  // Keep the last table
		size = DEFAULT_SIZE;
		updateCapacity(increase);
		table = new String[capacity];
		for (String str : temp) {
			if (str != null && str != UNIQUE_STRING) {
				add(str);
			}
		}
	}


	/*Update the capacity - increase or decrease, if decrease, checks that the capacity is not lower than
the min capacity*/
	private void updateCapacity(boolean increase) {
		capacity = (increase) ? capacity * MULTIPLY_CAPACITY : capacity / MULTIPLY_CAPACITY;
		capacity = Math.max(capacity, MIN_CAPACITY);
	}


	/**
	 * Look for a specified value in the set.
	 * @param searchVal - Value to search for
	 * @return True iff searchVal is found in the set
	 */
	public boolean contains(java.lang.String searchVal) {
		for (int i = 0; i < capacity; ++i) {
			int tableIndex = getIndexTable(searchVal, i);
			if (table[tableIndex] == null) {
				return false;
			} else if (table[tableIndex] == UNIQUE_STRING || !table[tableIndex].equals(searchVal)) {
				continue;
			}
			return true;
		}
		return false;
	}

	/**
	 * Remove the input element from the set.
	 * @param toDelete - Value to delete
	 * @return True iff toDelete is found and deleted
	 */
	public boolean delete(java.lang.String toDelete) {
		if (!contains(toDelete)) {
			return false;
		}
		for (int i = 0; i < capacity; ++i) {
			int tableIndex = getIndexTable(toDelete, i);
			if (table[tableIndex] != null &&
				table[tableIndex] != UNIQUE_STRING &&
				table[tableIndex].equals(toDelete)) {
				table[tableIndex] = UNIQUE_STRING;
				break;
			}
		}
		--size;
		if (shouldResize(false)) {
			resize(false);
		}
		return true;
	}

	/**
	 * @return The number of elements currently in the set
	 */
	public int size() {
		return size;
	}

	/**
	 * capacity in class SimpleHashSet
	 * @return The current capacity (number of cells) of the table.
	 */
	public int capacity() {
		return capacity;
	}


	/*Function that compose clamp on get new index and returns the index if the table*/
	private int getIndexTable(String str, int i) {
		return clamp(getNewIndex(str, i));
	}

	/*
		Get the new hash value of the next index  by probing hashing
	 */
	private int getNewIndex(String str, int i) {
		return str.hashCode() + ((i) + (i * i)) / 2;
	}
}
