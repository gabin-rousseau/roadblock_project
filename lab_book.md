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
## Day 10 - 26/01 
