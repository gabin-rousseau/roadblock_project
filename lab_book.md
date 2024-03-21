# Lab book 01-05 2024
### Project: Computer simulation of a roadblock model of translational control
### Author: Gabin A. M. ROUSSEAU

_The following lab book contains daily entries of the tasks carried out by Gabin (bullet points), followed by weekly plans for the following week (task lists, updated every Saturday)._

---
# Week 1 - 15/01 --> 19/01

## Day 1 - 15/01
- Practiced using the Github dev environment in order to modify and run jupyter notebooks if ever necessary.
- Discussed lab desk usage and lab book format (this one).
- Discussed Health and Safety measures as well as Ethical implications: none to report. Will have to return to this topic if I get the chance to shadow someone in the lab out of curiosity.
- Discussed literature review: Edward oriented my search of publications towards the modelling aspect, specifically the distinction between translational elongation modeling and initiation (which we are focused on and is very rarely published about). _A contrario_, more peripheral considerations such as cell-wall biogenesis shouldn't occupy more than one paragraph. 
- __*Discussed worflow of the project: take a parallel approach where I make progress on the literature review and understanding the biology we are attempting to model, then experiment with the current version of the model to add in elements*__.
- Discussed model format: TASEP (especially TASEP with defects) should be the model format, Edward and Juraj provided reference encompassing this topic and its uses in computational biology / translational control modelling.
- Took the mandatory courses about the SBS buildings and Health and Safety measures, took two courses that introduced me properly to github and the .md format.

![Doodle of the initial model design for Ssd1 and translation initiation](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/model_doodle_150124.png)
E=free to access, X=occupied, footprint corresponds to the 43s pre-initiation complex

## Day 2 - 16/01
- Prepared this lab book file.
- Set up a local PC.
- Re-trained myself to use ubuntu by installing anaconda via the terminal. Had to reinstall and correct the mistake of letting the install put the main anaconda folder in root (succeeded).
- Put together the bibliography file in the project repository, that I will update and rearrange as needed. (format: Publication name; author; year + doi hyperlink)
- Searched for the kind of format I should give the first TASEP model version.
- Found Juraj's TASEPy that I could draw inspiration from.
- Literature shared by Edward that looks more closely at initiation doesn't seem to have a deep focus on initiation as opposed to elongation, but from what I could see, it looked like the main difference I should take into account will be the format of the lattice and particles. (work on elongation looks at codons, whereas we are more interested in the 43S PIC's ~50bp footprint. Lattice unit: BP? Take inspiration from Juraj's TASEPy and define 43S as a l=50 particle with a fixed site tracked by the model?) 
- Discussed with Ramon the fact that I can't rely on a rate-based formulaism like in the road_trial notebook, must think of a rule-based formulaism prior to returning to any kind of solver. Will begin on Day 3.
  
![TASEpy sketch of the TASEP with a particle of length 3](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/l3_TASEPy.png)
## Day 3 - 17/01
- Completed the [rini v0.1 TASEP model on python! (short for roadblock_ini)](https://github.com/gabin-rousseau/roadblock_project/blob/main/python/rini_v0-1.ipynb)

![First output of the TASEP model, here in the form of the total number of ribosomes that complete scanning over time](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/passed_graph_v0-1.png)
- Prepared one slide for Edward's meeting.

## Day 4 - 18/01
- Attended Ramon's lab meeting where Augustinas discussed his paper focusing on infering transcriptome-wide burst size and frequency associated with cell age/cycle _via_ a mathematical model.
- Discussed the first version of the model with Ramon (image below):

![White-board diagrams summarising the next steps for the model](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rini_meeting1.jpg)
- Ramon is happy with the first version and thinks the logic is solid. __Alpha, Beta and P should all be part of the user input__ (we'll assume P is the same for all sites for now). However, we should make sure we can extract THE variable of interest while checking the model fits the behaviour expected from a TASEP. Indeed, while my model can be considered closer to a cellular automatom, TASEP tend to follow  the Gillespie algortithm and are characterised by a __PHASE DIAGRAM__ (see diagram to the left of "phase" on the right of the photo). Therefore, the next steps for the model are as follows:
  1. Get the model to calculate the rate of particle passage.
  2. Plot that "initiation" against alpha and beta.
  3. Make phase diagram.
  4. Compare with local/general density measured over time. Does the phase diagram profile make sense with the expected/effective density profiles?
- Attended Edward's lab meeting. See how binding rates and particle configurations interact with the initiation rate. Discussed the continuous process that enables one to improve their communication skills in presentations. Highlighting the right phrase, color coding text to match figures, putting just the right amount of information on figures, figure choice... For my project presentation, I should dedicate a slide to the question and why we are asking it. Edward made me notice I was confusing DNA bp with RNA nt.

## Day 5 - 19/01
- Work remotely to make progress on the literature review.


---
# Week 2 - 22/01 --> 26/01
- [ ] Finish or get close to finishing the literature review.

For rini v0.2:
- [X] Add alpha, beta and psi as user input variables.
- [X] Get the rate of initiation I as an output.
- [X] Plot the change in I against alpha and beta.
- [X] Plot alpha against beta to obtain a phase diagram.
- [X] Loop in local density measurements to compare with phase diagram.
## Day 6 - 22/01
- Finished rini v0.2, which involved changing some variable names, add rates to the function arguments, adding default values for all arguments and add local density to the output. Plotting early graphs of density vs. time in a+b conditions satisfying all 3 typical TASEP phases (low-density, high-density, maximum-current) seemed to be promising overall, although the stochasticity of the model can make the trend skewed one way or another in certain runs. 
- Received Edward's reference list (added to the bibliography). Contains:
  - 2 key papers on translation initiation in C. cerevisiae.
  - 1 classic paper on the discovery of RNA scanning by Marilym Kozak
  - The recommendation to seek a background reference if needed for RNA 5' secondary structure, Pab1/PABP poly(A)-binding protein forming an auto-regulating loop with the 5'UTR.
  - 4 papers on Ssd1 and its role binding RNA and in translation initiation. Pointed out I can also find a paper on Ssd1 regulating CLN2 translation.

![Another TASEP phase diagram showcasing expected bulk densities and current values depending on the active phase](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/TASEP_phasedensities2.png)
## Day 7 - 23/01
- Completed 3 functions that complement rini to respond to the week's goals:
  1. rini_I estimates the "initiation" rate I in a rini run based on the coefficient for a line of best fit (calculate from t=L onwards to remove the startup assuming peak conditions)
  2. rini_IvAB plots I against alpha and beta respectively. If plotted against alpha, alpha values are determined in a numpy rangem while beta remains at a constant value (by default 1) and vice versa.
  3. rini_AvB draws a phase diagram on which either pre-determined rini points or a set amount of random points are plotted. Points are numerically labelled and the function prints the associated median density alongside the expected bulk density for the phase the point corresponds to. (low density, high density, maximum-current).
 
- Discussed these with Ramon. He is happy with the results and suggested linking the IvAB and AvB results to the average of multiple runs rather than just one. Now, I should focus more on Edward's references to discuss the next steps on Thursday.

![rini v0.2 line rate of initiation regression figure](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rini_ratefit.png)

![rini v0.2 phase diagram](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rini_phases.png)
## Day 8 - 24/01
- Explored the literature with the intent to find some contextual information that could guide the next steps for the model. Added some key sentences from references in the bibliogaphy.
- Discussed with Edward the notion of stress and its relation with Ssd1. Ssd1 deletion have been correlated to interesting phenotypes in stress responses but nothing definitive it seems. Discussed the presence of different cell-wall biogenesis instance in _S. cerevisiae_ such as in budding, segregation at the end of budding, sporulation or differences depending on growth phases. When we start integrating the roadblock in the model, it would be interesting to vary its on-off rates  following for example a clock inspired by the stages in cell cyle.
- Experimented with the point from which the regression is made for the initiation rate. If it is from the last 0 before the first passage the values get weird: if nothing passes for a long time a suddenly one manages to pass at the end of the simulation, the rate would be impressively high, but very poorly reflects its intended purpose. Wiser to stick to the condition time>=L to remove the optimal startup. This condition also allows for a constant standard in the calculation and the number of points included, which is essential for interpretation and comparison.

![The time>=L condition sets a sensible standard for initiation rate calculation by removing the absolutely necessary startup](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/I_conditiondemo.png)
## Day 9 - 25/01
- Attended Ramon's lab meeting where Rodrigo talked about a paper that coupled mathematical modeling to the study of clonal hematopoiesis in blood cancer.
- Discussed with Juraj the behaviour of my model. Once again, he noted TASEP is typically done following the Gillespie algorithm which does not rely on movement rejection for the stochastic progression of the model (see picture below). Rather than checking for movements in a random order and rolling a die to tell if X action is performed, the G-algorithm first derives a propensity array (typically A[a0, a1, ..., aL]) from the current configuration where ai = Si * applicable rate (p or b). a0=a when S1=0.

From that point, 3 numbers are calculated. R is the sum of all propensities. r1 determines when a movement will happen next and is derived randomly from an exponential (read up on that part): the next movement will be performed r1 from now (t + r1). r2 determines which movement happens and is equal to R multiplied by a random uniform number from 0 to 1. At the right time, change is confirmed relative to the state of site i: __sum(a0...ai)-ai < r2 <= sum(a0...ai)__ / while sum(a0...ai)-ai< r2  
- Discussed the model with Edward and Ramon. __Action points: integrate the Gillespie algorithm and a single roadblock, improve the presentation of the phase diagram for the new version by colour coding points based on the phase and plotting observed vs expected density while keeping the colour coding.__

Discussed sites for ssd1 binding, from 1 to 5 more or less close to one another or in several groups. We should start with one. The kinetics of the ribosomal helicase might be able to dislodge a roadblock like it disrupts obstacle mRNA secondary structures. Likewise, if blocked for too long, there is the possibility of the ribosome unloading prematurely. Discussed whether a roadblock may only have a chance of blocking the path. The approach should be to assume blocking is guaranteed and instead the wiggle room is more related to the on and off rate of roadblock binding.

- Attended Edward's meeting. Discussed what would be useful to present in his meetings. An approach would be to explain what I have done and how I checked how it works for suggestions or biological relevance of the course chosen.

![Drawings Juraj made to explain how the Gillespie algorithm works](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/gillespie_explanation.jpg)

## Day 10 - 26/01 
- Work remotely to make progress on the literature review
---
# Week 3 - 29/01 --> 02/02
- [ ] Finish the literature review.

For rini v0.3:
- [X] Integrate the Gillespie algorithm.
- [ ] Implement a single roadblock in the model.
- [ ] Improve the presentation of the phase diagram

## Day 11 - 29/01
- Began writing rini v0.3 but work was a bit slow due to illness. Switching to the Gillespie formulaism is requiring some change in the way loops are being organised. I should be able to finish the first implementation tomorrow and get started with the single roadblock as described in the paper of TASEP with defects I found.

## Day 12 - 30/01
- Completed the Gillespie integration that defines v0.3. Changed the exit current calculation to the simple ratio of total passed particles against time. The phase diagram is noticeably more consistent with the expectation once steady state is approximated (t=10000). Work to optimise the model may be needed in the future as the runtime will be slower due to the high amount of iterations for the same time frame.


## Day 13 - 31/01
- Established in markdown the logic behind implementing a roadblock, discussed the variables that introduces and asked important considerations in writing the actual code for the implementation. Prepared a density profile comparison between v0.2 and v0.3 (Goal, implement by Friday).
- v0.3b will be used for roadblock testing.

## Day 14 - 01/02
- Discussed the model with Ramon and Edward. Scratched the idea of having blocked sites influence the hopping rate. Blocks are simply another total restriction for progress. For result discussion, we define Pb as the probability of site blocking: Pb = k+ / (k+ + k-), k+: block on-rate, k-: block off-rate. To assess the congestion effect of the roadblock, we can look into plotting the mean site (i) occupancy  (X-bar) across multiple samples (j) at a given point in time (can also look into the variance). Since time intervals themselves are determined stochastically, that will probably involve finding a way to seed the time points. numpy.random.Generator() may be the solution if this is the way forward.
 
![3rd meeting about rini discussing implementation of the roadblock and plotting of average site occupancy](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rini_meeting3.jpg)

- Attended Edward's meeting. Edward added some details about what the model intends to stand for, especially that alpha is for the PIC assembly on the mRNA. Brought up that this step seems to be rate-limiting biologically. While I presented figures to compare density profiles over time, Edward asked how fast particles went along the lattice over time, which made me hypothesize SSA is 0.5x as fast as the cellular automaton looking at the difference in maximum initiation rates. This may pose an issue when it comes to comparing directly the models because time has a different significance from one algorithm to another. If I intend to formally make that comparison, I should introduce a time standard when plotting.

## Day 15 - 02/02
- Worked remotely to make progress on the literature review.

---
# Week 4 - 05/02 --> 09/02
- [ ] Finish the literature review.

For rini v0.3:
- [X] Implement a single roadblock in the model (=make rini v0.4).
- [X] Change the final time point to be exactly the time limit.
- [X] Present a plot of average site occupancy.
- [X] Improve the presentation of the phase diagram

## Day 16 - 05/02
- Forced the final time point to be at time=t.
- Changed the phase diagram by removing numbered labels and printed sentenced by colour coding points based on which density phase they belong to. Added a second figure plotting observed mean density (between time points of a run) against expected bulk density. Kept the phase colour coding and plotted a red segmented line to spot how far from the expected value results are.
- Started writing the roadblock in the model: added the relevant variables (block on and off rates, block length and list of blockable indicies). So far, the model creates a subconfiguration for blocks, adds propensities for block-related actions, and updates the dataset for the block configurations. The actions and propensity update conditions are still missing for the model to be functional.

![Phase diagram of 10 random and unblocked runs of rini v0.3b](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/phase_random10_v03.png)

## Day 17 - 06/02
- Succcesfully implemented the roadblock into the model. The sites affected and the length of the roadblock can be additionally customised. The model now assumes the tracking sites to be at the head of particles and roadblocks to simply the exclusion rule for blocking: Si -k_on-> Bi if no particle is present i-l_rb+1 sites downstream and i+l-1 sites upstream AND no block present i-l_rb+1 sites downstream and i+l_rb-1 sites upstream. In other words, this allows the restriction to only depend on the downstream footprint of the prospective block and the respective upstream footprints of eventual particles or blocks present ahead. This is compatible with all previous functions.
- Discussed the calculation of average occupancies with Ramon (see below). A: the consistency of time points from one run to another is not an issue, as time can be artifically made continuous. If we want to sample a density or occupation state at t=3, when the closest values are only at t=2.5 and 3.5: we can take the value that is still active at 3 i.e., the last that was computed before t=3, so the value from 2.5. B: The goal is to plot average occupancy against sites (i.e. against our 1-dimensional space).
- Noticed that the restriction rule for blocking is error-prone if the block is located less than l_rb-1 from the entrance of the lattice, placed an extra condition to avoid that sort of error. The model seemed to be behaving as expected with the parameters rini(t=10000,l=3,l_rb=2,B_i=[1,8,9,19,25]).

![Doodles of the discussion about average site occupancy at a given time point](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/average_occupancy_vs_site_060224.png)

## Day 18 - 07/02
- Asked Ramon what use there was to sample runs at a timepoint midway through rather than just restricting runtime to the desired time point. The answer seems to be for flexibility mainly.
- Completed the first function for average occupancy plotting and data extraction rinimo. Takes in the usual rini variables plus the timepoint to be sampled, the number of samples, and two booleans to control plotting and returning the dataset. Plotted with a block on site 20 out of 30, and another time without blocks (B_i=[]).
- Quickly added the plotting of red segmented lines over the sites that are blockable (if any are specified).
- Upon seeing the first two plots, Ramon was surprised by the discontinuity of the line and the fact there was seemingly a slight downward trend without blocks. Suggested increasing time and sampling. 5000 seemed to be in the steady state already though (wihout blocks, but should still be at MC, maybe not in HD). Pushed the time to the 10000 limit I have been defaulting and increased sampling from 100 to 1000. The downward skew persists. Defining B_i as an empty list seems to be preserving anomalies in the phase diagram. Further troubleshooting required.
- Double-checked how I wrote rini to see if there might be a skew between entrance and exit, but both the actions and the conditions should be working as intended. Maybe something to do with the code that involves blocks when B_i is an empty list? Looping through an empty list or a range based off of the list's length should just break the loop instantly, I don't expect any interference from that.
- Now that I know how to calculate averages at any given time point over multiple runs, I should improve the phase diagram to calculate that kind of average rather than merging every time point of a single run.

![First plot from rinimo showing average occupancy levels across the L30 lattice at t=5000; n=100, B20](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rinimo_b20_t5000_0-4.png)
![Fourth plot from rinimo showing average occupancy levels across the L30 lattice at t=5000; n=1000, no block](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rinimo_n1000_noblocks_0-4.png)

## Day 19 - 08/02
- Juraj thinks the occupancy decrease seems more important than it really is due to size effects (the lattice being short, on the order of 10^1). Two changes that can be made to seek better results: make it so that a = 1 - b (0.25 a and 0.75 b). OR increase lattice size to 100 or 200.
-  Tested the a = 1 - b with L=30 and n=200, Juraj was correct! The occupancy seems properly distributed throughout.
-  Tried also running the extended t=20000 + L=200, n=200 run but this would take a terrifying amount of time. With two minutes per iteration, we are looking at about 6 hours and 40 minutes of simulation.
- **IMPORTANT:** Discussed with Edward and Ramon the progress of the project. The model has proved its functionality, we can now start addressing the use of its parameters to reach a hypothesis on the required initiation dynamics for Ssd1 to produce the results Edward observed. When there are 0 blocks, protein production (exit current) is at a standard value of 1. 1 block site leads to a small 5% decrease, but TWO sites yield a 30% decrease (Edward will share more details next week). One of our end goals would probably be to compare a very simple model where exit current is proportional to blocking probability (to the power of n the number of blocks), to a version of the model that assumes independent binding, and finally with another that assumes COOPERATIVE binding (one way to do this would be to dynamically change k_on around the starting value based on the blocking landscape). Reminder, alpha should most likely be limiting (i.e., LD) in reality.
- For now the next step is to be able to plot a graph that matches Edward's figure (see below). Next experiments will depend on the state of the parameters we use to reach a simulation that shows a trend similar to the few experimental results already available.    

![Balanced average occupancies when a = 1-b mean the model works!](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rinimo_a%3D1-b_0-4.png)

![Ssd1 seems to feature a non-linear blocking efficiency as the number of blocking sites increases](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/meeting_080224.png)

## Day 20 - 09/02
-Tried to progress on the literature review, but with little efficiency. Had to take some time off for the theatre production, which required some immediate attention. Put the review at the top of my W5 priorities.

---
# Week 5 - 12/02 --> 16/02
- [X] Absolutely finish the literature review.

For rini v0.4:
- [X] Adjust the model's output to plot graphs that match previous Ssd1 data.
- [ ] Begin work on 0.5 = make a version that models cooperative binding. Model idea #1: a bound block increases the chance of block binding in its neighbourhood 

## Day 21 - 12/02
- Attempted to somewhat optimise the core model by resorting to numpy arrays for the configurations, but this quickly led many errors so I decided to put that idea on hold in v0.49. A sensible way to improve the model could be by adding arguments that decide what will be part of the final dataset (assuming the dataset appending is limiting).
- Made the function rini_INIvBLOCK that plots a standardised exits vs. blockable site count profile. This takes values from n runs displayed as a mean with an sd error bar. With the default L=30, l and l_rb =1, n=10, and t=5000, I found that at Pb=54.8% and blocks=2, we get about 0.7 efficiency like with Edward's results. However, block1 was below 0.8 (see figure)=difference of about 0.1 between b1 and b2. I then proceeded to play with the lattice size, and noticde that more than tripling it (L=100) brought little change to the result. Further increasing particle length to 3 however did lower the distance between b1 and b0, but b1-b2 is about the same. l=6 led to the same observation, although b1-b2 might have been somewhat lowered as well. (the standard deviations do not enable any further interpretation as they seem to get bigger, playing with particle sizes seems to interact with the restriction rules in a way that increases the stochasticity from one run to another?). In a scenario where L=200, l=12 and l=2, the distance b0-b1 is now clearly smaller than b1-b2;b1~3% drop in efficiency, however b1-b2 is too small.
- After looking at L, l and l_rb, I tried observing what was happening with more than 2 block sites (i.e. up to 5, regularly interspaced blocks). In the initial default scenario with Pb=54.8%, we get again b2~0.7, and the distance between subsequent blocks seems to be halved one block after the other: the more blocks, the lesser the impact of adding another site. In the L=200, l=12 and l_rb=2 scenario, there is also a decrease in impact as blocks are added, but the trend is a bit more inconsistent (adding 3 didn't really change the curve); even then, the maximum efficiency drop does not go below 0.85 with 5 blocks.

 ![First initiation efficiency v. block sites profile where b2=0.7 as expected](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rini_inivblock_0-4.png)

## Day 22 - 13/02
- Pb is interesting as it describes the difference from kon and koff, but close these values are to 1 or 0 also matters. Pb may be the same, but the block distribution over time would be different? (high rates: more sporadic and more likely to be blocked by particles, low values= if a block binds, it will stay for longer with no factor controlling its presence except itself). Would need to establish another measurement to characterise this?) Lower absolute values will in general have a higher impact on initiation efficiency  due to this. Probably some time dependence if the values get too close to 0?
- Continued testing what variations do, but realised that it's hard to trace the results by constantly tweaking things differently. I should set a default standard and record the list of changed variables and how this affects the profile.
- Looked for potential sources of inspiration in how to define corini (the cooperative blocking version of rini). Added the corresponding bibliography section. No matter what, it seems like changes in propensities in a block's neighbourhood would be a good start.

- __List of rini variables and their effect on the initiation efficiency to blocks profile:__
_NB: default parameters = t=5000, L=100, l=1, a=0.6, b=0.6, p=1, k_on=0.5, k_off=0.5, l_rb=1, B_i=[49, 74], timepoint=5000, n=10_
Observables: distance b0b1 (default=0.125), distance b1b2 (default=0.025).
    1. t: double time = doesn't seem to make a difference here, sd values are visibly a bit lower 
    2. L: half length =  **b1b2*2**; double length = b0b1 - 0.01 
    3. l: l=3 = **b0b1/3**, b1b2~c
    4. a: a=0.3(LD) = b1b2=0.01 > b0b1=0.005 BUT the overall effects are noticeably diminished  ; a=0.9 = no changes
    5. b: b=0.3(HD) = b1b2=b0b1=0.01 ; b=0.9 = no changes
    6. p:NOT TESTED
    7. k_on & k_off: k=0.25(Pb50) = b0b1x1.2 > __b1b2x2__; k=0.75(Pb50) = b0b1x0.8 ; Pb25 = b0b1x0.15 > b1b2x0.3. ; Pb75 = b0b1x3.3 >> b1b2 (about the same if not smaller)
    8. l_rb: l_rb=3 = b0b1/7, b1b2*0.6
    9. B_i (number of blocks and successive locations): adding a block at the 25th site didn't change the profile up to b2.The location of the block likely doesn't matter in an independent roadblock model (unless they are so close steric hindrance is possible from one block to another.
    10. timepoint(sampled time, can be below t): NOT TESTED
    11. n (run sampling): NOT TESTED
- Fill the list when possible but testing l_rb =3 made it obvious something is not right with the exclusion rule for scanning (most likely), tied to l_rb. First revise the code to guarantee flexibility for l_rb. Found the issue: problem occurs when l_rb > l, can be fixed easily be rewriting the exclusion rule. Fixed with a token system.
- Showed Ramon the first look at the efficiency vs block profile. He seems pleased with the method and noted the results are about what he would expect from independent binding. The next step should be to prepare a cooperative version of the TASEP. He noted since we don't really know how the cooperativity is supposed to happen, it would probably be more elegant and simple to let a block binding event affect the probability of the next temporally only.

## Day 23 - 14/02
- Finished the test runs for the independent model and filled the list above. Went home early to start preparing the seminar practice presentation.
- Next week will be dedicated to making a cooperative roadblock algorithm (corini).

## Day 24 - 15/02
- Discussed my time management of the review. Edward suggested I dedicate whole days to just the literature review to properly sit down and complete the write-up.
- We are now moving forward with two aspects of the modeling: testing the independent hypothesis, and testing the cooperative hypothesis. Based on my early results, it looks like independent blocking does not satisfy Edward’s observations. Hypotheses:
  1. Independent: adjust the efficiency vs blocks to display normalised flux (passed/time) in boxplots (w/median and interquartiles). Will need to establish a solid range of result comparison between variable changes.
  2. Coop: code a version where block binding increases binding of the next. Finding one example that match Edward’s data will be sufficient. An important point of discussion will be how we scale the Lattice, particle and defect lengths.

- Edward asked me to make a summary figure that exposes the hypotheses we are testing.
- He also shared his flow cytometry analysis, now I have the exact figures to work with! Normalisation should therefore be made over time and based on the MEDIAN of 0-block.
- Changed rini_INIvBLOCK to use median standardisation instead of mean and change the plot from point to box (colorblind palette). This helped me compare what the model can currently do vs Edward's results.
- Edward was happy with the sketch I made, the question now is how to define the cooperative factor: an increase or decrease of k+/k- respectively? Is there a local effect? Is the effect lattice-wide? If local, is the condition for the effect just block presence itself? I will most likely have to test different approaches, but should keep a progression that goes from simple to complex and not try things on a whim.
- Finally, Edward made me notice the scale from his figure is on a log2 scale as opposed to mine.

- Based on Edward's cytometry data, the precise experimental values on standardised protein production efficiency are:
   1. 0 sites: 1.01
   2. 1 site: 0.959
   3. 2 sites: 0.741
  
[Link to the html cytometry result file preview](https://htmlpreview.github.io/?https://github.com/gabin-rousseau/ReporterFlow2021/blob/main/Rmd/FlowAnalysis_2021-12-14.html)

![Edward's flow cytometry results](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/edward_flowcytometry_rini.png)

## Day 25 - 16/02
- Worked on the litterature review.

---
# Week 6 - 19/02 --> 23/02
- [X] Improve the INIvBLOCK figure with median distances.
- [X] Prepare corini v0.6 - a cooperative version of the model where roadblock binding increases binding of subsequent blocks. Local effect with a customisable area of effect and effect strength. 

## Day 26 - 19/02
- Submitted the literature review.

## Day 27 - 20/02
- Adjusted the figure to visualise the distance between successive medians by plotting black segmented lines and printing the corresponding distance (e.g. b0b1) rounded to 2 significant figures.
- Made the first version corini (v0.6), that takes as new user input coop_p and coop_m, which together determine the strength of the cooperativity by increasing k_on when there are particles already present before binding, or decreasing k_off likewise when bound respectively. Coop_d is a distance factor that allows the user to customize an l_rb dependent area of effect for cooperativity (i.e. if coop_d=1, cooperativity will be effective at sites i +- (l_rb + coop_d) if one other block if found in that neighbourhood.). Cooperativity isn't cumulative: the presence of a single other block in the area of effect will trigger the full effect available, more blocks won't change this.
- Corini require some time spent on rewriting the restriction rules behind block propensity updates, as I noticed the first draft seemed to working improperly (twice as slow as expected). The issue lied in conditional ranges: when calculating off-rates the central block for which the propensity is calculated was at first counted towards the cooperativity effect, which caused this issue. Now fixed.
- To test the value of this model against the original independent blocking rini, I started plotting rinimo and INIvsBLOCK plots for certain scenario for both models, varying the number of blocks and their position respectively:
  1. default parameters:   t=10000, L=100, l=1, a=0.75, b=0.75, p=1, k_on=0.5, k_off=0.5, l_rb=1, B_i=[48, 49, 50],coop_p=0.4, coop_m=0.4, coop_d=1, timepoint=10000
  2. test#1 : rinimo no block
  3. test#2 : rinimo 1 block (50)
  4. test#3 : rinimo 3 blocks (default)
  5. test#5 : INIvBLOCK distant blocks (25, 50, 75)
  6. test#6 : INIvBLOCK neighbour blocks (49,50,51)
(focus on INIvBLOCK due to time constraints)

![First comparison between the independent and cooperative v0.6 models, showing plots where the distance between three blocks varies from 25 to 1](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/distance_vs_cooperativity_0-6.png)

## Day 28 - 21/02
- After quickly discussing the figure above with Edward, he noted the figure alone wasn't enough for an audience to understand, and that harmonising the y axis would also be important. Introducing this figure and talking over what it means is the end goal of tomorrow's presentation. Cooperativity happens in a fairly simple manner: if a block is in the designated area of effect, cooperativity is active, i.e, a single change to the probability of block binding and unbinding is applied when the conditions are fulfilled. In other words, the model doesn't consider cooperativity as a cumulative phenomenon (doesn't scale with the number of blocks in the area of effect), nor does it scale on the position of other blocks in the area of effect (no decay over the distance). These are things that we can take into account for further testing.
- **IMPORTANT**: this isn't problematic for now, but checks for cooperativity are error prone if i-(l_rb*coop_d)+1 < 0. I should change the indenting of conditions to prevent errors due to unintended index listing). Made a code fix, to be verified once the figures have finished generating. **VERIFIED**
- To address this, I regenerated figures with the same parameters with homogenised y axes and also made companion rinimo figures to visualise the impact of the blocks on particle occupation throughout the lattice. (about an hour and 40 minutes of wait... I should use less time-consuming parameters (time and lattice length mainly) when testing things other than these variables). Also made a rinimo figure w/o blocks, with one block, and an additional comparison for 2 blocks (rinimo n=50, IvB n=10).
- I note that in the corinimo close blocks figures, if I increase the area of effect for the same block site distribution, the third might have an even bigger impact as bloc 49 and 51 would also affect one another. Maybe but the distance increase from two is just by an additional 0.05 or so, so quite low. (compared three close blocks of l_rb=1 at coop_d=2). Also, the INIvBLOCK results are very very similar from the main figures showed below despite small, L(20), t(500) values.

![boxplots of roadblocking vs cooperativity](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/distance_vs_cooperativity2.png)
![rinimos of roadblocking vs cooperativity](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/distance_vs_cooperativity2bis.png)

## Day 29 - 22/02
- Very interesting discussion with Ramon and Edward over the lab meeting. Points of action by priority:
   1. Get some figures out of a maximally corsegrained format (L=5, B_i=[1,2,3], l=1, l_rb=1).
   2. Write about the cooperativity formalism choice: express the logic as a set of reactions (that would directly count in the Gillespie algorithm) to discuss my use of conditions. (as reactions would be a standard way to do this). Don't necessarily change the code, discuss and put the reaction logic down on paper.
   3. Work on a parameter space benchmark function for the ?coarsegrained model?. Look up functions to do parallel processing on python (possibly use the lab server or EDI). Make sure parameter sets can be extracted from each time point because...
   4. ... I should then use these parameters for post-analysis to see if there are any trends in high scoring parameter sets (e.g. is one variable always inferior to another?)
   5. ... and after isolating high scoring parameter sets, I can also test these on longer lattices or more specific configurations etc.
   6. Another goal (priority pending) would be to **profile** my code and isolate which steps are the most time consuming, before checking if I can optimise.
- Presented the mid-project talk at Edward's lab meeting, new presentation coming at Ramon's meeting on March 7th. Twice as long as should have been, can be significantly cut down by planning a concise way to talk through the slides at the real seminar.
- Questions:
    1. what are my predictions for the mechanism of Ssd1 cooperativity? A way to experiment on it? =Edward suggested we can still formulate the parcimonious hypothesis that Ssd1 units interact directly on contact (floppy N-terminal?), another question could be can they interact before binding RNA or does the cooperativity manifest on the mRNA? Not very keen on testing the cytosolic interactions with this model, since I can only look at the dynamics surrounding the lattice. Ssd1 complexes would mean secondary types of defects that REQUIRE sufficient number of sites (or do they?).
    2. After explaining what the parameters mean, unnecessary although appreciated by some to detail the default variables: just explain what is being compared. That apparently also confused Edward when I introduced the boxplots.
    3. What is the typical distance between Ssd1 motifs?
    4. What happens when I vary block binding/unbinding rates (outside of cooperativity)?
    5. Were TASEP models originally used by biologists?
    6. Is Ssd1 found in other organisms beyond cerevisiae? [Is there data from these organisms that could change the way we look at the model?] =S. cerevisiae is the model organism for Ssd1, it's mostly just KNOWN to be used in other fungi.
    7. Should introduce the TASEP separately from blocking rather than on the same slide.
    8. When talking about occupation profiles, Edward's recommends a stronger focus on comparing 0, 1, 2 to 3 blocks, otherwise it's harder to interpret these.


![Model doodle](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/TASEP_explanation_2202.png)
![Parameter doodle](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/parameter_description_2202.png)

- Edward's comments on Ssd1 distribution data in 5'UTRs: the section "Plot pileup on SUN4 5’UTR to show reproducibility" Shows that there is a roadblock motif at position 150 and 180, roughly. By contrast, UTH1 has roadblock motifs at roughly positions 30, 95, 125, 160, 190 (estimated by eye). And so on. So we'll have to discuss what level of coarse-grained/detail to model these at.
[Link to Edward's Ssd1 site spacing data in native UTRs](https://htmlpreview.github.io/?https://github.com/ewallace/Ssd1_CRACanalysis_2020/blob/v2.1/rmarkdown/pileup_Ssd1_closeup.html)
---
# Week 7 - 26/02 --> 01/03
- [X] Make figure observations for the maximally coarsegrained parameter set.
- [X] Write the block cooperativity logic down as a reaction system in order to approximately described what the model is currently doing (despit not relying on reactions i.e. separate Gillespie propensities).
- [X] Write rini v0.7, with a new function to test parameter sets.

## Day 31 - 26/02
- Got started with Quarto, which I intend to use for the final report write-up.
- Made boxplots for the model under the lattice format: (L=5, B_i=[1,2,3], l=1, l_rb=1), it looks like the initiation efficiency effects mostly remain consistent in the coarse format, should be useable in the parameter space test!
![Coarse independent trial](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/independent_coarse_trial.png)
![Coarse cooperative tril](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/cooperative_coarse_trial.png)

- IMPORTANT: just a couple of tweaks led to a result that nearly matches Edward's result. The following figure was obtained with the parameters: (**t=10000**, L=5, l=1, a=0.75, b=0.75, p=1, **k_on=0.06**, k_off=0.5, l_rb=1, B_i=[1, 2, 3],coop_p=0.4, coop_m=0.4, coop_d=1, **n=100**)
- Here, the modeled values of standardised initiation efficiency / protein production are:
  1. 0 sites: 1.00 (standard)
  2. 1 site: 0.948 (1.2% difference)
  3. 2 sites: 0.718 (3.2% difference)

![first_match: the very first match obtained from the model in comparison with Edward's flow cytometry data](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/first_match.png)

## Day 32 - 27/02
- Practiced LaTeX mathematical and chemical equation syntax to use on Jupyter, and wrote 4 summary equations to describe blocking/unblocking reactions, including in a cooperativity context. (see figure below)
![Summary reactions for the cooperativity model of blocking](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/cooperativity_reactions.png)

- [Using the Pool class from the multiprocessing Python library](https://www.sitepoint.com/python-multiprocessing-parallel-programming/) seems like the most approachable way to permit parallelisation of parameter space computing.
- Parameter space function concept (2 variants rini_paramspace and corini_paramspace):
  1. Input: t=1000, L=5, l=1, p=1, l_rb=1, B_i=[1,2,3], n, visual=False, dataset=True // specify the default parameters that won't be randomised i.e. time and lattice settings, n as the number of parameter sets to run through, visual dictates whether a plot of the output is to be generated, dataset dictates whether the output is returned.
  2. Contents: the function should generate a list of rini_INIvBLOCK argument tuples of length n where the rates a, b, k_on, k_off and coop parameters are randomised in a way fitting the parameters' boundaries (rates vary from 0 to 1 uniformly, coop_d varies between 1 and 2?). This can be passed onto a multiprocesses Pool class object as a starmap, allowing for parallel processing of the runs required. The pool processing would return a list of results which can be used to finalise the output.
  3. Output: a dataset showing for each parameter set: its ID, all of the parameters, a score of similarity to experimental data S: the mean of the individual similarity scores s1 and s2 1-|1-(model/experimental)| for the 1 site and 2 site values: the closer the score is to 1, the better the model result.
  4. CONSIDERATIONS:  coop_p/m will be a problem as in a randomised scenario this may cause nonsensical on and off rates for the blocks (e.g. negative off values): should place a limiter condition. Score calculation should rely on median standardised values of initiation efficiency from rini_INIvBLOCK, an extra argument should be added to that function in order to let it output just these two values (1s median and 2s median) for ease of interpretation.
 
- Added in corini a coop parameter limiting step to make sure intended boundaries are respected. Added the comparison_output argument to INIvBLOCK that leads to returning the 1s and 2s medians as a tuple. This can be used in the starmap.

## Day 33 - 28/02
- Completed the first version of the parameter space function. I discovered by working from home that multiprocessing worked really badly on windows couple with jupyter unless the working function used in parallel is imported. Made a rinipy.py file to easily import rini, corini and their respective INIvBLOCK functions (rin or cib).
- The following two figures were obtained with the parameters t=500, L=5, l=1, p=1, l_rb=1, B_i=[1,2,3], n=50, n_ivb=10, visual=False, dataset=True:
![First parameter space of the independent model](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/rini_space1.png)
![First parameter space of the cooperative model](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/corini_space1.png)

## Day 34 - 29/02
- Discussed the results with Edward and Ramon. Action points:
   1. Change the formalism of the cooperative model to make cooperative block dynamics the result of separate Gillespie actions as described in the reactions I drafted this week.
   2. Make sure the scale of each axis are the same (1:1 instead of 1:2)
   3. Reformulate the scores we're interested in: s1 and s2 should just be the absolute errors model-experiment, and S the rms sqrt((s1^2 + s2^2)/2). Suggested to simplify the plot by only looking at the variations for one variable at a time so that I can plot S over the variations of these parameters. Maybe highlight the best 5 points. Two other significant plots would be to show for 1s and 2s respectively the model median vs experimental median.
   4. Send figure drafts/sketches to Edward/Ramon before next Thursday to ensure I am working with the right ideas.
   5. Produce some boxplots to visualise the results in parameter sets of interest, add lines to show experimental medians as well.
- The strength of the model is it provides parameters that should make sense experimentally, and while we lack experimental data, we are in a good place to produce interesting predictions about what parameters can be best associated with existing results, as well as predict what other block sites (e.g. a third) would lead to under certain assumptions (i.e. cooperation vs. independence).

- The independent model yielded surprisingly high scoring parameters, although I noticed there seemed to be a limit around the 90-95% similarity mark that the cooperative model isn't affected by. I also noticed some points produced a division by zero error due to standardisation using 0 as the denominator (median of absolutely 0 succesful exits), while other outliers lied in the negative range (either the model median is negative or way higher than expected), which is part of the reason why I should just simplify my measurements. Likewise many points in the cooperative model fall to zero because of cooperative effects (namely coop_m). With these obvious outliers, Ramon noted it is also possible that some points that look fine may also contain parameter values that are biologically nonsensical. As a result, **I should probably be careful with how many parameters I vary at once and over which ranges I allow them to be varied: start wide, but then hone in on better values.**

---
# Week 8 - 04/03 --> 08/03
- [ ] Update the cooperative formalism to an extra set of Gillespie propensities in rini v0.8.
- [X] Make the parameter space figure scaling 131 instead of 121.
- [X] Make s1 and s2 absolute errors, S the rms of s1 and s2.
- [X] Make a concept set of plots showing S vs k_on alongside 1s and 2s model vs expected median values. Send to Ramon and Edward for feedback.
- [ ] Highlight the top 5 points in the S plot.

## Day 38 - 06/03
- Changed the paramspace function to allow for an easier selection of parameters to randomise (set desired randomisables to None by default and give a proper default value to the rest). Because of the increased amount of input though, the function takes about 50% longer than before (still about 0.1 it./s). Turned s1 and s2 into absolute errors, S is now the rms of s1 and s2.
- Generated the three concept figures with 1000-fold k_on randomisation (boundaries: 0 to 1) with the default parameters: t=500, L=5, l=1, p=1, l_rb=1, B_i=[1,2,3], n=10, n_ivb=10, visual=False, dataset=True, a=0.75,b=0.75, k_on=None, k_off=0.5,coop_p=0.4,coop_m=0.4,coop_d=1
- Also plotted boxplots for the  best parameter sets that appeared in the figures below, but this would be more interesting once I have rewritten cooperation.

![indespace1](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/indespace1_kon.png)
![coopspace1](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/coopspace1_kon.png)

- I'm quite confident I properly adapted the code to have cooperative block dynamics as separate reactions but I want to revisit the meaning of having them be compatible with base blocking propensities. Taking the example of cooperative unbinding two propensities (k_on,k_on-coop_m) could lead to the same result, but doesn't that defeat the purpose of the effect? I asked Ramon about it, comparing this to having the block being able to unbind on its own in addition to being rarely knocked off by some other particle, whereas the idea is a particles together can't unbind as easily.

## Day 39 - 07/03
- distinguished the function above (formerly plot_paramscore, now paramsolo) that is better suited to assess randomisation of just one parameter with a second one, plot_paramulti, that plots s2 vs s1.
- Presented the mid-project slides at Ramon's meeting. Ramon brought up that the rates (k-- and k--) were confusing on the TASEP slide, and recommended elaborating further on the model. Maybe introduce the main concept of the model, then talk about the Gillespie algorithm ("We have a set of possible actions at any given time, a particle entering, a particle moving... and you throw two dice! One to tell which action will happen, the other to determined how long it will take until the next action happens (the range of possible values for this time interval depend on how many actions are possible and how likely they each are to happen, just like the first die). Ramon didn't catch on to the fact that I used the coarsegrained model despite the sketch I added. Ramon noted the behaviour of the cooperative model looked weird at 3 blocks because the effect was closer to the addition of the first block. The answer is that the effect isn't cumulative which translates poorly in further addition of block sites. We don't enough data to really inform the format any further but that would typically be the approach; I added that it would be simple to express that in my model and it that it will probably become something worth considering as an alternative when data for more than two sites is in.

![indespace1b](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/indespace1b_kon.png)
![coopspace1b](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/coopspace1b_kon.png)

- Met with Ramon about the project. Discussed the way I deal with the independent and cooperative reactions, the figures I generated for the parameter space and what I can do to make progress on the parameter space thanks to realistic boundaries for the parameters varied.
    1. **Gillespie reactions**: Ramon agrees that they should be incompatible to simplify interpretation.
    2. **Figures**: Ramon prefers the s2 vs s1 figure for a multi-purpose use.
    3. To generate points that have a chance of making sense relative to the biology, it is now time to think about setting boundaries for the rates. First comes assessing what model time means in real time: as p=1, I rely on maximal ribosome scanning speed in nt/s vs the model speed to get a conversion scale (careful, might be a difference in speed from elongating to scanning, the value in the book that Ramon lent me, _CELL BIOLOGY by the numbers_ by Ron Milo _et al._, is for elongating ribosomes). Following that, I should read about initiation rate and protein production to get estimates for alpha and beta. If possible, I should also reason about block rates and cooperativity effect; for instance, Ramon said that since the dogma is that initiative binding is the rate-limiting step, the effective binding probability of the block shouldn't get too high (say 30%).

- First lead at page 232 of the book:

- Careful note: the S. cerevisiae value was obtained at 30C, as opposed to 37C in E. coli (expected to be faster under the same temperature, look up Q10). In mice, the speed seems to be 6 aa/s = ~20nt/s.

![page232](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/page232.jpg)

---
# Week 9 - 11/03 --> 15/03
### On hiatus while the theatre show  I produced unfolds.

---
# Week 10 - 18/03 --> 22/03
- [X]  Fix again corini so that the separate base/cooperative Gillespie actions are exclusive to one another: one's propensity is up if the other's condition isn't validated, basically.
- [ ]  Establish a conversion standard between real time and model time based on the real-life equivalent of p.
- [ ]  Draft a boundary idea for all rate variables grounded in known data such as page 232.

## Day 40 - 20/03
- Succesfully updated the corini formalism so that cooperation is considered as separate reactions, while preserving exclusivity (if cooperative blocking is possible, independent is no longer considered for as long as cooperation remains possible at that site.) When it comes to blocking/unblocking, the propensity for an executed action is set to zero immediately while updating the propensity of one reaction to above 0 nullifies that of the opposite reaction in terms of cooperativity (e.g. cooperative unbinding selected means erasure of independent unbinding until the cooperative conditions are no longer fulfilled).
- Found 2 papers that are relevant to time comparison:
  1. [Dynamics and processivity of 40S ribosome scanning on mRNA in yeast; Berthelot et al.; 2003](https://doi.org/10.1046/j.1365-2958.2003.03898.x): suggests an average scanning rate in yeast of 10nt/s at 26C. (recommended by Edward).
  2. [Computational resources and strategies to assess single-molecule dynamics of the translation process in S. cerevisiae; Magalhaes et al.; 2019](https://doi.org/10.1093/bib/bbz149): only looks at general initiation rate but also highlights its relationship with elongation, which might help with defining boundaries.
  3. [Unidirectional constant rate motion of the ribosomal scanning particle during eukaryotic translation initiation; Vassilenko et al.; 2011](https://doi.org/10.1093/nar/gkr147):"The scanning rate is of the same order of magnitude as the movement rate of translating ribosome."
  
## Day 41 - 21/03

---
# Week 11 - 25/03 --> 29/03
- [ ] 

---
# Week 12 - 01/04 --> 05/04
- [ ] 

---
# SPRING BREAK - 08/04 --> 19/04
- [ ] Prepare the first report draft for review by Edward and Ramon.
 
---
# Week 13 - 22/04 --> 26/04
- [ ] 

---
# Week 14 - 29/04 --> 03/05
- [ ] 

# END OF PROJECT












