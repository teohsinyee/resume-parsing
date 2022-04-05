## 1] Stackexchange answer

Quoted _Brian Spiering_ : <br>
Deep learning parser should be **sequence-based** (e.g., Recurrent Neural Network (RNN) or Long Short Term Memory (LSTM)).
To apply Deep Learning, you'll need many thousands of examples with each section labeled. 
There is HR-XML (Human Resources - Extensible Markup Language) which are the industry standards for labels of resume sections.

HR-XML: https://schemas.liquid-technologies.com/hr-xml/2007-04-15/?page=http___ns_hr-xml_org_2007-04-15.html
Question: https://datascience.stackexchange.com/questions/71372/how-to-approach-deep-learning-cv-resume-parser-using-convolutions

## 2] BroutonLab software
Used **stacked bidirectional GRU/LSTM recurrent layers**

This approach was also compared with Convolutional layers, which are generally faster than recurrent layers, but recurrent layers have shown better accuracy.

We experimented with different vector embeddings including **fastText** and **custom Word2vec**. This helped us to significantly reduce the following:
- Dependency on the amount of labeled data
- Time needed model training

#### Topic modeling
- Used several unsupervised approaches for text clusterization by topics. 
- Particularly, we used **BigARTM** to resolve this problem because it showed better performance and accuracy when compared to other libraries such as Gensim.

BroutonLab AI parser: https://broutonlab.com/broutonlab-data-science-success-stories/ai-nlp-for-resume-parsing-and-job-matching

## 3]
