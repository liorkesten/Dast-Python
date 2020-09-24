import java.util.LinkedList;
import java.util.List;

/**
 * a hash-set based on chaining.
 * @author liorkesten
 */
public class OpenHashSet extends SimpleHashSet {
	/**
	 * Private class Node - A wrapper for linked list. enable create array of Linked list.
	 * @author liorkesten
	 */
	private class Node {
		/*
		Data member of linked list.
		 */
		private final List<String> linkedList;

		// ------------ Constructor -------------
		private Node() {
			linkedList = new LinkedList<>();
		}
	}

	// ---------------------------- Private Class members --------------------------
	/* Default size for new object.*/
	private static final int DEFAULT_SIZE = 0;
	/*In case the we need to increase the capacity- multiply by this value*/
	private static final int MULTIPLY_CAPACITY = 2;
	/*Min valid capacity*/
	private static final int MIN_CAPACITY = 1;


	// ---------------------------- Private data members --------------------------
	/* Array of the linked lists -table of the hash*/
	private Node[] table;
	/* Size*/
	private int size;
	/* Capacity*/
	private int capacity;

	/**
	 * Constructs a new, empty table with the specified load factors, and the default initial capacity (16).
	 * @param upperLoadFactor The upper load factor of the hash table.
	 * @param lowerLoadFactor The lower load factor of the hash table.
	 */
	public OpenHashSet(float upperLoadFactor, float lowerLoadFactor) {
		super(upperLoadFactor, lowerLoadFactor);
		capacity = INITIAL_CAPACITY;
		table = new Node[capacity];
		size = DEFAULT_SIZE;


	}

	/**
	 * A default constructor. Constructs a new, empty table with default initial capacity (16), upper load
	 * factor (0.75) and lower load factor (0.25).
	 */
	public OpenHashSet() {
		this(DEFAULT_HIGHER_CAPACITY, DEFAULT_LOWER_CAPACITY);
	}

	/**
	 * Data constructor - builds the hash set by adding the elements one by one. Duplicate values should be
	 * ignored. The new table has the default values of initial capacity (16), upper load factor (0.75), and
	 * lower load factor (0.25).
	 * @param data Values to add to the set.
	 */
	public OpenHashSet(java.lang.String[] data) {
		this();
		for (String str : data) {
			add(str);
		}
	}


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
		int indexTable = getIndexTable(newValue);

		if (table[indexTable] == null) {
			table[indexTable] = new Node();
		}
		++size;
		table[indexTable].linkedList.add(newValue);
		return true;
	}

	/*Get the supposed index of the table of the newValue.*/
	private int getIndexTable(String newValue) {
		return clamp(newValue.hashCode());
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
		Node[] temp = table;  // Keep the last table
		size = DEFAULT_SIZE;
		updateCapacity(increase);
		table = new Node[capacity];
		for (Node node : temp) {
			if (node != null) {
				for (String str : node.linkedList) {
					add(str);
				}
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
		int indexTable = getIndexTable(searchVal);
		if (table[indexTable] != null) {
			for (String str : table[indexTable].linkedList) {
				if (str.equals(searchVal)) {
					return true;
				}
			}
		}
		return false;
	}

	/**
	 * Remove the input element from the set.
	 * @param toDelete - Value to delete
	 * @return True iff toDelete is found and deleted
	 */
	public boolean delete(java.lang.String toDelete) {
		int indexTable = getIndexTable(toDelete);
		if (!contains(toDelete) || table[indexTable] == null) {
			return false;
		}
		table[indexTable].linkedList.remove(toDelete);
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
	public int capacity() {return capacity;}
}
