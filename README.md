This Python script provides a straightforward inventory management system for querying product prices, adding items to a cart, and generating a sorted bill based on user preferences. It features:

- Hash Table Implementation: Uses a custom hash table with DJB2 hashing and quadratic probing for efficient product lookups. This structure handles inventory data with reduced collision likelihood and fast retrieval.

- Bubble Sort: Organizes the cart based on user preference. It sorts items either by price in ascending order or by quantity, using a simple comparison-based algorithm.

- Interactive User Input: Users enter items in the format `quantity:product name`, which the script processes to update the cart and calculate total costs. After entering items, users can choose to sort the final bill by price or quantity.

The dataset, `InventoryData.xlsx`, sourced from Kaggle, contains product names and retail prices used for managing inventory and computing costs.
