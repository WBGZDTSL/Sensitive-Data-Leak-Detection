# **sensitive data leak detection**

### 2022.08.25
1. Accomplish word extraction: we can use the split method to extract each field from the address by setting a fixed delimiter
2. Pytextrank: I find a python library named pytextrank that can rank the frequency of occurrence of keywords in a piece of text. Here is the link to [Pytextrank](https://derwen.ai/docs/ptr/sample/)

### 2022.08.26
1. Project motivation: Whether there are keywords in the path and the identity of the visitor can be retrieved to determine the download authority of the visitor
2. Worked done: We remove all symbols that exist in the file address and keywords, and then use the keywords to search the addresses in turn. If it exists, it will return '1', if it does not exist, it will return '0', and finally return a list of eigenvalues. We add a column of labels to the data. If there is a keyword in the feature value of each row, that is, there is a '1', we will add the '1' variable to the label column, otherwise it will return the '0' variable.
3. Direction: tokenization(yake, rake)

### 2022.08.29
1. Suffix Check: Given all file name suffixes, and then determine whether the file suffix extracted from the file directory is in the given file name suffix
2. EN keywords recognition: Precise search in Chinese; fuzzy search in English

### 2022.08.30

1. Modularity of code: Each function of the code forms a separate module
2. Database Connection： data input and output, version control
3. Tense: Can recognize different tenses of words