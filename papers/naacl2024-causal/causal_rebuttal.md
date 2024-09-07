# Causal Rebuttal

## Reviewer HEPR

**Q1: Details about Life Events Dataset**

**Ans:** We adopted an annotation procedure similar to that of previous work [1], which annotated a symptom dataset. Our life event dataset contains 2634 posts related to one or more life events, alongside 5000 control posts (i.e., posts unrelated to any life event). We engaged three experienced annotator for the task, and their inner agreement (Fleiss' Kappa) is as follows.

|                                         | Kappa |
|-----------------------------------------|-------|
| Loss and Bereavement                    | 0.91  |
| Marriage and Commitment                 | 0.91  |
| Relationship Conflicts and Breakdown    | 0.89  |
| Family Additions and Departures         | 0.37  |
| Health and Well-being                   | 0.91  |
| Work and Career Challenges              | 0.98  |
| Financial Challenges                    | 0.89  |
| Education Transitions                   | 0.92  |
| Change in Living Environment and Habits | 0.82  |
| Vacations and Holidays                  | 0.92  |
| Legal Matters                           | 0.93  |
| **Average**                             | 0.86  |

[1] Zhang et al. "Symptom Identification for Interpretable Detection of Multiple Mental Disorders on Social Media" EMNLP(2022)

The dataset will be publicly available.

**Q2: Why is there a big discrepancy between the F1 scores and the AUC scores? Is this performance expected based on prior work? Do we need better classifiers for this task or is the current performance enough to conduct follow-up experiments (downstream tasks)**

**Ans:** The key distinction between F1 and AUC stems from their sensitivity to the threshold. AUC is threshold-independent, whereas F1 is greatly affected by it. Tuning the threshold can enhance F1 scores.  

For the application on downstream tasks, the primary metric to consider should be AUC, because downstream tasks utilize continuous symptom probabilities rather than binary outcomes.  The classifier already boasts a high AUC, making it suitable for downstream tasks. 

**Q3: How often do these causal relationships are in agreement vs. not? What are some examples of when the causal relationships are not in agreement? Error analysis is necessary.**

**Ans:** Thank you for your insightful comment. We agree with you that the disagreements are also very important. Thus, we add a literature review to check the discovered causal relationship. Below is a table summarizing the **top-8** causal relationships with the highest ATE scores:


| **Causal Relationships**                                                         | **Supported/Disagreed** | **References** | **ATE** |
|----------------------------------------------------------------------------------|-------------------------|----------------|---------|
| fears_of_being_negatively_evaluated -> somatic_symptoms_sensory                  | Disagreed               | [1]            | 0.887   |
| fears_of_being_negatively_evaluated -> Depressed_Mood                            | Supported               | [2][3]         | 0.886   |
| fears_of_being_negatively_evaluated -> Suicidal_ideas                            | Supported               | [4]            | 0.874   |
| Hyperactivity_agitation -> Impulsivity                                           | Disagreed               | [5]            | 0.869   |
| fears_of_being_negatively_evaluated -> do_things_easily_get_painful_consequences | Supported               | [6][7]         | 0.857   |
| panic_fear -> somatic_symptoms_sensory                                           | Mixed                   | [8][9]         | 0.855   |
| fears_of_being_negatively_evaluated -> Autonomic_symptoms                        | Supported               | [10][11]       | 0.855   |
| panic_fear -> Decreased_energy_tiredness_fatigue                                 | Supported               | [12]           | 0.845   |

Among these, **five** relationships are supported by existing literature. **Two** Two relationships show disagreement to some extent, proposing alternative associations. 
An example is Seinsche et al.'s (2023) finding suggesting a connection between social anxiety and a clearer memory about distasteful social situations, which is contradict to our causal link between fear of being negatively evaluated and poor memory. Moreover, **one** finding got mixed results, depending on studies and samples. 

Overall, the existing literature provides limited evidence due to a lack of direct causal examinations between pairs of symptoms. Our current findings have the promise of inspiring future studies focusing on direct causal relationship examinations on pairs of symptoms.

[1] Kim, J. H. J. et al. (2019). Cultural variation in temporal associations among somatic complaints, anxiety, and depressive symptoms in adolescence. Journal of Psychosomatic Research, 124, 109763-109763.

[2] Jacobson, N. C. et al. (2017). Anxiety and depression as bidirectional risk factors for one another: A meta-analysis of longitudinal studies. Psychological Bulletin, 143(11), 1155-1200.

[3] Kim, J. H. J. et al. (2019). Cultural variation in temporal associations among somatic complaints, anxiety, and depressive symptoms in adolescence. Journal of Psychosomatic Research, 124, 109763-109763.

[4] Klumpp, H. et al. (2023). Objective and subjective sleep measures are related to suicidal ideation and are transdiagnostic features of major depressive disorder and social anxiety disorder. Brain Sciences, 13(2), 288.

[5] Grandjean, A. et al. (2021). Stronger impulse capture and impaired inhibition of prepotent action in children with ADHD performing a simon task: An electromyographic study. Neuropsychology, 35(4), 399-410. 

[6] Moscovitch, D. A. et al. (2018). Autobiographical memory retrieval and appraisal in social anxiety disorder. Behaviour Research and Therapy, 107, 106-116. 

[7] Chu, C. et al. (2016). Thwarted Belongingness Mediates the Relationship Between Fear of Negative Evaluation and Suicidal Ideation. Cognitive Therapy and Research, 40(1), 31–37. 

[8] Ehlers, A. (1993). Interoception and panic disorder. Advances in Behaviour Research and Therapy, 15(1), 3–21.

[9] Kang, S. J. et al. (2024). A pontomesencephalic PACAPergic pathway underlying panic-like behavioral and somatic symptoms in mice.Nature Neuroscience, 27(1), 90-101.

[10] Alvares, G. A. et al. (2013). Reduced Heart Rate Variability in Social Anxiety Disorder: Associations with Gender and Symptom Severity. PLOS ONE, 8(7), e70468.

[11] Weeks, J. W. et al. (2016). Fears of Positive versus Negative Evaluation: Distinct and Conjoint Neuroendocrine, Emotional, and Cardiovascular Responses to Social Threat. Journal of Experimental Psychopathology, 7(4), 632–654.

[12] Pasquini, M. et al. (2015). Fatigue experiences among OCD outpatients. Psychiatric Quarterly, 86(4), 615-624.

**Q4: Can ERD task and DPD task be reframed so that they're not presented with equal weight？**

**Ans:** We agree that the ERD task, in comparison to the DPD task, is more established and provides richer information. We will reframe the tasks accordingly.

## Reviewer w8Tp

**Q1: The concern about whether this paper is a great fit for \*ACL**

**Ans:** We believe this paper is suitable for \*ACL and NLP community for two reasons. 

1. The \*ACL community has shown interest in causality-related research. For example, in 2022, TACL published a noteworthy survey paper[1] emphasizing the potential synergy between causality and NLP, particularly in two areas: (1) Estimating causal effects from text, where our work closely aligns, and (2) using causal formalisms to enhance NLP methods. Additionally, our downstream tasks involve analyzing social media text, further establishing the relevance of our work for \*ACL.

2. Previous efforts within the NLP community have delved into causal relationships using syntactic analysis[2]. However, these endeavors often focus on short-term causal relationships within a single sentence, presenting certain limitations. We believe our work has the potential to inspire the NLP community to explore methodologies for unveiling more long-term and latent causal relationships.

[1] Feder et al. "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond." TACL(2022)

[2] Garg et al. "CAMS: an annotated corpus for causal analysis of mental health issues in social media posts." LREC(2022)

**Q2: The concerns about the quality of the Propensity Score Matching. 1) The choice of covariates to perform the matching could be better motivated; 2) The quality of the matching itself was not analyzed/validated in any way.**

**Ans:** 1) We incorporate the remaining 36 symptoms as covariates when assessing causal relationships between two specific symptoms. The motivation is straightforward: individuals may experience a range of symptoms, and these symptoms can mutually influence each other. With these covariates, we ensure that matched treatment and control pairs demonstrate high similarity in the other 36 symptoms, thereby boosting the reliability of causal computations.

2）To ensure the quality of our matching, we analyzed the distribution of propensity scores between the treatment and control groups. Our findings reveal a significant overlap in propensity scores between these two groups, indicating that our matched pairs share great similarity in covariates. 

**Q3: It is unclear how many of the discovered causal relationships were not supported by literature, and/or how many of the found relationships were actually disputed in literature. Could you do a more systematic analysis?** 

**Ans:** Thank you for your insightful comment. We add a literature review to check the discovered causal relationship. Below is a table summarizing the **top-8** causal relationships with the highest ATE scores:

| **Causal Relationships**                                                         | **Supported/Disagreed** | **References** | **ATE** |
|----------------------------------------------------------------------------------|-------------------------|----------------|---------|
| fears_of_being_negatively_evaluated -> somatic_symptoms_sensory                  | Disagreed               | [1]            | 0.887   |
| fears_of_being_negatively_evaluated -> Depressed_Mood                            | Supported               | [2][3]         | 0.886   |
| fears_of_being_negatively_evaluated -> Suicidal_ideas                            | Supported               | [4]            | 0.874   |
| Hyperactivity_agitation -> Impulsivity                                           | Disagreed               | [5]            | 0.869   |
| fears_of_being_negatively_evaluated -> do_things_easily_get_painful_consequences | Supported               | [6][7]         | 0.857   |
| panic_fear -> somatic_symptoms_sensory                                           | Mixed                   | [8][9]         | 0.855   |
| fears_of_being_negatively_evaluated -> Autonomic_symptoms                        | Supported               | [10][11]       | 0.855   |
| panic_fear -> Decreased_energy_tiredness_fatigue                                 | Supported               | [12]           | 0.845   |

Among these, **five** relationships are supported by existing literature. **Two** Two relationships show disagreement to some extent, proposing alternative associations. 
An example is Seinsche et al.'s (2023) finding suggesting a connection between social anxiety and a clearer memory about distasteful social situations, which is contradict to our causal link between fear of being negatively evaluated and poor memory. Moreover, **one** finding got mixed results, depending on studies and samples. 

Overall, the existing literature provides limited evidence due to a lack of direct causal examinations between pairs of symptoms. Our current findings have the promise of inspiring future studies focusing on direct causal relationship examinations on pairs of symptoms.

[1] Kim, J. H. J. et al. (2019). Cultural variation in temporal associations among somatic complaints, anxiety, and depressive symptoms in adolescence. Journal of Psychosomatic Research, 124, 109763-109763.

[2] Jacobson, N. C. et al. (2017). Anxiety and depression as bidirectional risk factors for one another: A meta-analysis of longitudinal studies. Psychological Bulletin, 143(11), 1155-1200.

[3] Kim, J. H. J. et al. (2019). Cultural variation in temporal associations among somatic complaints, anxiety, and depressive symptoms in adolescence. Journal of Psychosomatic Research, 124, 109763-109763.

[4] Klumpp, H. et al. (2023). Objective and subjective sleep measures are related to suicidal ideation and are transdiagnostic features of major depressive disorder and social anxiety disorder. Brain Sciences, 13(2), 288.

[5] Grandjean, A. et al. (2021). Stronger impulse capture and impaired inhibition of prepotent action in children with ADHD performing a simon task: An electromyographic study. Neuropsychology, 35(4), 399-410. 

[6] Moscovitch, D. A. et al. (2018). Autobiographical memory retrieval and appraisal in social anxiety disorder. Behaviour Research and Therapy, 107, 106-116. 

[7] Chu, C. et al. (2016). Thwarted Belongingness Mediates the Relationship Between Fear of Negative Evaluation and Suicidal Ideation. Cognitive Therapy and Research, 40(1), 31–37. 

[8] Ehlers, A. (1993). Interoception and panic disorder. Advances in Behaviour Research and Therapy, 15(1), 3–21.

[9] Kang, S. J. et al. (2024). A pontomesencephalic PACAPergic pathway underlying panic-like behavioral and somatic symptoms in mice.Nature Neuroscience, 27(1), 90-101.

[10] Alvares, G. A. et al. (2013). Reduced Heart Rate Variability in Social Anxiety Disorder: Associations with Gender and Symptom Severity. PLOS ONE, 8(7), e70468.

[11] Weeks, J. W. et al. (2016). Fears of Positive versus Negative Evaluation: Distinct and Conjoint Neuroendocrine, Emotional, and Cardiovascular Responses to Social Threat. Journal of Experimental Psychopathology, 7(4), 632–654.

[12] Pasquini, M. et al. (2015). Fatigue experiences among OCD outpatients. Psychiatric Quarterly, 86(4), 615-624.


**Q4: Evaluation metric of DPD**

**Ans:** According to the survey[1], the commonly used evaluation metrics of change point detection includes F1 score, annotation error, rand index, etc. In our F1 score calculation, we designate true positive (TP) samples as those falling within a specific temporal proximity to the actual diagnosis time. This adjustment acknowledges the challenge of predicting the exact diagnosis day in real-world scenarios and aligns with the methodology in [1], where true positives account for a "user-defined margin of error (M > 0)." 

When both a positive and negative prediction occur in the time window, our focus is solely on the positive prediction, because this task only cares about the change point(i.e., positive prediction).

[1] Truong et al. "Selective review of oﬄine change point detection methods." Signal Processing(2020)


**Q5: Questions about 4.2 experiments**

**Ans:** Thank you for bringing up this point. Currently, our work centers around symptoms. The life-event-to-symptom causality is one way to complete the symptom sequence, so we only use symptom features as baseline. We will take your suggestions into account for future investigations.

## Reviewer mzTh 
**Q1: For both tasks, the authors only used one baseline as a comparison.**

**Ans:** Our baseline experiments aim to showcase the advantages of integrating causal relationships into downstream tasks. The baseline model is tailored to process symptom signals as input. It's worth noting that our objective is not to pursue SOTA performance; rather, the baseline serves as a kind of ablation to validate effectiveness. While more complex models could handle the symptom signal, such complexity is considered non-essential for achieving our goal.


**Q2: Statistical significance results**

**Ans:** Thank you for raising this point. We conducted three sets of experiments using different seeds. Due to space constraints, we present a subset of the results (formatted as "mean (standard deviation)") below.

| Method   | Causal Window | ERDE5         | ERDE50       |
|----------|---------------|---------------|--------------|
| baseline | -             | 13.663(0.012) | 6.84(0.018)  |
| +symp    | 30            | 13.523(0.010) | 6.057(0.010) |
| +symp    | 90            | 13.313(0.028) | 6.18(0.048)  |

We also calculated the p-values indicating the significance of the differences between the baseline and our method, as shown in the table below. Most p-values are smaller than 0.05, indicating statistical significance.

| Method                 | p-value (ERDE5) | p-value (ERDE50) |
|------------------------|-----------------|------------------|
| baseline vs. +symp(30) | 0.183           | 0.041            |
| baseline vs. +symp(90) | 0.018           | 0.012            |


**Q3: For the task of Diagnosis Point Detection, the authors mentioned that the dataset includes when the user was diagnosed with depression and used it as a label. I assume that you remove these for the test part, but it's not specifically mentioned in the paper.**

**Ans:** Yes, we removed these for the test part.

**Q4: the average number of days of post history**

**Ans:** In our dataset, the average posting history spans **1359 days**, providing sufficient coverage for window sizes ranging from 30 to 180 days. 

**Q5: Has RuLSIF been used in other text-related tasks? If not, it could be something interesting to discuss.**

**Ans:** RuLSIF is widely applied in time series data. In our application, where the input is comprised of social media posts arranged in a time series, the use of RuLSIF is natural. Nevertheless, to the best of our knowledge, we are not aware of other text-related tasks that utilize RuLSIF.

**Q6: When the model uses both LE and symp features together the model loses performance, any thoughts on why this happens?**

**Ans:** After conducting error analysis, we discovered that incorporating symp&LE features into the model results in an increase in false positive samples. This can be traced back to the introduction of LE, which raises the likelihood of additional symptoms. Thus, we plan to  explore more thoughtful approaches to combine symp&LE  relationships in our future work.  

**The additional information you shared with us about the dataset and its annotation, the discovered causal relationships, and the statistical analysis of the results, can strongly strengthen the paper, highlighting its relevance and the pertinence of the experimental methodology.
My question now is how do you plan to include all this information in the paper, with what level of detail, in what sections, etc.**

**Ans:** Thank you for your reply. We appreciate your feedback and believe that incorporating the suggested analyses and experiments will enhance the quality of our paper without changing its core focus. Below is our plan for revising the paper:
1. **Life Events Dataset and Annotation:** We will describe the annotation procedures and present the agreement results among annotators in the appendix. Additionally, a brief overview of the basic characteristics of the dataset, such as size and distribution, will be provided in the main body (Section 2.1).
2. **Discovered Causal Relationships and Systematic Literature Review:** We will expand Table 1 in the paper to encompass a systematic analysis of the top-10 causal relationships. Further analysis will be provided in Section 3.1.
3. **Statistical Analysis of Results:** The results of our statistical analysis will be integrated into the existing experimental charts. We will provide some explanations about the statistical results in Section 4.1 and 4.2. 
4. Some minor points previously in the main body may be moved to the appendix.
