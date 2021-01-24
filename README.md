# corporasystembias

Code for the paper: Corpora Evaluation and System Bias Detection in Multi-document Summarization


CORPUS:
For Pyramid evaluation through PyrEval:
1 -> Write a python script to copy and paste files from your respective source directories to the appropriate folders in PyrEval(Documents - Raw/model and Ground truth summaries -      Raw/peer). This script needs to run in a loop for every topic in the corpus to get the final set of CSVs.
2 -> In pyreval.py file set the below :
     command to '0' at https://github.com/serenayj/PyrEval/blob/master/pyreval.py#L193, 
     remove the infinte loop at https://github.com/serenayj/PyrEval/blob/master/pyreval.py#L187, 
     add clear method in the end of autorun at https://github.com/serenayj/PyrEval/blob/master/pyreval.py#L36.
3 -> Remove any steps of deleting csvs if present in above mentioned clear() method
4 -> Write a python code to run through all the CSVs for each topic and calculate average

For Inv-Pyramid:
1 -> Since we are calculating the SCUs on a per document basis, write a python script to copy a single document 4 times in the Raw/model folder.
2 -> Each SCU generated will could be present multiple times, pick the unique ones among them.
3 -> Document SCUs can be found easily by putting the candidate set in the Raw/model folder.
4 -> Due to limited semantic understanding of Neural nets, SCUs may present in documents may not exactly match the SCU in reference.
5 -> Use any similarity alogorithm to match the SCU's, in our cases after manual evaluation we setted for Cosine similarity above 0.4.
