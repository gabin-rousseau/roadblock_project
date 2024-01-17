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
- ## Day 3 - 17/01
