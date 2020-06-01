public class Program {
	public class LRUCache {
		public int maxSize;

		public LRUCache(int maxSize) {
			this.maxSize = maxSize > 1 ? maxSize : 1;
		}

		public void InsertKeyValuePair(string key, int value) {
			// Write your code here.
		}

		public LRUResult GetValueFromKey(string key) {
			// Write your code here.
			return null;
		}

		public string GetMostRecentKey() {
			// Write your code here.
			return null;
		}
	}

	public class LRUResult {
		public bool found;
		public int value;

		public LRUResult(bool found, int value) {
			this.found = found;
			this.value = value;
		}
	}
}