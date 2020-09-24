import java.util.*;

/**
 * This class measure the time it takes to method apply on different SimpleSets
 * @author liorkesten
 */
public class SimpleSetPerformanceAnalyzer {
	// --------------------------- Static members --------------------------
	/* Num of iterations to do until the JVM warm up */
	private static final int NUM_OF_ITERATION_TO_WARP_UP_SET = 70000;
	/*Num of iterations to do check for average time*/
	private static final int NUM_OF_ITERATION_CHECKS_SET = 70000;
	/* Num of iterations to do until the JVM warm up */
	private static final int NUM_OF_ITERATION_WARP_UP_LIST = 7000;
	/*Num of iterations to do check for average time*/
	private static final int NUM_OF_ITERATION_CHECKS_LIST = 7000;

	/*Array of files to analyze methods on their dataset. */
	private static final String[][] ARRAY_OF_FILES = {
			Ex4Utils.file2array("data1.txt"),
			Ex4Utils.file2array("data2.txt")
	};

	/*Hash map contains that data structures */
	private static Map<String, SimpleSet> DATA_STRUCTURES;


	private static final String[] WORDS_TO_CHECK = {"hi", "-13170890158", "23"};

	// --------------------------- Main of the program --------------------------

	/**
	 * Main of the program
	 * @param args : None
	 */
	public static void main(String[] args) {
		measure();
	}

	// ------------------------------ Menus ----------------------------------------

	/**
	 * Main function that measure the time.
	 */
	public static void measure() {
		System.out.println("-----------------------File number 1----------------------------");
		DATA_STRUCTURES = createNewMapOfDS();
		measureFile(ARRAY_OF_FILES[0]);

		System.out.println("-----------------------File number 2----------------------------");
		DATA_STRUCTURES = createNewMapOfDS();
		System.out.println(DATA_STRUCTURES.get("OpenHashSet").size());
		measureFile(ARRAY_OF_FILES[1]);
	}

	/*This method invoke each data structure on specific data set (file)*/
	private static void measureFile(String[] file) {
		measureDataStructure(file, "OpenHashSet");
		measureDataStructure(file, "ClosedHashSet");
		measureDataStructure(file, "TreeSet");
		measureDataStructure(file, "LinkedList");
		measureDataStructure(file, "HashSet");
	}

	/*This method invoke each method on specific data structure and data set (file)*/
	private static void measureDataStructure(String[] words, String simpleSetName) {
		SimpleSet tempSet = DATA_STRUCTURES.get(simpleSetName);
		measureAdd(simpleSetName, tempSet, words);
		measureContains(simpleSetName, tempSet, WORDS_TO_CHECK[0]);
		measureContains(simpleSetName, tempSet, WORDS_TO_CHECK[1]);
		measureContains(simpleSetName, tempSet, WORDS_TO_CHECK[2]);
	}


	// ------------------------------ Add Method ----------------------------------------

	/*
	 *
	 * @param simpleSetName
	 * @param simpleSet
	 * @param wordsToAdd
	 */
	private static void measureAdd(String simpleSetName, SimpleSet simpleSet, String[] wordsToAdd) {
		long startTime = System.nanoTime();
		for (String word : wordsToAdd) {
			simpleSet.add(word);
		}
		long endTime = System.nanoTime();
		long totalTime = convertNanoSecToMilliSec(endTime - startTime);
		System.out.printf("Data structure: %s, Method: Add, Time: %s ms\n", simpleSetName, totalTime);
	}

	// ------------------------------ Contains Method ----------------------------------------

	/*
	 *Function that measure the time to add array of string into specific set.
	 * @param simpleSetName : The type of the SimpleSet
	 * @param simpleSet : Object of SimpleSet
	 * @param wordToCheck : The word to check if the SimpleSet contains it.
	 */
	private static void measureContains(String simpleSetName, SimpleSet simpleSet, String wordToCheck) {
		int iterationsToWarmUp = (simpleSetName.contains("Set")) ?
								 NUM_OF_ITERATION_TO_WARP_UP_SET : NUM_OF_ITERATION_WARP_UP_LIST;
		int iterationsToCheck = (simpleSetName.contains("Set")) ?
								NUM_OF_ITERATION_CHECKS_SET : NUM_OF_ITERATION_CHECKS_LIST;

		warmUpContains(iterationsToWarmUp, simpleSet, wordToCheck);
		long totalTime = calculateTimeContains(iterationsToCheck, simpleSet, wordToCheck);

		System.out.printf("Data structure: %s, Method: contains,word %s, Time: %s ns\n", simpleSetName,
						  wordToCheck, totalTime);
	}

	/*Warm up the contains method*/
	private static void warmUpContains(int n, SimpleSet simpleSet, String wordToCheck) {
		for (int i = 0; i < n; ++i) {
			simpleSet.contains(wordToCheck);
		}
	}

	/*Calculate the time of contains method*/
	private static long calculateTimeContains(int n, SimpleSet simpleSet, String wordToCheck) {
		long start = System.nanoTime();
		for (int j = 0; j < n; ++j) {
			simpleSet.contains(wordToCheck);
		}
		long end = System.nanoTime();
		return (end - start) / n;
	}

	/*This method return a new hashmap of new objects that the key is the name of the hashset*/
	private static Map<String, SimpleSet> createNewMapOfDS() {
		return new HashMap<String, SimpleSet>() {
			{
				put("OpenHashSet", new OpenHashSet());
				put("ClosedHashSet", new ClosedHashSet());
				put("TreeSet", new CollectionFacadeSet(new TreeSet<>()));
				put("LinkedList", new CollectionFacadeSet(new LinkedList<>()));
				put("HashSet", new CollectionFacadeSet(new HashSet<>()));
			}
		};

	}


	/*
	 * Convert nano seconds to milliseconds.
	 * @param nano : Nano time
	 * @return Milliseconds time.
	 */
	private static long convertNanoSecToMilliSec(long nano) {
		return nano / 1000000;
	}
}
