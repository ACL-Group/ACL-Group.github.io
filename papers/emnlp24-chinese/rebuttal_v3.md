# Reviewer nTDy
## Briefly explain our model
* First, let us briefly explain our model to clarify a possible misunderstanding. Our model can be seen as *six* transformers concatenated horizontally, with some connections between them (as shown in Fig. 5a). Each transformer is responsible for one feature extracted from a Chinese character. For example, the initial part for Chinese character "皙" in Fig. 5b is :("[IPA]","s","s","s","[UNK]","[UNK]","ɕ"), showing its evolution over 6 different dynasties. The boundaries of these transformers are marked by the segment embedding in Fig 5b. The input sequence to these transformers is not a sequence of IPA symbols (or tokens in your terms), but a sequence of features chronologically ordered by historical time periods in China (six time periods in this paper), which represents the evolution of pronunciation of a character over time.

## weakness
* W1: The paper currently does not mention the tokenization process utilized for their encoder architecture. How does the tokenizer (sentence-piece or BPE etc) affect the learning process of phoneme sequences? I could be missing something, but could the authors point out where tokenization (and its impact) was discussed?
* About "tokenization process"
    * A: Our "tokenization process" is completed during our feature extraction process. As shown in Fig. 6 and lines 244-262, we segment a Chinese character into several structures and components, and similarly, we divide a phoneme into four parts based on its structure, as shown in Fig. 4 and lines 210-229. These segmented units are the smallest units processed by our model.
    
* W2: How was the initial embedding layer initialized?
* About embedding initialization
    * A: We used the embedding initialization strategy from the BERT model. The weights of the nn.Embedding layer were initialized using a Gaussian distribution with a mean of 0 and a standard deviation of 0.02. The bias of the BertLayerNorm layer was initialized to 0, and the weights to 1. Four different embeddings were initialized using nn.Embedding, with each embedding having its own weight parameters, combined by element-wise addition, passed through layer normalization, and then dropout was applied to the normalized embeddings.
    
* W3: In general, I think the paper could benefit from more experiments with stronger baselines (some variant of LSTMs) for capturing short-context temporal information.
* About LSTMs
    * A: Yes it is a natural solution to use LSTM as baseline for such a temporal prediction task. In fact, we tried LSTMs with only temporal and phonetic information in the earlier phase of the work, but they performed worse than the transformer. We believe that those variants designed for ASR [1] did not perform as expected here because our input sequences are much shorter than ASR: each set of prediction (glyph, temporal, initial, medial, nucleus, coda) has a maximum length of 15. However, we will include these results in the final version. 
    
     [1] A. Zeyer, P. Bahar, K. Irie, R. Schlüter and H. Ney, "A Comparison of Transformer and LSTM Encoder Decoder Models for ASR," 2019 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU), Singapore, 2019, pp. 8-15, doi: 10.1109/ASRU46091.2019.9004025.

## comments
* C1: As shown in Fig. 5, the encoder takes in entries following a specific linear order (glyph-> temporal—> initial). On what basis or intuition was this order chosen? Did the authors try reverting or permuting the order since even though self-attention per se is permutation-invariant, the addition of positional information (segments and linear positional encoding) could likely have an impact in how the model learns as well as the results obtained?
* About encoder order
    * We divided the whole architecture into two parts and present them in Figs 5 and 9, which may have caused some confusion. We will merge these two figs into one in the final version, showing the complete order as (glyph -> temporal -> initial -> medial -> nucleus -> coda). 

* C2: Considering the smaller context lengths for each entry, I am curious why how would an LSTM based encoder perform in this setting? Previous work like [2] suggests that LSTMs are at times comparable to transformers for encoding temporal information especially for speech-based tasks like ASR. Did the authors conduct any experiments with LSTMs for predicting the target phonemes? 
* About LSTM
    * Same as W3.

* C3: Also, established libraries such as Panphon[3] could provide crucial vector-based features for IPA segments instead of the orthographic form. Did the authors consider such feature types as additional context (for IPA segments)? Although not necessary, I think that could well be an interesting direction to explore.
* About vector-based features
    * Thank you for your insightful suggestion. We are aware of the potential benefits of using vector-based features of IPA segments. We will certainly consider this in our future research.




# Reviewer Y5Mv
## weakness
* W1: Since the authors mentioned in Figure 1 that similar characters can have different pronunciations because characters do not indicate sound, why did the authors use glyph information in the model? The motivation for using glyphs is unclear.
* About motivation for using glyphs
    * While most Chinese characters are not directly associated with sound or syllable, many characters sharing a common component have identical or similar sound: For example, "妗", "衿", and "砛" all have the same pronunciation [ʨin]; "侌", "吟", and "訡" have same pronunciation [jin]; "岑" and "笒" share the same pronunciation [ʦən]. This phenomenon motivates the glyph information embedding. We will clarify this point in the paper.

* W2: The authors used temporal information in their model; however, the model cannot learn the pronunciation changes of characters over dynasties. They used their model to predict pronunciation in AD 2300, a period for which the reason for selection is unclear. As there is no ground truth for pronunciation in 2300, I would like to see if their model is trained on the Middle Tang, Late Tang, and Song datasets to predict Yuan and MingQing pronunciation for which there is ground truth. If their model has a high f1-score in predicting the pronunciation of characters in the Yuan and Ming dynasties, the model might solve the problem of the lack of a dataset in the three periods.
* About the capabilities of our model
    * Our model can be seen as *six* transformers concatenated horizontally, with some connections between them (as shown in Fig. 5a). Each transformer is responsible for one feature extracted from a Chinese character. For example, the initial part for Chinese character "皙" in Fig. 5b is :("[IPA]","s","s","s","[UNK]","[UNK]","ɕ"), showing its evolution over 6 different dynasties.
    * As shown in lines 461-469 and Table 6, even when modern data is completely missing from the training set, our model still achieves an F1 score of 0.38 on the modern test set. This is similar to the scenario you described.

## comments
* C1: The example of glyph can not show which types of Chinese characters (simplified or traditional ones) are used in this work. I guess the authors used traditional Chinese characters, but it might be better if the information can be found in this paper.
* About types of Chinese characters
    * We use the traditional Chinese character set and will clarify this in the next version.

* C2: In Table 4, the f1 scores of CT and GTeT look close. Time factors are useless for CT, as the authors mentioned in line 359. Does this mean that chronological labels do not help their model either? Which significance test has been used in the result analysis?
* About chronological labels
    * As shown in Fig. 5a and lines 312-317, We use special markers [CHAR], [YEAR], and [IPA] to integrate chronological information with phonetic changes. The close F1 scores can be attributed to task simplicity in Random Split Evaluation, where characters with different glyphs but identical pronunciations might appear in training and test sets.  We used a paired t-test for significance in Table 4, with p-values {0.081, 0.048, 0.037, 0.026, 0.028, 0.041}, mostly meeting the 5% significance level. Slightly higher p-values can be attributed to the small number of total tests conducted.

* C3: There are several reconstruction systems. I wonder why the authors use Li's system.
    * We chose Li's system to capture temporal changes, as it provides reconstruction results at 9 different representative time points. Other systems, such as those for the Song or Yuan dynasties \[1][2], are limited to specific periods. Additionally, for the 6 specific historical periods we focus on, reconstructions based on Guangyun records show minimal differences among linguists (lines 128-155), making Li's system a representative choice.


[1] Xinkui Li. 1988. 宋代汉语韵母系统研究\[A Study of Chinese Rhyme System in Song Dynasty]. 语言研究\[Studies in Language and Linguistics], (1):15.

[2] Baxter, W. H. (2014). *Old Chinese: A New Reconstruction*. OUP USA.

## Reviewer FA7n

* We chose not to model tones in this work because tone information is missing from the dataset and most reconstruction work in the past.

