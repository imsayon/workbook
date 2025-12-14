---

## Module 1 – Q1

**Palindrome Extraction Using File Handling**

String slicing (`[::-1]`) is used to reverse each word for palindrome checking. Slicing creates a new reversed string, which takes linear time proportional to the length of the word. Since slicing is applied only to words of length greater than or equal to five, unnecessary operations are avoided. Although slicing creates temporary strings, it is internally optimized and provides better readability and maintainability compared to manual character-by-character reversal. For typical text file sizes, this approach is efficient and practical.

---

## Module 1 – Q2

**Menu-Driven String Operations**

Built-in string methods such as `upper()`, `count()`, and `startswith()` are implemented at the interpreter level and are optimized for performance. These methods reduce the need for explicit loops, making the code shorter, clearer, and less error-prone. Using built-in methods improves execution speed and ensures reliable string manipulation compared to manually iterating through characters.

---

## Module 2 – Q1

**Statistical Operations on a List of Integers**

Python lists are mutable, meaning changes made to a list inside a function affect the original list passed to it. Operations such as sorting and duplicate removal modify the list structure directly. If the original list needs to be preserved, a copy should be created before performing modifications. Understanding list mutability helps avoid unintended side effects and ensures predictable function behavior.

---

## Module 2 – Q2

**Student Records Using List of Tuples**

A list of tuples requires linear searching for add, update, delete, and search operations, resulting in O(n) time complexity. While this approach satisfies the problem requirements, dictionaries would be more efficient for such data storage because they allow direct access using keys with O(1) average time complexity. Lists are suitable for small datasets, but dictionaries are preferable for larger or frequently accessed records.

---

## Module 3 – Q1

**Library System Using Nested Dictionaries**

Nested dictionaries allow hierarchical representation of real-world data by grouping related attributes under a single key. In the library system, each book ID maps to a dictionary containing title, author, and year. This structure improves data organization, readability, and scalability, making it easier to manage and retrieve complex information.

---

## Module 3 – Q2

**Regular Expression Based Data Extraction**

Regular expressions provide a concise and powerful way to match patterns such as email addresses and date formats. Manual string scanning would require multiple conditional checks and complex logic, making the code longer and harder to maintain. Regex simplifies pattern matching, improves accuracy, and handles multiple formats efficiently.

---

## Module 4 – Q1

**Bank Account Class and Encapsulation**

Encapsulation restricts direct access to sensitive data by allowing interaction only through defined methods. By keeping the balance as a protected attribute and providing deposit and withdrawal methods, data integrity is maintained. Encapsulation improves reliability by preventing unauthorized or invalid modifications to object state.

---

## Module 4 – Q2

**Word Frequency Storage Using Shelve**

The `shelve` module provides persistent storage with key-value access, making retrieval faster compared to reading and processing text files repeatedly. Pretty printing improves readability of stored data during debugging and presentation. Shelve is more efficient for repeated access, while plain text storage is better suited for simple or one-time processing.

---

## Module 5 – Q1

**Web Scraping Using Requests and BeautifulSoup**

Common issues during web scraping include malformed HTML, missing tags, and network errors. BeautifulSoup handles imperfect HTML structures gracefully, reducing parsing failures. Missing attributes such as `href` can result in incomplete data extraction and must be handled carefully to avoid runtime errors.

---

## Module 5 – Q2

**Data Analysis Using Pandas and Matplotlib**

Pandas simplifies data manipulation by providing built-in functions for aggregation, filtering, and column-wise operations. Tasks such as computing totals, averages, and grades require significantly less code compared to pure Python lists. Matplotlib integrates easily with Pandas, enabling quick visualization of data, which improves clarity and productivity.

---
