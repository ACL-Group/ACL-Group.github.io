
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
Introduction
---------------
This project is targeted to represent verb meanings (actions) as noun concepts. For example, you can represent `company buy company` as `acquisition` , `country invade country` as `war` and so on. The approach of generating verb meanings (actions) is published by our previous work (named "Represent Verbs as Argument Concepts") on AAAI 2016. And you can find the code at https://github.com/pangolulu/Action.

Taxonomy
--------------
We use a taxonomy as the external classification knowledge for generating the noun concepts for verbs. A taxonomy is a directed graph `(V, E)`. Here, `V` is a set of terms, `E` is a set of binary `isA` relations: `E={(e,c)| e in V, c in V, e isA c}` where `e` is called an `entity`, `c` is called a `concept`, and `c` is said to cover `e`. Most terms in `V` are both concepts and entities; terms with zero outdegree in the graph are entities only. In this paper, we consider two different taxonomies, namely WordNet and Probase. WordNet organizes words into sets of synonyms (called synsets) along with `isA` relation between two synsets. Each word may belong to multiple synsets and have multiple hypernyms (concepts) or hyponyms (entities). Probase covers a lot of named entities and multi-word expressions (e.g., Microsoft, Star Wars) which may not be covered by WordNet. This feature allows us to extract more precise arguments.

Approach
--------------
#### Baseline Method
1. Use a WSD tool to get the verbs meaning as a synset id in WordNet.
2. Transfer the verbs in that synset to their noun forms by a dictionary, such as `acquire` to `acquisition`.
3. Rank the noun words (todo).

#### Retrieval Method
1. Prepare the corpus (news).
2. Retrieve the verb triples (subject, verb, object) related to the titles from the corpus.
3. Retrieve the noun concepts from all the titles filtered by a knowledge base, such as Probase or WordNet.
4. Relate the verb triples and noun concepts, and form a bipartite graph, as `G(T, C)`.
5. For a give verb meanning (action) such as `company buy company`, find all its verb triple instances appearing in the retrieved verb triples (`T`) such as `google buy moto` based on a knowledge base.
6. Regard the verb triples as key words and noun concepts as documents in the area of Infromation Retrieval.
7. Use some Infromation Retrieval techniques, such as TF-IDF or BM25 to rank the noun concepts.