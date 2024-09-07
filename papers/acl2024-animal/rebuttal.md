# Rebuttal

## Reviewer 1

Thanks for your careful and valuable comments. 
We are pleased to note that your interest in animal communication and also pointed out some problems to help us improve the quality of our work. 
We will explain your concerns point by point.

**Q1: The definition of "Phoneme"**

**Ans:** We apologize about the confusion with the definition of "Phonemes". 
Given that we have minimum knowledge about the animal vocalization,
in this work, we make the assumption that canine vocalization exhibits similar structures with human language, that each minimal acoustic change unit can be symbolized as a phone.
Additionally, **Hsu et al. (2021)** suggests that acoustic hidden units obtained through HuBERT can be considered as "Phones" 
as the meaningful shortest sound units in human language, and has performed well in human ASR tasks.
We define a "phoneme" (integer in our paper) as symbolic representation of all similar phones, just like in human language. 
We will definitely revise the paper to clarify this and give a definition at the beginning of the paper to avoid confusion.
We will also review the entire paper to be more cautious about using words like "phoneme", "word", and "sentence".

**Q2: What do phonemes map to acoustically?**

**Ans:** A phoneme maps to a set of similar phones.
We also measure the final dog phoneme results by whether humans can distinguish between sound segments belonging to the same or different phonemes.
From the perspective of our definition of dog phonemes,
a 70% accuracy rate is sufficient to demonstrate the quality of our final 
dog phoneme set for word discovery, as defined by our phoneme combinations.

**Q3: The definition of "word"**

**Ans:**
We define a canine word as a frequently occurring sequence of phonemes, not only from one dog, but potentially among many different dogs. 
We hypothesize each canine word indicates a stable pattern and can be used to signify same meanings.
We have validated the prevalence of such canine words in the training data through a coverage analysis in the paper.

Although a 70% coverage rate indicates the prevalence of the words we discovered, 
it does not mean that all these words are actually uttered by dogs (some of them maybe ambient noises) or represent specific meanings.
We can only say that these repeated combinations of phonemes have the potential of being the true words.
In our next work, we will analyze the dog's behavior, state, context, 
and other information when they vocalize these potential "words" to further explore their meanings and verify their plausibility.

**Q4: Typos**

**Ans:** Thank you for pointing out the typos in our paper and providing suggestions for the writing.
We will correct the typos when revising the paper and clarify the definitions of phones,
phonemes, words, and vocabulary, as well as make the logic of the paper more concise and smooth.

Our ultimate goal is to understand the verbal expressions of dogs, the prerequisite of which is audio preprocessing, similar to any other existing spoken language understanding.
While it is our long-term goal to study the syntax and semantics of the dog language, we limit the scope of this paper to the purely lexical analysis of dog communication.  
The focus of this paper is segmenting and exploring the possible dog vocal patterns as minimal acoustic units.
The main objective of this paper is to propose a self-supervised framework for transcribing dog barks into a sequence of symbols.
Our future work will link these symbolic representation of the dog vocals with the dog's behavior, contextual environment, etc. to further analyze their potential significance. 
So this work is a necessary step for conducting semantic analysis.
The proposed data-driven approach has the benefit of good scalability and generalizability to other species.
We also developed a demo system for researchers to get the transcription of dog audio clips,
thereby attracting more attention and involvement in the exploration of animal languages.
Ultimately, this contributes to the possibility of effective information exchange between humans and animals in the future.

## Reviewer 2

Thank you for your detailed and passionate comments. We value every bit of your criticism, 
and we are very excited that our work has attracted the attention of animal communication experts like yourself.

**Q1: The definition of "Phoneme", "Word", "Sentence"**

**Ans:** Although, as you mentioned,
there is a controversy regarding whether animal vocal communication systems are similar to human language, 
and there is also an on-going debate about whether animal communications are a language, nothing is conclusive at this point. 
Nonetheless, our work of identifying the unique acoustic symbols and further transcribing the dog barks into written text is an important first step toward the systematic understanding of dog communications. 
This could open up a brand new chapter in natural language processing research. 
Given that we have minimum knowledge about the animal vocalization,
in this work, we make the assumption that canine vocalization exhibits similar structures with human language, that each minimal acoustic change unit can be symbolized as a phone.
Here a phone is defined as the minimum distinct acoustic unit. 
A phoneme is a symbol that represent a set of most similar phones.
We define a canine word as a frequently occurring sequence of phonemes, not only from one dog, but potentially among many different dogs. 
We hypothesize each canine word indicates a stable pattern and can be used to signify same meanings.
A sentence is a longer sequence of phonemes bounded by at least 100 ms of pauses.
We are hoping that the methods, results, and the demo developed and presented in this paper
take a step towards resolving the grand question of whether animal vocal communication systems resemble that of human.
We will definitely revise the paper to clarify this and give a definition at the beginning of the paper to avoid confusion.
We will also review the entire paper to be more cautious about using words like "phoneme", "word", and "sentence".

**Q2: The evaluation of phonemes didn't follow the biology method**

**Ans:** Our ultimate goal is to understand the verbal expressions of dogs, the prerequisite of which is audio preprocessing, similar to any other existing spoken language understanding.
While it is our long-term goal to study the syntax and semantics of the dog language, we limit the scope of this paper to the purely lexical analysis of dog communication.  
The focus of this paper is segmenting and exploring the possible dog vocal patterns as minimal acoustic units.
The main objective of this paper is to propose a self-supervised framework for transcribing dog barks into a sequence of symbols.
Our future work will link these symbolic representation of the dog vocals with the dog's behavior, contextual environment, etc. to further analyze their potential significance. 
So this work is a necessary step for conducting semantic analysis.
The proposed data-driven approach has the benefit of good scalability and generalizability to other species.
We also developed a demo system for researchers to get the transcription of dog audio clips,
thereby attracting more attention and involvement in the exploration of animal languages.
Ultimately, this contributes to the possibility of effective information exchange between humans and animals in the future.

**Q3: Why don't you follow the basic idea of human transcription?**

**Ans:** If the basic idea of human transcription is phonetic analysis and labelling - we tried, but we found that since there's no established phonetic framework (phonetic symbols, frequency range study, articulatory change etc.) to dog vocalizations, it is even difficult to define what is a minimal acoustic unit and different annotators have low agreement in segmenting the acoustic changes. Hence we propose a self-supervised method to cope with such situation without any annotation protocol as existing in human language.
We use very basic and general method of segmenting the audio data into frames of 50ms length, 
and then use HuBERT, which is the current state-of-the-art self-supervised transformer language model on these audio frames
to transcribe the audio clips into sequences of phonemes. Our approach is the first of such attempts to transcribe
non-human voices using HuBERT. We will cite the following papers which are related earlier attempts of unsupervised human
voice transcription in the revised version.

Hanan Aldarmaki, Asad Ullah, Sreepratha Ram, Nazar Zaki. Unsupervised Automatic Speech Recognition: A review. Speech Communication, Vol. 139, 2022.
Alexei Baevski, Wei-Ning Hsu, Alexis Conneau, Michael Auli. Unsupervised Speech Recognition.

## Reviewer 3

Thank you for your comment and pointed out some problems to help us improve the quality of our work. 
We will explain your concerns point by point.

**Q1: The definition of Phoneme**

**Ans:** We apologize for not clearly elucidating the definitions of phones, phonemes, and words in the paper.
To advance our understanding of potential and total unknown animal languages,
we make the assumption that canine vocalization exhibits similar structures with human language, that each minimal acoustic change unit can be symbolized as a phone.
Additionally, **Hsu et al. (2021)** suggests that acoustic hidden units obtained through HuBERT can be considered "Phones" as the meaningful shortest sound units in human language, 
and has performed well in human ASR tasks.
Therefore, we use the same phoneme(integer in our paper) to represent several similar phones,
akin to human language.
We believe that due to the biological similarity of dogs' vocal organs,
there are bound to be repeated phones produced by dogs that can be summarized as phonemes.

We define a canine word as a frequently occurring sequence of phonemes, not only from one dog, but potentially among many different dogs. 
We hypothesize each canine word indicates a stable pattern and can be used to signify same meanings.
We have validated the prevalence of such canine words in the training data through a coverage analysis in the paper.
We will definitely revise the paper to clarify this and give a definition at the beginning of the paper to avoid confusion.
We will also review the entire paper to be more cautious about using words like "phoneme", "word", and "sentence".

Although a 70% coverage rate indicates the prevalence of the words we discovered, 
it does not mean that all these words are actually uttered by dogs (some of them maybe ambient noises) or represent specific meanings.
We can only say that these repeated combinations of phonemes have the potential of being the true words.
In our next work, we will analyze the dog's behavior, state, context, 
and other information when they vocalize these potential "words" to further explore their meanings and verify their plausibility.


**Q2: This method is too general to the dog vocalizations**

**Ans:** We completely agree with your point.
As in current works, dog barks, as well as mosquito flying sound, are all named as sound events. 
A general audio processing perspective is to generalize a framework that can identify and classify each different sound type.
The pipeline proposed in this paper can also be applied to sounds emitted by lawnmowers.
In fact, our initial intention was to design a universal pipeline that could be applied to all animals capable of vocalization.
The goal is to explore whether animal vocal communication systems can be identified through data-driven methods to uncover their underlying patterns.
These patterns form the basis for linking information about behavior, environment, etc. during vocalization and analyzing meaning.

Our ultimate goal is to understand the verbal expressions of dogs, the prerequisite of which is audio preprocessing, similar to any other existing spoken language understanding.
While it is our long-term goal to study the syntax and semantics of the dog language, we limit the scope of this paper to the purely lexical analysis of dog communication.  
The focus of this paper is segmenting and exploring the possible dog vocal patterns as minimal acoustic units.
The main objective of this paper is to propose a self-supervised framework for transcribing dog barks into a sequence of symbols.
Our future work will link these symbolic representation of the dog vocals with the dog's behavior, contextual environment, etc. to further analyze their potential significance. 
So this work is a necessary step for conducting semantic analysis.
The proposed data-driven approach has the benefit of good scalability and generalizability to other species.
We also developed a demo system for researchers to get the transcription of dog audio clips,
thereby attracting more attention and involvement in the exploration of animal languages.
Ultimately, this contributes to the possibility of effective information exchange between humans and animals in the future.


