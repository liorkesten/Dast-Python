/**
 * A superclass for implementations of hash-sets implementing the SimpleSet interface.
 * @author liorkesten
 */
public abstract class SimpleHashSet implements SimpleSet {

	// -----------------------------Class members --------------------------
	/**
	 * Describes the capacity of a newly created hash set.
	 */
	protected static final int INITIAL_CAPACITY = 16;
	/**
	 * Describes the lower load factor of a newly created hash set.
	 */
	protected static final float DEFAULT_LOWER_CAPACITY = 0.25f;
	/**
	 * Describes the higher load factor of a newly created hash set.
	 */
	protected static final float DEFAULT_HIGHER_CAPACITY = 0.75f;
	// -----------------------------Private Data members --------------------------
	/*
	 *  Upper load factor data member
	 */
	private final float upperLoadFactor;
	/*
	 * Lower load factor data member
	 */
	private final float lowerLoadFactor;
	// -----------------------------Methods --------------------------

	/**
	 * Constructs a new hash set with capacity INITIAL_CAPACITY.
	 * @param upperLoadFactor - the upper load factor before rehashing
	 * @param lowerLoadFactor - the lower load factor before rehashing
	 */
	protected SimpleHashSet(float upperLoadFactor, float lowerLoadFactor) {
		this.upperLoadFactor = upperLoadFactor;
		this.lowerLoadFactor = lowerLoadFactor;
	}

	/**
	 * Constructs a new hash set with the default capacities given in DEFAULT_LOWER_CAPACITY and
	 * DEFAULT_HIGHER_CAPACITY.
	 */
	protected SimpleHashSet() {
		this(DEFAULT_HIGHER_CAPACITY, DEFAULT_LOWER_CAPACITY);
	}

	/**
	 * @return The current capacity (number of cells) of the table.
	 */
	public abstract int capacity();

	/**
	 * @return The lower load factor of the table.
	 */
	protected float getLowerLoadFactor() {return lowerLoadFactor;}

	/**
	 * @return The higher load factor of the table.
	 */
	protected float getUpperLoadFactor() {return upperLoadFactor;}

	/**
	 * Clamps hashing indices to fit within the current table capacity (see the exercise description for
	 * details)
	 * @param index - the index before clamping.
	 * @return an index properly clamped.
	 */
	protected int clamp(int index) {
		return index & (capacity() - 1);
	}
}
