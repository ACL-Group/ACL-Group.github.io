# Chatbot Rebuttal

## Reviewer nqvA

**1. Questions about CPT baseline**

**Ans:** The baseline in our paper, denoted as CPT, originates from [1]. This model is pretrained and then fine-tuned on a depression diagnosis dialogue dataset. We label this baseline after the pretrained model named CPT (Chinese Pre-trained Un-balance Transformer). CPT stands as one of the most competitive models for generating Chinese text, boasting better performance in various tasks compared to BART [2]. Thus, it serves as a strong baseline for doctor chatbots, and is quite different from our proposed LLM-empowered chatbot.

[1] Yao et al. "D4: a Chinese Dialogue Dataset for Depression-Diagnosis-Oriented Chat." EMNLP (2022)

[2] Shao et al. "CPT: A Pre-Trained Unbalanced Transformer for Both Chinese Language Understanding and Generation." ArXiv, abs/2109.05729.(2021)

**2. The missing "related works" issue**

**Ans:** The related works section is in Appendix H due to the space limitation.

It's true that there have been multiple efforts to build chatbots for mental health therapy (e.g., woebot, wysa), as well as many works about empathetic response generation in mental health counselling, but very few works about chatbots diagnosing mental disorders, and the empathy in diagnosis. Though there exists some chatbots for diagnosis purpose, most of them focus on physical illness.

Moreover, we can notice the increasing attention to virtual patients, but there are still limited works. A substantial portion of existing virtual patients operate on rule-based systems or can merely provide binary responses like 'yes' or 'no' when queried about symptoms.

**3. Answers for Questions**

**Q1:** Thank you for this advice. We will add more examples to the paper, and there has been some in Appendix F (case study) and Appendix G (error analysis). Here, we'd like to provide examples of "human-like" and "robot-like" utterances:
- Robot-like Examples:
	- Original text: 即使我没有做很多*劳动*，也会感到很*疲劳*，而且感觉自己反应变慢，难以集中注意力。
	- Translation: Despite not engaging in extensive *physical labor*, I find myself experiencing notable *fatigue*. Furthermore, I perceive a deceleration in my cognitive processing speed and struggle to sustain focused attention.
	- Original text: 我感觉自己的情况越来越严重了，有时候甚至会想到*自杀和自伤*的想法和行为。
	- Translation: I perceive that my condition is progressively worsening; at times, I even entertain thoughts and engage in behaviors related to *self-harm and suicide*.

Here the words in *italic* are considered robot-like. For example, `fatigue` will usually be described as `tired`, and `self-harm` is commonly described with `want to die`

- Human-like Examples:
	- Original text: 我就会突然感到很*难受*，情绪就像是一下子就控制不住了，有时候会哭，有时候发脾气，但我也不知道为什么会这样。
	- Translation: I just start feeling really *uncomfortable* out of nowhere, my emotions seem to spiral out of control all of a sudden. Sometimes I cry, sometimes I get angry, but I don't even know why it happens.
	- Original text: 我不知道，可能是觉得自己很*没用*，对家人和朋友都是负担吧。不如离开这个世界。
	- Translation: I don't know, maybe it's because I feel really *worthless*, like I'm a burden to my family and friends. It's better to just leave this world.

**Q2:** Thank you for pointing this out. We will remove the mentioned sentence from the introduction. Our intention was to convey that in scenarios involving large-scale screenings where relying solely on human doctors for diagnosis is impractical and time-consuming, chatbots could potentially fill a role. It's important to clarify that while chatbots can assist in screening, the definitive medical diagnosis can only be provided by qualified professionals.
	
**Q3:** We provided the number of participants in the paper (Sec 4.3). 
- For the evaluation of *doctor chatbots*, we involved 14 depressed patients. This means each doctor chatbot (D1, D2, D3, CPT) underwent evaluation by 14 patients. This resulted in a total of 56 transcripts (simulated doctor with actual patient).
- In the evaluation of *patient chatbots*, we invited 9 psychiatrists and assessed 2 prompt design (P1, P2). As depressed patients have different symptoms, we designed 7 distinct symptom lists to create simulated patients. Consequently, each of these 7\*2=14 patient bots was evaluated by 3 different psychiatrists, yielding 14\*3=42 transcripts (actual doctor with simulated patient).

## Reviewer ypfw
**Reasons To Reject:**

1. Can you elaborate more on why talk to psychiatrists only when identifying psychiatrists key objectives? I think patients' opinions are also important.

	**Ans:** Actually, we have engaged in conversations with individuals who have experienced depression, as one of our team members had personal experience with depression. Their insights were instrumental during the design and iterative processes of developing the doctor chatbot, but our discussions were limited to a small sample. What's more, we find that most patients' opinions are covered by the psychiatrists' opinions, so they were not explicitly pointed out in the paper.

	Additionally, psychiatrists undergo extensive training on how to be good doctors, making them well-qualified to establish standards for doctor chatbots. Therefore, we think consulting with medical experts at this stage provides a solid foundation for setting appropriate goals for this work.

2. The automatic evaluation was done using ChatGPT. I don't think this way of using ChatGPT to evaluate ChatGPT is a big problem, but it is vital to discuss the limitations and hit on how reliable it is.

	**Ans:** Thank you for your suggestion, We'll address ChatGPT's reliability for annotation in the limitations section.

	In this work, we used ChatGPT to make initial annotations just for efficiency. We then took the extra step of having 3 human annotators review and refine the labels assigned by ChatGPT. This meticulous process ensured the credibility of the automatic metrics presented in our paper. Further, for larger-scale data annotation needs, the labeled dataset produced in this study can serve as a foundation for training classification models, offering a potential solution.
## Reviewer 7VPs

**Q1:** The ground truth of "diagnosis accuracy" is not automatically labeled. Instead, it comes from each patient self-reported score on the Beck Depression Inventory (BDI-II)[1], a highly reputable and widely employed tool for measuring the severity of depression. This metric is classified as an automatic metric just because we can automatically compare the model's prediction against these human labels in evaluation.

What's more, we did think about having real doctors provide initial diagnoses for each patient, but this approach can cause some ethical problems. Additionally, we believe diagnostic accuracy is closely tied to the methodology used for assessment. If real doctors were to diagnose solely based on the limited chatbot-patient conversation history, it could lead to potential misdiagnoses and thus affect the reliability of the ground truth.

[1] Beck, A. T., Steer, R. A., & Brown, G. (1996). Beck Depression Inventory–II (BDI-II)

**Q2:** We really appreciate your thoughtful consideration of the evaluation process described in the paper. In this paper, the evaluation of doctor chatbot comes from both the patients' and psychiatrists' viewpoints. First, depressed patients assess the doctor chatbot primarily based on the "user experience" standpoint, where they have the best to say. Second, we also employ metrics such as "symptom recall" and "in-depth ratio" to measure how well the chatbot aligns with the objectives (Section 2), which is proposed with psychiatrists.

Furthermore, we think the suggestion to involve human doctors in evaluating the dialogue between doctor chatbot and patients is valuable. We will incorporate this in the future work.

**Q3:** CPT[1] (Chinese Pre-trained Un-balance Transformer) is one of the most competitive models for generating Chinese text, boasting better performance in various tasks compared to BART. Thus, it serves as a strong baseline for doctor chatbots. CPT can consistently produce fluent and eloquent responses, as demonstrated by [2], and we can also provide some examples randomly drawn from dialog in our work：
- Original Text: 会觉得在生活中是自己在拖累别人吗?
- Translation: Do you ever feel like you're burdening others in life?
- Original Text: 除了起床上厕所，每天晚上醒来的次数会超过两次吗？
- Translation: Apart from getting up to use the restroom, do you wake up more than twice every night?

Compared to ChatGPT, the main limitation of the CPT baseline lies in its inflexible diagnostic process, despite its ability to thoroughly inquire about symptoms. This limitation stems from the constrained training data available, as explained in the third paragraph of the introduction.

[1] Shao et al. "CPT: A Pre-Trained Unbalanced Transformer for Both Chinese Language Understanding and Generation." ArXiv, abs/2109.05729.(2021)

[2] Yao et al. "D4: a Chinese Dialogue Dataset for Depression-Diagnosis-Oriented Chat." EMNLP (2022)

**Q4:** Indeed, we tested our doctor chatbots on actual human depressed patients (See Section 4.3). What's more, we've discussed limitations and highlighted some future directions (e.g., extending to cover multiple mental disorders) in the "limitations" section.

We are eager to delve deeper into our future direction. We recognize that directly shaping prompts for ChatGPT might not comprehensively align with our aims, given considerations such as patient resistance and doctor empathy. As a solution, we are planning to further refine open-source LLMs through additional fine-tuning, utilizing the dialog data generated in this study. This paper represents the initial step toward our objectives, with ongoing efforts to attain them in the future.


