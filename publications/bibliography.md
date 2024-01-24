# Project Bibliography
### Project: Computer simulation of a roadblock model of translational control
### Author: Gabin A. M. Rousseau
---
## Starting references:
- [Beyond the triplet code: context cues transform translation
GA Brar, Cell, 2016](http://doi.org/10.1016/j.cell.2016.09.022): Translation initiation can be triggered by non-canonical signals like RAN. 5' methylated adenines can mediate recruiting the translation initiation factor eIF3, skipping cap-binding by eIF4E.
- [Physical and Mathematical Modeling in Experimental Papers
W. Möbius and L. Laan, Cell, 2015](http://doi.org/10.1016/j.cell.2015.12.006): guidelines on the decision to model in addition to exclusive experimentation.
- Translational control review : [Gebauer, F., Hentze, M. Molecular mechanisms of translational control. Nat Rev Mol Cell Biol 5, 827–835 (2004)](https://doi.org/10.1038/nrm1488):IRP binding blocks the recruitment of the 43S complex to ferritin mRNA that is engaged with the eIF4F complex, interfering with the formation of the PIC before scanning can progress; hnRNP-K–hnRNP-E1 targets the initiation factors rather than the ribosomal subunits themselves (inhibit 60s recruitment in late initiation).
- Edward's review on translational/post-transciptional control (incl. Ssd1) : [Post-transcriptional control of fungal cell wall synthesis
Hall RA, Wallace EWJ, The Cell Surface (2022)](http://doi.org/10.1016/j.tcsw.2022.100074)

## Juraj's recommended publications to understand TASEP in the context of translation
- [MATHEMATICAL AND COMPUTATIONAL MODELLING OF RIBOSOMAL MOVEMENT AND PROTEIN SYNTHESIS: AN OVERVIEW; T. Haar; 2012](https://doi.org/10.5936/csbj.201204002): "Characteristics of early versions of the TASEP include assumptions of limitless ribosome-supply, a single, uniform elongation rate-constant along the mRNA, and a coarse-grained description of the elongation process, which is simply regarded as a “hopping-probability”. Recent modifications to the basic TASEP allowed analyses of codon-specific elongation rates [26, 27, 28, 30, 33], limiting supplies of ribosomes [31, 37, 38] or tRNAs [35], and traffic on circularised mRNAs [25], thus making the approach more physiologically relevant. Several recent studies also described approaches that go beyond the description of ribosome movement as a simple hopping probability, and instead consider the detailed sub-steps of the translation elongation cycle [29, 32, 33, 36, 39]."
- [mRNA translation from a unidirectional traffic perspective; Shyam, Sharma; 2023](https://doi.org/10.48550/arXiv.2312.12062)
- [Analysing GCN4 translational control in yeast by stochastic chemical kinetics modelling and simulation; You _et al._; 2011](https://doi.org/10.1186/1752-0509-5-131)
- [Stochastic scanning events on the GCN4 mRNA 5’ untranslated region generate cell-to-cell heterogeneity in the yeast nutritional stress response; Meng _et al._; 2023](https://doi.org/10.1093/nar/gkad433)
- (old paper about the mRNA scanning mechanism) [Dynamics and processivity of 40S ribosome scanning on mRNA in yeast; Berthelot _et al._; 2003](https://doi.org/10.1046/j.1365-2958.2003.03898.x)

## Edward's recommended publications to get an overview of translation **initiation** modelling
- [Control of translation initiation: a model-based analysis from limited experimental data
Richard J Dimelow  and Stephen J Wilkinson
JOURNAL OF THE ROYAL SOCIETY INTERFACE 2008](https://doi.org/10.1098/rsif.2008.0221):we suggest that the rate of translation initiation is most strongly influenced by one of two reactions: either the guanine nucleotide exchange reaction involving initiation factors eIF2 and eIF2B or the assembly of the multifactor complex from its constituent protein/tRNA containing complexes. ... We approximate [initiation] as consisting of 12 key reactions and make the assumption that all eIF2 molecules are bound to GDP or GTP. ... All reactions were modelled using reversible mass-action kinetics, apart from reaction 12 [(final assembly of the ribosomal complex and start codon identification, resulting in translation)], which was assumed irreversible.
![Figure 2 Rate of protein synthesis versus initiation factor concentration for (a) eIF1A, (b) eIF4E, (c) eIF4G and (d) eIF5B. The graphs show the experimental data points (diamond) and model-predicted values (solid line).](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/51fig2.jpg)
- [TASEP modelling provides a parsimonious explanation for the ability of a single uORF to derepress translation during the integrated stress response
Dmitry E Andreev et al.,
eLife 2018](https://doi.org/10.7554/eLife.32563): What designates some uORFs as providers of stress resistance? To explore this, we developed a simple stochastic model of Initiation Complexes Interference with Elongating Ribosomes (ICIER) that is based on the Totally Asymmetric Simple Exclusion Process (TASEP). ... In ICIER, we represent scanning and elongating ribosomes as two separate types of particles with different dynamic properties, with the possibility of transformation of one into the other at specific sites. The parameters used for the modelling were based on estimates from experimental quantitative measurements of mRNA translation in eukaryotic systems.
![The ICIER model distinguishes scanning ribosomes from elongating ribosomes in a TASEP framework](https://iiif.elifesciences.org/lax/32563%2Felife-32563-fig1-v2.tif/full/1500,/0/default.jpg)
- [Biologically motivated three-species exclusion model: Effects of leaky scanning and overlapping genes on initiation of protein synthesis
Bhavya Mishra and Debashish Chowdhury
Phys. Rev. E 100, 022106 – Published 6 August 2019](https://doi.org/10.1103/PhysRevE.100.022106): because of “leaky” scanning, a fraction of the scanning subunits miss the target site and continue their search beyond the first target. Sometimes such scanners successfully identify the site that marks the site for initiation
of the synthesis of a different protein. In this paper, we develop an exclusion model with three interconvertible
species of hard rods to capture some of the key features of these biological phenomena and study the effects of
the interference of the flow of the different species of rods on the same lattice. More specifically, we identify
the mean time for the initiation of protein synthesis as appropriate mean first-passage time that we calculate
analytically using the formalism of backward master equations.
- Complex recent paper combining model and experiment : [Li, K., Kong, J., Zhang, S. et al. Distance-dependent inhibition of translation initiation by downstream out-of-frame AUGs is consistent with a Brownian ratchet process of ribosome scanning. Genome Biol 23, 254 (2022).](https://doi.org/10.1186/s13059-022-02829-1)

## Translation initiation mechanism
- [Mechanism and Regulation of Protein Synthesis in Saccharomyces cerevisiae; Thomas E Dever,   Terri Goss Kinzy, Graham D Pavitt; Genetics, Volume 203, Issue 1, 1 May 2016, Pages 65–107](https://doi.org/10.1534/genetics.115.186221)
- [Translation initiation by cap-dependent ribosome recruitment: Recent insights and open questions
Nikolay E. Shirokikh, Thomas Preiss
WIRES RNA
First published: 06 April 2018](https://doi.org/10.1002/wrna.1473)
## Eukaryotic RNA scanning discovery
- [Point mutations define a sequence flanking the AUG initiator codon that modulates translation by eukaryotic ribosomes
M Kozak, Cell 1986
PMID: 3943125](https://doi.org/10.1016/0092-8674(86)90762-2 )

## Ssd1, RNA binding and translation initiation
- Showed that Ssd1 binds RNA: [Ssd1p of Saccharomyces cerevisiae Associates with RNA
Uesono et al., JBC 1997](https://doi.org/10.1074/jbc.272.26.16103)
- Mapped Ssd1 binding targets and found motif in 5'UTRs: [Diverse RNA-Binding Proteins Interact with Functionally Related Sets of RNAs, Suggesting an Extensive Regulatory System
Daniel J Hogan, Daniel P Riordan, André P Gerber , Daniel Herschlag , Patrick O Brown
PLoS Biology, 2008](https://doi.org/10.1371/journal.pbio.0060255)
- Showed that Ssd1 regulates translation: [Cbk1 Regulation of the RNA-Binding Protein Ssd1 Integrates Cell Fate with Translational Control
Jaclyn M. Jansen, Antony G. Wanless, Christopher W. Seidel,2 and Eric L. Weiss
Current Biology, 2009](https://doi.org/10.1016/j.cub.2009.10.071)
- Mapped Ssd1 binding targets precisely, found precise motif in 5'UTRs and verified it in vitro. (Our paper!): [Yeast Ssd1 is a non-enzymatic member of the RNase II family with an alternative RNA recognition site
Bayne et al., Nucleic Acids Research, 2022](https://doi.org/10.1093/nar/gkab615)
---
## Python application of TASEP
- [TASEPy: a Python-based package to iteratively solve the inhomogeneous exclusion process; Ciandrini _et al._; 2023](https://doi.org/10.48550/arXiv.2308.00847)

## 43S footprint on mRNA (30bp protected)
- [Preinitiation Complex Loading onto mRNAs with Long versus Short 5′ TLs; Weiss _et al._; 2022](https://doi.org/10.3390%2Fijms232113369)

## TASEP phase diagram
- [Nonequilibrium Steady States of Matrix Product Form: A Solver's Guide; R. A. Blythe, M. R. Evans; 2007](https://doi.org/10.48550/arXiv.0706.1678)
- [Rényi entropy of the totally asymmetric exclusion process; Anthony J Wood et al 2017 J. Phys. A: Math. Theor. 50 475005](http://dx.doi.org/10.1088/1751-8121/aa90fe)
![TASEP phase diagram and the expected steady-state densities for each phase type](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/phase_diagram_densities.jpg)
- [An Exact Formula for the Statistics of the Current in the TASEP with Open Boundaries; Alexandre Lazarescu, Kirone Mallick; 2011](https://doi.org/10.48550/arXiv.1104.5089)
![Another TASEP phase diagram showcasing expected bulk densities and current values depending on the active phase](https://github.com/gabin-rousseau/roadblock_project/blob/main/images/TASEP_phasedensities2.png)

## TASEP with defects
- [Totally asymmetric exclusion process with site-wise dynamic disorder; Warclaw _et. al_; 2019](https://doi.org/10.1088/1751-8121/aafb8a): We propose an extension of the totally asymmetric simple exclusion process (TASEP) in which particles hopping along a lattice can be blocked by obstacles that dynamically attach/detach from lattice sites.
