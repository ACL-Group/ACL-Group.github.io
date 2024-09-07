# Reviewer 1

We sincerely appreciate your comments. 

**Q1: Whether the job is suitable for ACL?**

**Ans:** ACL communicates scientific results on computational linguistics and natural language processing. 
Animal languages, or communications between dogs in this paper, are clearly legitimate forms of **natural languages**. 
The study of dog language is clearly linguistics as well. 
Previous work such as "Transcribing vocal communications of domestic shiba lnu dogs." has been accepted by ACL.
We believe our study on animal communications will breathe new life into the ACL community.

**Q2: The staged training approach when clustering.**

**Ans:** Staged training is a method in HuBERT (Hsu et al., 2021) that significantly improves results. More details can be found in the paper "HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units."

**Q3: Some words and their corresponding actions.**

**Ans:** xingyuan: Can we provide some examples?


# Reviewer 2

Thank you for your valuable comments and suggestions.

**Q1: Phonetic and lexical discovery of canine vocalization.**

**Ans:** Exploration of canine vocalization requires first exploring meaningful units in canine vocalization.
The focus of this paper is to discover these possible meaningful units in canine vocalizations. 
So we tried to use similar definitions in human language to describe the phones, words that may be present in canine vocalization. 
This gives a series of candidate meaningful units in canine vocalization.
Then we discover the units with stable meaning through the context information, and finally get the most likely meaningful units in canine language which we call their "words".
At every step of the workflow, we utilized the most effective methodology and confirmed its efficiency.

**Q2: About audio event clustering.**

**Ans:** The difference between our work and Jansen's is that 1. We want to explore meaningful units in canine vocalizations, so we need to get reasonable candidates for sound units, not just a coarse-grained piece of audio. 2. Exploring the meanings that sound units may contain requires labeling the sound units with strongly labeled data, and at the same time, we need to get the causal relationships between them, not just tagging them.

# Reviewer 3

Thank you for your comment and pointed out some problems to help us improve the quality of our work. 
We will explain your concerns point by point.

**Q1: Other factors that may affect barking.**

**Ans:** We do not deny that there are many other factors associated with dog barking, such as smell, mood, or other factors that we don't know about. 
But as we said at the beginning of 3.3, It is very challenging to obtain complete contextual information. 
But we can obtain partial context to explore coarse-grained semantics behind that dog barking sound (Berthet et al., 2023). 
If they have a strong causal relationship, then this contextual information may be part of the semantics.

**Q2: About noise removal.**

**Ans:** In our work, noise removal is mainly in the first two parts of the workflow: **Audio Clean-up by AudioSep** and **Sentence Extraction**. 
We expect to explore the possible phones of canines through HuBERT. HuBERT needs to be trained on noisy data. 
However, it is feasible to exclude the non-barking aspect (noise label) of the HuBERT result (Table 3).

**Q3: The manually labeled data in the semantics discovery method.**

**Ans:** We apologize for not clarifying the details of this section. 
We obtained some video clips of dogs barking and established several activity categories (Table 2). Then manually label the category they belong to. We labeled 2534 video clips with a balanced number of each category.

**Q4: Typos.**

**Ans:** Thank you for pointing out the typos in our paper and providing suggestions for the writing. We will correct the typos when revising the paper.
