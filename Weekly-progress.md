## Week 4 (04-Apr to 07-Apr)

1. Figure out PDF metadata that could be useful
2. Find tools that can extract coordinates & font styles from PDF
    - [coordinates](https://www.e-iceblue.com/Tutorials/Spire.PDF/Spire.PDF-Program-Guide/Text/How-to-Get-Coordinates-of-Desired-Text-in-PDF-in-C-VB.NET.html)
    - [font styles](https://stackoverflow.com/questions/68097779/how-to-find-the-font-size-of-every-paragraph-of-pdf-file-using-python-code)
3. Test on existing parsers
    - Tested on 3 tools
    - Commercial (https://affinda.com/resume-parser/) (https://labs.hrflow.ai/profile-analysis/parsing/) <br>
    - Free (https://demos.pragnakalp.com/resume-parser/)
    - None of it is perfect (Still failed to parse some info)
4. Study Named Entity Recognition (NER) [Completed]
    - Because many tagging schemes
    - BIO, BIOSE, IOB, BILOU, BMEWO - Gives different performance
5. Text annotation tools [On-going]
    - Doccano *Make a comparison
    - Brat
6. Proposed pipeline to Pei Seng 
#### Feedback
1. How to compare our parser performance with the existing ones? (Quantitative)
2. How to test parser result accuracy?

### Will be working on
1. Development (Prove proposed pipeline)

## Week 5 (11-Apr to 15-Apr)
1. Classify 500 resumes into scanned images and contains text folders
    - Will abandon scanned images PDF as for now
2. Research on GROBID (extration model of scholar articles) [Deprecated because less useful]
3. Proposed new pipeline & gained new feedback (Mentor suggested to research more about deep learning)
4. Comparing annotation tool (to annotate text line) : Doccano vs Label studio

## Week 6 (18-Apr to 22-Apr)
1. Compared Label Studio with Doccano 
    - Label studio cannot perform multi-label for each line (TBC)
    - Label studio output is a bit cluttered
    - Doccano can multi-label & export annotated text in JSON & CSV format
    - If use Doccano, the input file should contained all resumes text, cannot separated files
2. Decide annotation labels 
    - 6 Classes (education, ... )
    - 3 general (header, content, other)
    - Consider to add sentence writing style (simple,keyvalue,complex)
3. Brainstorm how to use the annotated text
    - ???

## Week 7 (25-Apr to 29-Apr)
1. Study Machine Learning (only NN part) course by Andrew Ng
2. Refine the resume tags (change from 6 tags to 13 tags)
3. Improvise literature review of 10 papers 
4. Annotate 100 resumes using Doccano

## Week 8 (05-May to 06-May)
1. Back to stage 1 - segregate all pdf contains tables using Camelot (in-progress)


