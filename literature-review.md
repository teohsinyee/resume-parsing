# 1] Smart Recruitment — Cracking Resume Parsing through Deep Learning @ Medium
### Keypoints
1. text extraction could not be solved by a single type of algorithm alone.
2. created an entirely new classification system to segregate the resumes into different types, based on their template, and tackle each type differently. 
3. most of them (like the ones that contain tables, partitions, etc) 
4. For such complex types, we decided to use Optical Character Recognition (OCR) along with some Deep NLP algorithms on top, to extract text.
5. the hard way would be to build a deep learning model from scratch for OCR and NLP, and the smart way was to use the power of open source and deploy an off the shelf model for the task.
6. we are able to extract text accurately from about 98% of simple resumes and 90% of the complex ones.

### Challenges
1. Corpus not updated (new companies everyday)
2. Different meanings of same word

### Approaches
1. Apply NER to deep learning model ([BIOES tagging](http://ml.cau.ac.kr/activities/outputs/210803-BIOES,%20Conditional%20Random%20Field.pdf))
2. model architecture-LSTMs 
(it takes into account the context of a word in a statement)
3. curate dataset for model training and evaluation
(started unlabelled training data & searched for tools online for manual annotation efforts within the team). 
4. hired some people to do the data labelling and started the training process 
5. model had crossed our benchmark of 80.0

# 2] 
