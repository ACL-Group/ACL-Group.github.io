# response

We sincerely appreciate the reviewers' valuable suggestions, which have helped us identify flaws and areas for improvement in our previously submitted paper. After carefully considering the reviewers' advice, we have made the following advancements:

## update 1: Clear definition on canine "sentence", "word" and "phone"

To discover communication pattern within canine vocalization, we refer to the definition of human language and apply it to dogs.

- "sentence": A continuous sequences of dogs barks with no more than 0.5 seconds silence in between.
- "word": The smallest sequence of 205 phones that consistently appears in one or more 206 specific situations.
- "phone": The fundamental sound components within canine vocalizations.

## update 2: Improvement on word discovery method

While preserving the sentence-word-phone structure, we use Adaptor Grammar based method to train and parse canine sentences. This model can learn the relationship between recurrent phone sequence segments and the nonterminal Word, resulting in a more reliable candidate vocabulary.

## update 3: Word semantics analysis

To measure the authenticity of discovered canine words and create a potential vocabulary of canine language, we analyze their frequency and distribution in different contexts, and validate their effectiveness by comparing changes in the original video.