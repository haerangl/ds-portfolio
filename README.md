## Haerang Lee's Data Science Portfolio

I am a data scientist with anti-fraud, risk, and compliance domain experience. I built my career at the intersection of business judgment and data science, where I developed a well-rounded set of skills in business intuition, communication, analytics, and programming. I often serve as the interpreter between data scientists and business professionals. 

**By Day: Core Analytics and Science at Uber**
For Uber's executives who want to minimize the company's exposure to financial and reputational risks, our team provides insights into the robustness of Uber's processes, systems, and policies. While our clients and stakeholders may work in silos, we provide cross-functional and end-to-end reviews to recommend improvements. To a team of finance, risk, and compliance professionals, I bring data science to assess the company's health with increased speed and depth. I add a new layer of insight from science and engineering to evaluate data risks, such as governance or quality issues. I also train other members of the department in data analytics, including hypothesis testing, exploratory analysis, and SQL.

Earlier in my career, I worked at KPMG. For companies looking to identify potential fraud or build a case for litigation, I identified the patterns of fraud or assessed legal claims using data analysis. For audit or legal professionals who were unfamiliar with analytical or statistical tools, I quantified and visually represented the data to communicate insights. 

**By Night: Data Science Graduate Student at UC Berkeley**
I am currently pursuing the Master of Information and Data Science at UC Berkeley (evenings and weekends) and this portfolio is a collection of my projects from the program.  

1. **Statistical modeling**
   1. [Experiment and Causal Inference in R - **Speaking Science: Effect of Locality in Science Engagement**](https://github.com/haerangl/speaking-science)\*  
   In this experiment, my team and I examine whether the proximity to the location discussed in a science news article affects the reader’s engagement with the article and its topic. We picked the research question and designed the experiment from scratch. We designed the metrics, the randomization method, and data collection mechanisms. We determined the sample size to maximize the statistical power and analyzed the results.    
   We conducted an online survey, in which treatment and control groups received the same article discussing the impact of air pollution, except that the keywords indicating the location differed. For treatment, the location keywords were of the reader's own city, and for control, they were of a remote city.  
   For the outcome, we operationalized the conceptual variable of *engagement* by creating three metrics: article reading time, donation toward alleviating air pollution, and reading comprehension quiz score. We considered clustering, blocking, spillover, and other real life issues to arrive at the final design of our study.  
   We analyzed the results using linear regressions to determine the causal relationship. Locality appeared to increase readers' reading comprehension of the article, while not having any statistically significant impact on the reading time or the donation amount toward the science issue. However, the results may not generalize well to the broader world due to the nature of the survey participants and the lab environment.  
     
   1. [Econometrics and Linear Regressions in R - **Crime in North Carolina**](Econometrics%20in%20R%20-%20NC%20Crime)\*  
   In this paper, my team and I examine the correlation between North Carolina's 1987 crime rate per county and several independent variables, including the average sentence length, percentage of racial minorities, and wages. We build and compare three linear models for their validity and robustness, then provide data-driven policy suggestions. Our results indicate that stricter criminal justice does not have practical implications in reducing crime.

1. **Machine Learning**
   1. [Convoluted Neural Network - **Facial Keypoint Detection** (Kaggle)](Convoluted%20Neural%20Network%20-%20Facial%20Keypoint%20Detection%20(Kaggle))\*  
   Our team tackled the Kaggle Facial Keypoints Detection Challenge using CNN. As of May '20, we estimate that our model would place around 35th among the participants. We experimented with various methods to fill the missing data, CNN architectures, and data augmentation techniques. We achieved the minimum loss with the model featuring VGG-16, KNN to fill NAs, data augmentation, and transfer learning. The resulting model generalized well even on tilted or turned faces.  
   
1. **Programming** 
    1. [OOP in Python - **Finding Flipper, a Text Game**](OOP%20in%20Python%20-%20Finding%20Flipper,%20a%20Text%20Game)  
    I built a simple text game to play in the command line prompt. The objective of the game is to tell Albert, the main character, to move around the house until he finds Flipper the cat. Inside the code, there are three classes--Friend, Activity, and Locations--each of which takes on various forms throughout the game and interacts with each other.


\*Group projects
