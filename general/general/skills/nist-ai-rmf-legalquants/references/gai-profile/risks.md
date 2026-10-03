# The 12 GAI Risks

*From NIST AI 600-1 (Generative AI Profile, July 2024), Section 2. Risks unique to or exacerbated by generative AI, with their Trustworthy AI characteristic mappings.*

Quick index:

- [1. CBRN Information or Capabilities](#1-cbrn-information-or-capabilities)
- [2. Confabulation](#2-confabulation)
- [3. Dangerous, Violent, or Hateful Content](#3-dangerous-violent-or-hateful-content)
- [4. Data Privacy](#4-data-privacy)
- [5. Environmental Impacts](#5-environmental-impacts)
- [6. Harmful Bias and Homogenization](#6-harmful-bias-and-homogenization)
- [7. Human-AI Configuration](#7-human-ai-configuration)
- [8. Information Integrity](#8-information-integrity)
- [9. Information Security](#9-information-security)
- [10. Intellectual Property](#10-intellectual-property)
- [11. Obscene, Degrading, and/or Abusive Content](#11-obscene-degrading-and-or-abusive-content)
- [12. Value Chain and Component Integration](#12-value-chain-and-component-integration)

## 1. CBRN Information or Capabilities <a id="1-cbrn-information-or-capabilities"></a>

In the future, GAI may enable malicious actors to more easily access CBRN weapons and/or relevant knowledge, information, materials, tools, or technologies that could be misused to assist in the design, development, production, or use of CBRN weapons or other dangerous materials or agents. While relevant biological and chemical threat knowledge and information is often publicly accessible, LLMs could facilitate its analysis or synthesis, particularly by individuals without formal scientific training or expertise.

Recent research on this topic found that LLM outputs regarding biological threat creation and attack planning provided minimal assistance beyond traditional search engine queries, suggesting that state-ofthe-art LLMs at the time these studies were conducted do not substantially increase the operational likelihood of such an attack. The physical synthesis development, production, and use of chemical or biological agents will continue to require both applicable expertise and supporting materials and infrastructure. The impact of GAI on chemical or biological agent misuse will depend on what the key barriers for malicious actors are (e.g., whether information access is one such barrier), and how well GAI can help actors address those barriers.

Furthermore, chemical and biological design tools (BDTs) – highly specialized AI systems trained on scientific data that aid in chemical and biological design – may augment design capabilities in chemistry and biology beyond what text-based LLMs are able to provide. As these models become more efficacious, including for beneficial uses, it will be important to assess their potential to be used for harm, such as the ideation and design of novel harmful chemical or biological agents.

While some of these described capabilities lie beyond the reach of existing GAI tools, ongoing assessments of this risk would be enhanced by monitoring both the ability of AI tools to facilitate CBRN weapons planning and GAI systems’ connection or access to relevant data and tools.

**Trustworthy AI Characteristics:** Safe, Explainable and Interpretable

## 2. Confabulation <a id="2-confabulation"></a>

“Confabulation” refers to a phenomenon in which GAI systems generate and confidently present erroneous or false content in response to prompts. Confabulations also include generated outputs that diverge from the prompts or other input or that contradict previously generated statements in the same context. These phenomena are colloquially also referred to as “hallucinations” or “fabrications.”

Confabulations can occur across GAI outputs and contexts.9,10 Confabulations are a natural result of the way generative models are designed: they generate outputs that approximate the statistical distribution of their training data; for example, LLMs predict the next token or word in a sentence or phrase. While such statistical prediction can produce factually accurate and consistent outputs, it can also produce outputs that are factually inaccurate or internally inconsistent. This dynamic is particularly relevant when it comes to open-ended prompts for long-form responses and in domains which require highly contextual and/or domain expertise.

Risks from confabulations may arise when users believe false content – often due to the confident nature of the response – leading users to act upon or promote the false information. This poses a challenge for many real-world applications, such as in healthcare, where a confabulated summary of patient information reports could cause doctors to make incorrect diagnoses and/or recommend the wrong treatments. Risks of confabulated content may be especially important to monitor when integrating GAI into applications involving consequential decision making.

GAI outputs may also include confabulated logic or citations that purport to justify or explain the system’s answer, which may further mislead humans into inappropriately trusting the system’s output. For instance, LLMs sometimes provide logical steps for how they arrived at an answer even when the answer itself is incorrect. Similarly, an LLM could falsely assert that it is human or has human traits, potentially deceiving humans into believing they are speaking with another human.

The extent to which humans can be deceived by LLMs, the mechanisms by which this may occur, and the potential risks from adversarial prompting of such behavior are emerging areas of study. Given the wide range of downstream impacts of GAI, it is difficult to estimate the downstream scale and impact of confabulations.

**Trustworthy AI Characteristics:** Fair with Harmful Bias Managed, Safe, Valid and Reliable, Explainable and Interpretable

## 3. Dangerous, Violent, or Hateful Content <a id="3-dangerous-violent-or-hateful-content"></a>

GAI systems can produce content that is inciting, radicalizing, or threatening, or that glorifies violence, with greater ease and scale than other technologies. LLMs have been reported to generate dangerous or violent recommendations, and some models have generated actionable instructions for dangerous or

9 Confabulations of falsehoods are most commonly a problem for text-based outputs; for audio, image, or video content, creative generation of non-factual content can be a desired behavior.

10 For example, legal confabulations have been shown to be pervasive in current state-of-the-art LLMs. See also, e.g.,

unethical behavior. Text-to-image models also make it easy to create images that could be used to promote dangerous or violent messages. Similar concerns are present for other GAI media, including video and audio. GAI may also produce content that recommends self-harm or criminal/illegal activities.

Many current systems restrict model outputs to limit certain content or in response to certain prompts, but this approach may still produce harmful recommendations in response to other less-explicit, novel prompts (also relevant to CBRN Information or Capabilities, Data Privacy, Information Security, and Obscene, Degrading and/or Abusive Content). Crafting such prompts deliberately is known as “jailbreaking,” or, manipulating prompts to circumvent output controls. Limitations of GAI systems can be harmful or dangerous in certain contexts. Studies have observed that users may disclose mental health issues in conversations with chatbots – and that users exhibit negative reactions to unhelpful responses from these chatbots during situations of distress. This risk encompasses difficulty controlling creation of and public exposure to offensive or hateful language, and denigrating or stereotypical content generated by AI. This kind of speech may contribute to downstream harm such as fueling dangerous or violent behaviors. The spread of denigrating or stereotypical content can also further exacerbate representational harms (see Harmful Bias and Homogenization below).

**Trustworthy AI Characteristics:** Safe, Secure and Resilient

## 4. Data Privacy <a id="4-data-privacy"></a>

GAI systems raise several risks to privacy. GAI system training requires large volumes of data, which in some cases may include personal data. The use of personal data for GAI training raises risks to widely accepted privacy principles, including to transparency, individual participation (including consent), and

purpose specification. For example, most model developers do not disclose specific data sources on which models were trained, limiting user awareness of whether personally identifiably information (PII) was trained on and, if so, how it was collected.

Models may leak, generate, or correctly infer sensitive information about individuals. For example, during adversarial attacks, LLMs have revealed sensitive information (from the public domain) that was included in their training data. This problem has been referred to as data memorization, and may pose exacerbated privacy risks even for data present only in a small number of training samples.

In addition to revealing sensitive information in GAI training data, GAI models may be able to correctly infer PII or sensitive data that was not in their training data nor disclosed by the user by stitching together information from disparate sources. These inferences can have negative impact on an individual even if the inferences are not accurate (e.g., confabulations), and especially if they reveal information that the individual considers sensitive or that is used to disadvantage or harm them.

Beyond harms from information exposure (such as extortion or dignitary harm), wrong or inappropriate inferences of PII can contribute to downstream or secondary harmful impacts. For example, predictive inferences made by GAI models based on PII or protected attributes can contribute to adverse decisions, leading to representational or allocative harms to individuals or groups (see Harmful Bias and Homogenization below).

**Trustworthy AI Characteristics:** Accountable and Transparent, Privacy Enhanced, Safe, Secure and Resilient

## 5. Environmental Impacts <a id="5-environmental-impacts"></a>

Training, maintaining, and operating (running inference on) GAI systems are resource-intensive activities, with potentially large energy and environmental footprints. Energy and carbon emissions vary based on what is being done with the GAI model (i.e., pre-training, fine-tuning, inference), the modality of the content, hardware used, and type of task or application.

Current estimates suggest that training a single transformer LLM can emit as much carbon as 300 roundtrip flights between San Francisco and New York. In a study comparing energy consumption and carbon emissions for LLM inference, generative tasks (e.g., text summarization) were found to be more energyand carbon-intensive than discriminative or non-generative tasks (e.g., text classification).

Methods for creating smaller versions of trained models, such as model distillation or compression, could reduce environmental impacts at inference time, but training and tuning such models may still contribute to their environmental impacts. Currently there is no agreed upon method to estimate environmental impacts from GAI.

**Trustworthy AI Characteristics:** Accountable and Transparent, Safe

## 6. Harmful Bias and Homogenization <a id="6-harmful-bias-and-homogenization"></a>

Bias exists in many forms and can become ingrained in automated systems. AI systems, including GAI systems, can increase the speed and scale at which harmful biases manifest and are acted upon, potentially perpetuating and amplifying harms to individuals, groups, communities, organizations, and society. For example, when prompted to generate images of CEOs, doctors, lawyers, and judges, current text-to-image models underrepresent women and/or racial minorities, and people with disabilities. Image generator models have also produced biased or stereotyped output for various demographic groups and have difficulty producing non-stereotyped content even when the prompt specifically requests image features that are inconsistent with the stereotypes. Harmful bias in GAI models, which may stem from their training data, can also cause representational harms or perpetuate or exacerbate bias based on race, gender, disability, or other protected classes.

Harmful bias in GAI systems can also lead to harms via disparities between how a model performs for different subgroups or languages (e.g., an LLM may perform less well for non-English languages or certain dialects). Such disparities can contribute to discriminatory decision-making or amplification of existing societal biases. In addition, GAI systems may be inappropriately trusted to perform similarly across all subgroups, which could leave the groups facing underperformance with worse outcomes than if no GAI system were used. Disparate or reduced performance for lower-resource languages also presents challenges to model adoption, inclusion, and accessibility, and may make preservation of endangered languages more difficult if GAI systems become embedded in everyday processes that would otherwise have been opportunities to use these languages. Bias is mutually reinforcing with the problem of undesired homogenization, in which GAI systems produce skewed distributions of outputs that are overly uniform (for example, repetitive aesthetic styles

and reduced content diversity). Overly homogenized outputs can themselves be incorrect, or they may lead to unreliable decision-making or amplify harmful biases. These phenomena can flow from foundation models to downstream models and systems, with the foundation models acting as “bottlenecks,” or single points of failure.

Overly homogenized content can contribute to “model collapse.” Model collapse can occur when model training over-relies on synthetic data, resulting in data points disappearing from the distribution of the new model’s outputs. In addition to threatening the robustness of the model overall, model collapse could lead to homogenized outputs, including by amplifying any homogenization from the model used to generate the synthetic training data.

**Trustworthy AI Characteristics:** Fair with Harmful Bias Managed, Valid and Reliable

## 7. Human-AI Configuration <a id="7-human-ai-configuration"></a>

GAI system use can involve varying risks of misconfigurations and poor interactions between a system and a human who is interacting with it. Humans bring their unique perspectives, experiences, or domainspecific expertise to interactions with AI systems but may not have detailed knowledge of AI systems and how they work. As a result, human experts may be unnecessarily “averse” to GAI systems, and thus deprive themselves or others of GAI’s beneficial uses.

Conversely, due to the complexity and increasing reliability of GAI technology, over time, humans may over-rely on GAI systems or may unjustifiably perceive GAI content to be of higher quality than that produced by other sources. This phenomenon is an example of automation bias, or excessive deference to automated systems. Automation bias can exacerbate other risks of GAI, such as risks of confabulation or risks of bias or homogenization.

There may also be concerns about emotional entanglement between humans and GAI systems, which could lead to negative psychological impacts.

**Trustworthy AI Characteristics:** Accountable and Transparent, Explainable and Interpretable, Fair with Harmful Bias Managed, Privacy Enhanced, Safe, Valid and Reliable

## 8. Information Integrity <a id="8-information-integrity"></a>

Information integrity describes the “spectrum of information and associated patterns of its creation, exchange, and consumption in society.” High-integrity information can be trusted; “distinguishes fact from fiction, opinion, and inference; acknowledges uncertainties; and is transparent about its level of vetting. This information can be linked to the original source(s) with appropriate evidence. High-integrity information is also accurate and reliable, can be verified and authenticated, has a clear chain of custody, and creates reasonable expectations about when its validity may expire.”11

11 This definition of information integrity is derived from the 2022 White House Roadmap for Researchers on Priorities Related to Information Integrity Research and Development.

GAI systems can ease the unintentional production or dissemination of false, inaccurate, or misleading content (misinformation) at scale, particularly if the content stems from confabulations.

GAI systems can also ease the deliberate production or dissemination of false or misleading information (disinformation) at scale, where an actor has the explicit intent to deceive or cause harm to others. Even very subtle changes to text or images can manipulate human and machine perception.

Similarly, GAI systems could enable a higher degree of sophistication for malicious actors to produce disinformation that is targeted towards specific demographics. Current and emerging multimodal models make it possible to generate both text-based disinformation and highly realistic “deepfakes” – that is, synthetic audiovisual content and photorealistic images.12 Additional disinformation threats could be enabled by future GAI models trained on new data modalities.

Disinformation and misinformation – both of which may be facilitated by GAI – may erode public trust in true or valid evidence and information, with downstream effects. For example, a synthetic image of a Pentagon blast went viral and briefly caused a drop in the stock market. Generative AI models can also assist malicious actors in creating compelling imagery and propaganda to support disinformation campaigns, which may not be photorealistic, but could enable these campaigns to gain more reach and engagement on social media platforms. Additionally, generative AI models can assist malicious actors in creating fraudulent content intended to impersonate others.

**Trustworthy AI Characteristics:** Accountable and Transparent, Safe, Valid and Reliable, Interpretable and Explainable

## 9. Information Security <a id="9-information-security"></a>

Information security for computer systems and data is a mature field with widely accepted and standardized practices for offensive and defensive cyber capabilities. GAI-based systems present two primary information security risks: GAI could potentially discover or enable new cybersecurity risks by lowering the barriers for or easing automated exercise of offensive capabilities; simultaneously, it expands the available attack surface, as GAI itself is vulnerable to attacks like prompt injection or data poisoning.

Offensive cyber capabilities advanced by GAI systems may augment cybersecurity attacks such as hacking, malware, and phishing. Reports have indicated that LLMs are already able to discover some vulnerabilities in systems (hardware, software, data) and write code to exploit them. Sophisticated threat actors might further these risks by developing GAI-powered security co-pilots for use in several parts of the attack chain, including informing attackers on how to proactively evade threat detection and escalate privileges after gaining system access.

Information security for GAI models and systems also includes maintaining availability of the GAI system and the integrity and (when applicable) the confidentiality of the GAI code, training data, and model weights. To identify and secure potential attack points in AI systems or specific components of the AI

12 See also https://doi.org/10.6028/NIST.AI.100-4, to be published.

value chain (e.g., data inputs, processing, GAI training, or deployment environments), conventional cybersecurity practices may need to adapt or evolve.

For instance, prompt injection involves modifying what input is provided to a GAI system so that it behaves in unintended ways. In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. Indirect prompt injection attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by stealing proprietary data or running malicious code remotely on a machine. Merely querying a closed production model can elicit previously undisclosed information about that model.

Another cybersecurity risk to GAI is data poisoning, in which an adversary compromises a training dataset used by a model to manipulate its outputs or operation. Malicious tampering with data or parts of the model could exacerbate risks associated with GAI system outputs.

**Trustworthy AI Characteristics:** Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable

## 10. Intellectual Property <a id="10-intellectual-property"></a>

Intellectual property risks from GAI systems may arise where the use of copyrighted works is not a fair use under the fair use doctrine. If a GAI system’s training data included copyrighted material, GAI outputs displaying instances of training data memorization (see Data Privacy above) could infringe on copyright.

How GAI relates to copyright, including the status of generated content that is similar to but does not strictly copy work protected by copyright, is currently being debated in legal fora. Similar discussions are

taking place regarding the use or emulation of personal identity, likeness, or voice without permission.

**Trustworthy AI Characteristics:** Accountable and Transparent, Fair with Harmful Bias Managed, Privacy Enhanced

## 11. Obscene, Degrading, and/or Abusive Content <a id="11-obscene-degrading-and-or-abusive-content"></a>

GAI can ease the production of and access to illegal non-consensual intimate imagery (NCII) of adults, and/or child sexual abuse material (CSAM). GAI-generated obscene, abusive or degrading content can create privacy, psychological and emotional, and even physical harms, and in some cases may be illegal.

Generated explicit or obscene AI content may include highly realistic “deepfakes” of real individuals, including children. The spread of this kind of material can have downstream negative consequences: in the context of CSAM, even if the generated images do not resemble specific individuals, the prevalence of such images can divert time and resources from efforts to find real-world victims. Outside of CSAM, the creation and spread of NCII disproportionately impacts women and sexual minorities, and can have subsequent negative consequences including decline in overall mental health, substance abuse, and even suicidal thoughts. Data used for training GAI models may unintentionally include CSAM and NCII. A recent report noted that several commonly used GAI training datasets were found to contain hundreds of known images of

CSAM. Even when trained on “clean” data, increasingly capable GAI models can synthesize or produce synthetic NCII and CSAM. Websites, mobile apps, and custom-built models that generate synthetic NCII have moved from niche internet forums to mainstream, automated, and scaled online businesses.

**Trustworthy AI Characteristics:** Fair with Harmful Bias Managed, Safe, Privacy Enhanced

## 12. Value Chain and Component Integration <a id="12-value-chain-and-component-integration"></a>

GAI value chains involve many third-party components such as procured datasets, pre-trained models, and software libraries. These components might be improperly obtained or not properly vetted, leading to diminished transparency or accountability for downstream users. While this is a risk for traditional AI systems and some other digital technologies, the risk is exacerbated for GAI due to the scale of the training data, which may be too large for humans to vet; the difficulty of training foundation models, which leads to extensive reuse of limited numbers of models; and the extent to which GAI may be integrated into other devices and services. As GAI systems often involve many distinct third-party components and data sources, it may be difficult to attribute issues in a system’s behavior to any one of these sources

Errors in third-party GAI components can also have downstream impacts on accuracy and robustness. For example, test datasets commonly used to benchmark or validate models can contain label errors. Inaccuracies in these labels can impact the “stability” or robustness of these benchmarks, which many GAI practitioners consider during the model selection process.

**Trustworthy AI Characteristics:** Accountable and Transparent, Explainable and Interpretable, Fair with Harmful Bias Managed, Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable
