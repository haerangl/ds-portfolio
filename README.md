## Haerang Lee's Data Science Portfolio

### Data Scientist in Training

A data analyst with seven years of experience, I may have never had a data scientist title at work. Still, I've dedicated 20-30 hours/week for the last 12 months in a rigorous part-time data science master's program at UC Berkeley. This portfolio is a collection of my work to demonstrate my technical skills.

1. **Statistical modeling**
   1. [Experiment and Causal Inference in R - **Speaking Science: Effect of Locality in Science Engagement**](https://github.com/haerangl/speaking-science)\*  
   In this experiment, my team and I examine whether the proximity to the location discussed in a science news article affects the reader’s engagement with the article and its topic. We picked the research question and designed the experiment from scratch. We designed the metrics, the randomization method, and the survey flow. We determined the sample size to maximize the statistical power and analyzed the results.    
   We conducted an online survey, in which treatment and control groups received the same article discussing the impact of air pollution, except that the keywords indicating the location differed. For treatment, the location keywords were of the reader's own city, and for control, they were of a remote city.  
   For the outcome, we operationalized the conceptual variable of *engagement* by creating three metrics: article reading time, donation toward alleviating air pollution, and reading comprehension quiz score. We considered clustering, blocking, spillover, and other real life issues to arrive at the final design of our study.  
   We analyzed the results using linear regressions to determine the causal relationship. Locality appeared to increase readers' reading comprehension of the article, while not having any statistically significant impact on the reading time or the donation amount toward the science issue. However, although we may have had enough statistical power to detect real differences, the results may not generalize well to the broader world.  
     
   1. [Econometrics and Linear Regressions in R - **Crime in North Carolina**](Econometrics%20in%20R%20-%20NC%20Crime)\*  
   In this paper, my team and I examine the correlation between North Carolina's 1987 crime rate per county and several independent variables, including the average sentence length, percentage of racial minorities, and wages. We build and compare three linear models for their validity and robustness, then provide data-driven policy suggestions. Our results indicate that stricter criminal justice does not have practical implications in reducing crime.

1. **Machine Learning**
   1. [Convoluted Neural Network - **Facial Keypoint Detection** (Kaggle)](Convoluted%20Neural%20Network%20-%20Facial%20Keypoint%20Detection%20(Kaggle))\*  
   Our team tackled the Kaggle Facial Keypoints Detection Challenge using CNN. As of May '20, we estimate that our model would place around 35th among the participants. We experimented with various methods to fill the missing data, CNN architectures, and data augmentation techniques. We achieved the minimum loss with the model featuring VGG-16, KNN to fill NAs, data augmentation, and transfer learning. The resulting model generalized well even on tilted or turned faces. 
1. **Programming** 
    1. [OOP in Python - **Finding Flipper, a Text Game**](OOP%20in%20Python%20-%20Finding%20Flipper,%20a%20Text%20Game)  
    I built a simple text game to play in the command line prompt. The objective of the game is to tell Albert, the main character, to move around the house until he finds Flipper the cat. Inside the code, there are three classes--Friend, Activity, and Locations--each of which takes on various forms throughout the game and interacts with each other.
1. **Data Analysis** 
   1. [Data Cleaning and Analysis in Python - **Dangerous Genetic Mutations**](Data%20Cleaning%20and%20Analysis%20in%20Python%20-%20Dangerous%20Genetic%20Mutations)  
   I parse a Variant Call Format (VCF) file to explore genetic mutations data and identify which of those should be considered dangerous. The emphasis of the exercise is on parsing messy data (e.g., file headers; key-value pairs inside of some columns), data cleansing, and exploring to understand the contents and trends.
   1. [Analysis in Pandas - **CMS Hospital Quality Analysis**](Analysis%20in%20Pandas%20-%20CMS%20Hospital%20Quality%20Analysis)\*  
   In this project, My teammate and I obtained the Hospital Compare datasets from the Centers for Medicare & Medicaid Services (CMS) website. We used Pandas and Matplotlib to do explore data and to find which hospitals offered the best care in the US. We observed that the hospitals in the Rocky West and Midwest regions scored consistently higher than the national average. We also noted that the patients could not always determine the quality of the medical processes they received, but they could tell when the quality of their experience was high. 

\*Group projects
