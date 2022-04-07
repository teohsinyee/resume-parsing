## 1] Stackexchange answer

Quoted _Brian Spiering_ : <br>
Deep learning parser should be **sequence-based** (e.g., Recurrent Neural Network (RNN) or Long Short Term Memory (LSTM)).
To apply Deep Learning, you'll need many thousands of examples with each section labeled. 
There is HR-XML (Human Resources - Extensible Markup Language) which are the industry standards for labels of resume sections.

HR-XML: https://schemas.liquid-technologies.com/hr-xml/2007-04-15/?page=http___ns_hr-xml_org_2007-04-15.html
<br>
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

## 3] Overview of Stanford NER Tagger
https://www.listendata.com/2018/05/named-entity-recognition-using-python.html

## 4] Skills API
https://apilayer.com/marketplace/description/skills-api

## 5] Codes to extract each fields
- Quite simple & straight forward

| Field         | Method        |
| :------------- |:-------------| 
| Name          | NLTK          | 
| Skills        | Corpus/API with help of N-gram   |   
| Institution   | Find institution corpus to train NER model & train using Spacy | 

https://blog.apilayer.com/build-your-own-resume-parser-using-python-and-nlp/

## 6] Accurate software demo
- Return in JSON format with 7 main keys (headers)

| Personal info      | My comments      |
| :------------- |:-------------| 
| Name| Accurate becuz it's simple |
| Email, Phone | Accurate becuz it's simple (Regex) |
| Home Address | Segmented to designated fields. Detection of *country & states & postcodes* are accurate. Data enrichment is good (E.g. Convert Pulau Pinang to Penang) |
| URL | Able to differentiate social media domain such as LinkedIn |
| Gender | Gender prediction using picture provided |

| Educations     | My comments      |
| ------------- |:-------------| 
|Title|Accurate. E.g. Master of Science(Msc) |   
|Institution name| Can detect non-English| 
|course titles| Accurate|   
|Date start & ends| Inaccurate why?|

| Other headers     | My comments      |
| :------------- |:-------------| 
| Working experiences | Can't even process 'Research Fellow' or 'tutor'.|   
| Skills  | Accurate | 
| Languages  | Accurate | 
| Tasks  | Less useful | 
| Attachments  | Less useful | 


https://labs.hrflow.ai/profile-analysis/parsing/

## 7] Detailed & layman's NER Process
1. Collected 420 resumes
2. Annotate manually using Doccano
3. Split into 80(training), 20(testing)
4. Develop model using Spacy
- Becuz Spacy got higher speed & accuracy
- Can refer to Spacy archi
5. Train model
- Use techniques like dropout & shuffle data after each iteration
6. Evaluate model
- Use mterics such as accuracy score, precision, recall, and F-score

https://www.kharpann.com/portfolio/named-entity-recognition-from-resumes/

## 8] Approaches to NER
### CRF to model sequential data (ML)
####  Shortcomings
1. Can capture prev,current words but NOT forward word
2. Need to do extra feature engineering

### Deep Learning
1. Evaluate performance using F1 Score (To get balance between precision & recall)
2. Use Bi-LSTM (To take past & future info AKA 1 LSTM run LEFT to RIGHT, another 1 run RIGHT to LEFT) <br>

_Bi-Directional Architecture_
1. Bi-LSTM-CRF
2. Bi-LSTM-CNN
3. LSTM-CNN-CRF
4. ELMo

https://towardsdatascience.com/named-entity-recognition-ner-meeting-industrys-requirement-by-applying-state-of-the-art-deep-698d2b3b4ede
