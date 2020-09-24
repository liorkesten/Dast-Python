import java.util.Collection;

/**
 * Wraps an underlying Collection and serves to both simplify its API and give it a common type with the
 * implemented SimpleHashSets.
 * @author liorkesten
 */
public class CollectionFacadeSet implements SimpleSet {

	/*The FacadeSet of collections*/
	private final Collection<String> collection;

	/**
	 * Creates a new facade wrapping the specified collection.
	 * @param collection - The Collection to wrap.
	 */
	public CollectionFacadeSet(java.util.Collection<java.lang.String> collection) {
		this.collection = collection;
	}


	@Override
	public boolean add(String newValue) {
		if (contains(newValue)) {
			return false;
		}
		return collection.add(newValue);
	}

	@Override
	public boolean contains(String searchVal) {
		return collection.contains(searchVal);
	}

	@Override
	public boolean delete(String toDelete) {
		return collection.remove(toDelete);
	}

	@Override
	public int size() {
		return collection.size();
	}
}
