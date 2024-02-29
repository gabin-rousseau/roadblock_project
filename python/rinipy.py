#rini dependencies
import matplotlib.pyplot as plt

import numpy as np


import seaborn as sns
sns.set_theme(style="whitegrid", palette="colorblind")

import pandas as pd

#rini_AvB dependency
import statistics

#to wrap around iterables to display a progress bar
from tqdm import tqdm


#Core function for the model
def rini(t=100, L=30, l=1, a=0.75, b=0.75, p=1, k_on=0.5, k_off=0.5, l_rb=1, B_i=[19]):
    '''
    
    roadblock_ini v0.7
    (rini for short)
    
    DESCRIPTION:
    This is the 0.7 version of Gabin ROUSSEAU's model for the roadblock effect of mRNA-binding Ssd1 on translation initiation in S. cerevisiae.
    
    -->Runs an inhomogeneous TASEP model of user-defined parameters that allows for a set particle of variable length, to which the exclusion process self-adapts.
    Returns a dataset containing for each time point:
    1 - The total number of particles that initiated up to that time point "passed_total". (i.e., passed through the lattice. Not to be confused with loading, where a particle enters the lattice. Named so because we model after the ribosome PIC.)
    2 - The state of each lattice site Si (0 or 1). i = 1 ,..., L
    3 - The lattice-wide density d = number of particles / L. Measured at the end of an iteration.
    
    ARGUMENTS: t, L, l, a, b, p
    t:     number of iterations to run the TASEP model; DEFAULT: t=100
    L:     lattice length;                              DEFAULT: L=30
    l:     particle length;                             DEFAULT: l=1
    a:     rate of loading;                             DEFAULT: a=0.75
    b:     rate of unloading;                           DEFAULT: b=0.75
    p:     rate of scanning (i.e., site hopping);       DEFAULT: p=1
    k_on:  rate of blocking;                            DEFAULT: k_on=0.5
    k_off: rate of unblocking;                          DEFAULT: k_off=0.5
    l_rb:  roadblock length;                            DEFAULT: l_rb=1
    B_i:   blockable lattice index list;                DEFAULT: B_i=[19]
    
    CHANGELOG:
    Changed formulaism to one matching the Gillespie algorithm, for a non-discrete timeline of events that are randomly determined in order and temporal spacing by a,b and p.
    Added to restriction rules: particles can't progress if a particle site is located l places ahead OR a block is located l' ahead (l' being the length of a block).
    With the addition of roadblocks of customisable length
    
    
    '''
    
    #set initial variables
    S_start=0
    C=[] #Lattice configuration
    B=[] #Blocking subconfiguration
    B_i.sort() #sort B_i in ascending order
    P=[] #Site hopping rates
    A=[a] #Gillespie propensities
    for i in range(L):
        C.append(S_start)
        B.append(S_start)
        if i < L-1:
            P.append(p)
        if i > 0: #to not overwrite A0=a
            if i < L-1:
                A.append(C[i]*P[i])
            else:
                A.append(0)
                
    for i in B_i:
        A.append(k_on)
        A.append(0) #k_off position
    
    
   
    passed_total=0 #counter for particles that terminated scanning
    
    #prepare returned dataset
    rini_data={'time':[0], 'passed_total':[0], 'density':[0]}
    loc1=0
    #update with all site configurations
    for S in C:
        loc1+=1
        rini_data.update({f'S{loc1}':[0]})
    #update with all block configurations    
    for i in B_i:
        rini_data.update({f'B{i+1}':[0]})
        
    
    #exclusion rule variables
    S_condition_0=C[0:l]
    B_condition_0=C[0:l_rb]
    
    #time tracker to compare against t
    time = 0
    
    #launch model
    while time <= t:
            #Rolling the random numbers for stochasticity
            R=sum(A)
            if R>0:
                r1=np.random.exponential(1/R)
                r2=np.random.uniform(0,1)*R
                time+=r1
                #determining which site is acted upon
                i = 0 #preparing the index of the moved particle
                r = 0.0 #iterative value that serves to pinpoint the index (rmax=R)
                while r < r2:
                    r += A[i]
                    i += 1
                i-=1

                #LOADING
                if i==0 and C[i]==0:
                    C[0]+=1

                #SCANNING
                elif i<L-1 and C[i]==1:
                    C[i]-=1
                    C[i+1]+=1
                    A[i]=0 #reset propensity for the current move

                #UNLOADING
                elif i==L-1 and C[i]==1:
                    C[i]-=1
                    passed_total+=1
                    A[i]=0 #reset propensity for the current move
                    
                    
                #BLOCKING/UNBLOCKING
                elif i>L-1:
                    i-=L
                    #blocking
                    if (i%2)==0:
                        blocked=B_i[int(i/2)]
                        B[blocked]+=1
                        A[i+L+1]=k_off #instantly flag the site as being unblockable
                    #unblocking
                    else:
                        unblocked=B_i[int((i-1)/2)]
                        B[unblocked]-=1
                        A[i+L]=0
    
                else:
                    print(f'An unexpected error happened at time {time}, please check the code because i={i}, A[i]={A[i]} and R={R}.')

                #UPDATING PROPENSITIES FOR THE NEXT ITERATION: LOADING, PARTICLES AND BLOCKS
                particles=[index for index in range(len(C)) if C[index] == 1]

                #load-ready?
                if C[0]==0:
                    if S_condition_0==C[0:l] and B_condition_0==B[0:l_rb]:
                        A[0]=a
                    else:
                        A[0]=0


                #particle check
                for particle in particles:
                    #unload-ready?
                    if particle==L-1:
                        A[particle]=b
                    #scan-ready?                       
                    
                    else: 
                        particle_token=0 #0 means a particle is ahead
                        roadblock_token=0 #0 means a roadblock is ahead
                        #particle checkpoint
                        if particle <= L-l-1: #can it be blocked by another particle?
                            if C[particle+l]==0: #is it not blocked by a particle?
                                particle_token=1
                        else: #can't be blocked by a particle
                            particle_token=1
                            
                                
                        #roadblock checkpoint
                        if particle <= L-l_rb-1: #can it be blocked by a roadblock?
                            if B[particle+l_rb]==0: #is it not blocked by a roadblock?
                                roadblock_token=1
                        else: #can't be blocked by a roadblock
                            roadblock_token=1
                        
                        #token validation
                        if particle_token==1 and roadblock_token==1:
                            A[particle]=P[particle]
                        else:#something is blocking the particle
                            A[particle]=0
                
                #block-ready?
                for block_ii in range(len(B_i)): #loop through block subindicies (index in the configuration index list)
                    block_i=B_i[block_ii] #get the configuration index
                    #restriction rule for blocking to be possible: depends on particle and block length, assumes the tracking site is at the head of all particles/blocks for rule simplicity.
                    
                    if block_i-l_rb+1 >=0: #if a site is place too close to the entry, this value would be negative, this condition takes this scenario into account
                        if 1 not in C[block_i-l_rb+1:block_i+l] and 1 not in B[block_i-l_rb+1:block_i+l_rb]:
                            A[L+(block_ii*2)]=k_on
                        else:
                            A[L+(block_ii*2)]=0
                    else:
                        if 1 not in C[0:block_i+l] and 1 not in B[0:block_i+l_rb]:
                            A[L+(block_ii*2)]=k_on
                        else:
                            A[L+(block_ii*2)]=0
                        

                    
                    
            
                #update dataset
                
                if time <= t:
                    rini_data.setdefault('time', []).append(time)
                elif time > t: #force the final time point to be at time=t if t is exceeded at the end of the run
                    rini_data.setdefault('time', []).append(t)

                rini_data.setdefault('passed_total', []).append(passed_total)

                particle_count=0

                loc3=0
                for S in C:
                    loc3+=1
                    rini_data.setdefault(f'S{loc3}', []).append(S)
                    if S==1:
                        particle_count+=1

                d=round(particle_count/L,2) #lattice density rounded to 2 decimals
                rini_data.setdefault('density', []).append(d)
                
                for i in B_i:
                    rini_data.setdefault(f'B{i+1}', []).append(B[i])
            
            else: #break the loop early to avoid errors in case no action is possible (which should only happen if a rate is null)
                #update dataset
                rini_data.setdefault('time', []).append(t)

                rini_data.setdefault('passed_total', []).append(passed_total)

                particle_count=0

                loc3=0
                for S in C:
                    loc3+=1
                    rini_data.setdefault(f'S{loc3}', []).append(S)
                    if S==1:
                        particle_count+=1

                d=round(particle_count/L,2) #lattice density rounded to 2 decimals
                rini_data.setdefault('density', []).append(d)
                
                for i in B_i:
                    rini_data.setdefault(f'B{i+1}', []).append(B[i])
                break

            #END OF ITERATION
            
            
                
        
    return pd.DataFrame(data=rini_data)


#Core function for the model
def corini(t=100, L=30, l=1, a=0.75, b=0.75, p=1, k_on=0.5, k_off=0.5, l_rb=1, B_i=[19], coop_p=0.4, coop_m=0.4, coop_d=1):
    '''
    
    roadblock_ini v0.7 
    (rini for short)
    
    DESCRIPTION:
    This is the 0.7 co-operative version of Gabin ROUSSEAU's model for the roadblock effect of mRNA-binding Ssd1 on translation initiation in S. cerevisiae. As it is "cooperative", it assumes block dynamics are cooperative rather than independent in the base model.
    Variables are the same as rini with three additions.
    coop_p: coop "plus", strength of the coop effect on k_on;   DEFAULT: coop_p = 0.4
    coop_m: coop "minus", strength of the coop effect on k_off; DEFAULT: coop_m = 0.4
    coop_d: coop "distance, area of effect multiplied by l_rb"; DEFAULT: coop_d = 1
    
    '''
    
    #set initial variables
    S_start=0
    C=[] #Lattice configuration
    B=[] #Blocking subconfiguration
    B_i.sort() #sort B_i in ascending order
    P=[] #Site hopping rates
    A=[a] #Gillespie propensities
    for i in range(L):
        C.append(S_start)
        B.append(S_start)
        if i < L-1:
            P.append(p)
        if i > 0: #to not overwrite A0=a
            if i < L-1:
                A.append(C[i]*P[i])
            else:
                A.append(0)
                
    for i in B_i:
        A.append(k_on)
        A.append(0) #k_off position
    
    #coop parameter limiting
    if k_on+coop_p>1: #coop_p is too high, set it to the allowed maximum
        coop_p=1-k_on
        
    if k_off-coop_m<0: #coop_m is too high, set it to the allowed maximum
        coop_m=k_off
    
    
   
    passed_total=0 #counter for particles that terminated scanning
    
    #prepare returned dataset
    rini_data={'time':[0], 'passed_total':[0], 'density':[0]}
    loc1=0
    #update with all site configurations
    for S in C:
        loc1+=1
        rini_data.update({f'S{loc1}':[0]})
    #update with all block configurations    
    for i in B_i:
        rini_data.update({f'B{i+1}':[0]})
        
    
    #exclusion rule variables
    S_condition_0=C[0:l]
    B_condition_0=C[0:l_rb]
    
    #time tracker to compare against t
    time = 0
    
    #launch model
    while time <= t:
            #Rolling the random numbers for stochasticity
            R=sum(A)
            if R>0:
                r1=np.random.exponential(1/R)
                r2=np.random.uniform(0,1)*R
                time+=r1
                #determining which site is acted upon
                i = 0 #preparing the index of the moved particle
                r = 0.0 #iterative value that serves to pinpoint the index (rmax=R)
                while r < r2:
                    r += A[i]
                    i += 1
                i-=1

                #LOADING
                if i==0 and C[i]==0:
                    C[0]+=1

                #SCANNING
                elif i<L-1 and C[i]==1:
                    C[i]-=1
                    C[i+1]+=1
                    A[i]=0 #reset propensity for the current move

                #UNLOADING
                elif i==L-1 and C[i]==1:
                    C[i]-=1
                    passed_total+=1
                    A[i]=0 #reset propensity for the current move
                    
                    
                #BLOCKING/UNBLOCKING
                elif i>L-1:
                    i-=L
                    #blocking
                    if (i%2)==0:
                        blocked=B_i[int(i/2)]
                        B[blocked]+=1
                        A[i+L]=0
                    
                    
                    #unblocking
                    else:
                        unblocked=B_i[int((i-1)/2)]
                        B[unblocked]-=1
                        A[i+L]=0
    
                else:
                    print(f'An unexpected error happened at time {time}, please check the code because i={i}, A[i]={A[i]} and R={R}.')

                #UPDATING PROPENSITIES FOR THE NEXT ITERATION: LOADING, PARTICLES AND BLOCKS
                particles=[index for index in range(len(C)) if C[index] == 1]
            
                #load-ready?
                if C[0]==0:
                    if S_condition_0==C[0:l] and B_condition_0==B[0:l_rb]:
                        A[0]=a
                    else:
                        A[0]=0


                #particle check
                for particle in particles:
                    #unload-ready?
                    if particle==L-1:
                        A[particle]=b
                    #scan-ready?                       
                    
                    else: 
                        particle_token=0 #0 means a particle is ahead
                        roadblock_token=0 #0 means a roadblock is ahead
                        #particle checkpoint
                        if particle <= L-l-1: #can it be blocked by another particle?
                            if C[particle+l]==0: #is it not blocked by a particle?
                                particle_token=1
                        else: #can't be blocked by a particle
                            particle_token=1
                            
                                
                        #roadblock checkpoint
                        if particle <= L-l_rb-1: #can it be blocked by a roadblock?
                            if B[particle+l_rb]==0: #is it not blocked by a roadblock?
                                roadblock_token=1
                        else: #can't be blocked by a roadblock
                            roadblock_token=1
                        
                        #token validation
                        if particle_token==1 and roadblock_token==1:
                            A[particle]=P[particle]
                        else:#something is blocking the particle
                            A[particle]=0
                
                #block-ready?
                for block_ii in range(len(B_i)): #loop through block subindicies (index in the configuration index list)
                    block_i=B_i[block_ii] #get the configuration index
                    #restriction rule for blocking to be possible: depends on particle and block length, assumes the tracking site is at the head of all particles/blocks for rule simplicity.
                    
                    if block_i-l_rb+1 >=0: #if a site is placed too close to the entry, this value would be negative, this condition takes this scenario into account
                        if 1 not in C[block_i-l_rb+1:block_i+l] and 1 not in B[block_i-l_rb+1:block_i+l_rb]:
                            #COOP-ON EFFECT?
                            if block_i-(l_rb*coop_d) < 0: #this first condition prevents unintended indexing at negative values when calculating cooperativity distance
                                if 1 in B[0:block_i-l_rb+1] or 1 in B[block_i+l_rb:block_i+1+(l_rb*coop_d)]:
                                    A[L+(block_ii*2)]=k_on+coop_p
                                else:
                                    A[L+(block_ii*2)]=k_on
                            elif 1 in B[block_i-(l_rb*coop_d):block_i-l_rb+1] or 1 in B[block_i+l_rb:block_i+1+(l_rb*coop_d)]:
                                A[L+(block_ii*2)]=k_on+coop_p
                            else:
                                A[L+(block_ii*2)]=k_on
                        elif B[block_i]==1:
                            #COOP-OFF EFFECT?
                            if block_i-(l_rb*coop_d) < 0:
                                if 1 in B[0:block_i-l_rb+1] or 1 in B[block_i+l_rb:block_i+1+(l_rb*coop_d)]:
                                    A[L+(block_ii*2)+1]=k_off-coop_m
                                else:
                                    A[L+(block_ii*2)+1]=k_off
                            
                            elif 1 in B[block_i-(l_rb*coop_d):block_i-l_rb+1] or 1 in B[block_i+l_rb:block_i+1+(l_rb*coop_d)]:
                                A[L+(block_ii*2)+1]=k_off-coop_m
                            else:
                                A[L+(block_ii*2)+1]=k_off
                                
                    else:
                        if 1 not in C[0:block_i+l] and 1 not in B[0:block_i+l_rb]:
                            #COOP-ON EFFECT?
                            if 1 in B[block_i+l_rb:block_i+1+(l_rb*coop_d)]:
                                A[L+(block_ii*2)]=k_on+coop_p
                            else:
                                A[L+(block_ii*2)]=k_on
                        elif B[block_i]==1:
                            #COOP-OFF EFFECT?
                            if 1 in B[block_i+l_rb:block_i+1+(l_rb*coop_d)]:
                                A[L+(block_ii*2)+1]=k_off-coop_m
                            else:
                                A[L+(block_ii*2)+1]=k_off
                        

                    
                    
                #update dataset
                
                if time <= t:
                    rini_data.setdefault('time', []).append(time)
                elif time > t: #force the final time point to be at time=t if t is exceeded at the end of the run
                    rini_data.setdefault('time', []).append(t)

                rini_data.setdefault('passed_total', []).append(passed_total)

                particle_count=0

                loc3=0
                for S in C:
                    loc3+=1
                    rini_data.setdefault(f'S{loc3}', []).append(S)
                    if S==1:
                        particle_count+=1

                d=round(particle_count/L,2) #lattice density rounded to 2 decimals
                rini_data.setdefault('density', []).append(d)
                
                for i in B_i:
                    rini_data.setdefault(f'B{i+1}', []).append(B[i])
            
            else: #break the loop early to avoid errors in case no action is possible (which should only happen if a rate is null)
                #update dataset
                rini_data.setdefault('time', []).append(t)

                rini_data.setdefault('passed_total', []).append(passed_total)

                particle_count=0

                loc3=0
                for S in C:
                    loc3+=1
                    rini_data.setdefault(f'S{loc3}', []).append(S)
                    if S==1:
                        particle_count+=1

                d=round(particle_count/L,2) #lattice density rounded to 2 decimals
                rini_data.setdefault('density', []).append(d)
                
                for i in B_i:
                    rini_data.setdefault(f'B{i+1}', []).append(B[i])
                break

            #END OF ITERATION
            
            
                
        
    return pd.DataFrame(data=rini_data)

    

#Plots a standardised initiation (protein production proxy) value against the number of blockable sites used
def rini_INIvBLOCK(t=10000, L=100, l=1, a=0.75, b=0.75, p=1, k_on=0.5, k_off=0.5, l_rb=1, B_i=[48, 49, 50], n=10, dataset=False, visual=True, comparison_output=False):
    '''
    For rini v0.7
    
    rini_INIvBLOCK: function to plot a standardised measure of the exit count (represents initiation/protein production) against the number of blocks.
    
    Takes in the usual rini parameters and "timepoint", that defines for which time point of the run average occupancies should be computed; 
    "n" defines how many rini runs will be sampled for the plot.
    "dataset" is a boolean that enables the function to the return the mean_occupancy dataset. (default: False)
    "visual" is a boolean that enables the function to plot the mean occupancies over their lattice sites. (default: True)
    '''
    #open data lists
    repetition=[] #column for repetition IDs
    blocks=[] #columns for blockable site counts
    exits=[] #column for standardised mean exits
      
    blockcount=len(B_i)+1
    
    
    #Launch n runs and calculate standardised mean exits
    exits_zero=[] #tally exits for zero blocks to establish a median standard
    #loop for as many repetitions as required
    for i in range(n):
        #record exit flux for each block scenario
        for ii in range(blockcount):
            
            current_run=rini(t,L,l,a,b,p,k_on,k_off,l_rb,B_i[0:ii])
            
            
           
            repetition.append(i)
            blocks.append(ii)
            current_exits=max(current_run['passed_total'])/t
            exits.append(current_exits)
            if ii == 0:
                exits_zero.append(current_exits)
    median_exits_zero=statistics.median(exits_zero)        
    if median_exits_zero!= 0: #prevent division by zero
        standardised_exits=[x/median_exits_zero for x in exits]   
    else:
        standardised_exits=[x*0 for x in exits]
        print('A division by zero was avoided, standard efficiency = 0 in a point.')   
    
    rini_INIvBLOCK_data=pd.DataFrame(list(zip(repetition, blocks, standardised_exits)), columns = ['repetition_number', 'block_number','initiation'])
    
    if dataset==True:
        return rini_INIvBLOCK_data
        print("Dataset returned.")
        
    if comparison_output==True:
        median1=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==1])
        median2=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==2])
        return (median1, median2)
    
    if visual==True:
        plt.figure(figsize = (12, 4))
        plt.subplot(121)
        sns.boxplot(x='block_number', y='initiation', fill=False, showcaps=False, width=.5, hue='block_number', palette='colorblind', legend=False,data=rini_INIvBLOCK_data)
        for iii in range(1,blockcount):
            median_i=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==iii-1])
            median_ii=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==iii])
            plt.plot([iii-0.5,iii-0.5], [median_i,median_ii],'--', color='black')
            plt.text(iii-0.675,median_i+0.001,f'b{iii-1}b{iii} = {median_i-median_ii:.2g}',fontsize=9)
        
        #plt.xticks(np.arange(0, L+2, step=2))
        plt.yticks(np.arange(0, 1.2, step=0.2))
        plt.xlabel('Number of blockable sites')
        plt.ylabel('Initiation efficiency (independence model)')
        plt.title(f'Initiation efficiency vs. number of blocks | Sites:{[x+1 for x in B_i]} | Pb = {round(k_on/(k_on+k_off)*100,1)}% | n = {n}')

        plt.tight_layout()
        plt.show();

#Plots a standardised initiation (protein production proxy) value against the number of blockable sites used
def corini_INIvBLOCK(t=10000, L=100, l=1, a=0.75, b=0.75, p=1, k_on=0.5, k_off=0.5, l_rb=1, B_i=[48, 49, 50],coop_p=0.4, coop_m=0.4, coop_d=1, n=10, dataset=False, visual=True, comparison_output=False):
    '''
    For corini v0.7
    
    rini_INIvBLOCK: function to plot a standardised measure of the exit count (represents initiation/protein production) against the number of blocks.
    
    Takes in the usual rini parameters and "timepoint", that defines for which time point of the run average occupancies should be computed; 
    "n" defines how many rini runs will be sampled for the plot.
    "dataset" is a boolean that enables the function to the return the mean_occupancy dataset. (default: False)
    "visual" is a boolean that enables the function to plot the mean occupancies over their lattice sites. (default: True)
    '''
    #open data lists
    repetition=[] #column for repetition IDs
    blocks=[] #columns for blockable site counts
    exits=[] #column for standardised mean exits
      
    blockcount=len(B_i)+1
    
    
    #Launch n runs and calculate standardised mean exits
    exits_zero=[] #tally exits for zero blocks to establish a median standard
    #loop for as many repetitions as required
    for i in range(n):
        #record exit flux for each block scenario
        for ii in range(blockcount):
            
            current_run=corini(t,L,l,a,b,p,k_on,k_off,l_rb,B_i[0:ii],coop_p,coop_m,coop_d)
            
            
           
            repetition.append(i)
            blocks.append(ii)
            current_exits=max(current_run['passed_total'])/t
            exits.append(current_exits)
            if ii == 0:
                exits_zero.append(current_exits)
    median_exits_zero=statistics.median(exits_zero)        
    if median_exits_zero!= 0: #prevent division by zero
        standardised_exits=[x/median_exits_zero for x in exits]   
    else:
        standardised_exits=[x*0 for x in exits]
        print('A division by zero was avoided, standard efficiency = 0 in a point.')  
    
    rini_INIvBLOCK_data=pd.DataFrame(list(zip(repetition, blocks, standardised_exits)), columns = ['repetition_number', 'block_number','initiation'])
    
    if dataset==True:
        return rini_INIvBLOCK_data
        print("Dataset returned.")
        
    if comparison_output==True:
        median1=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==1])
        median2=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==2])
        return (median1, median2)
    
    if visual==True:
        plt.figure(figsize = (12, 4))
        plt.subplot(121)
        sns.boxplot(x='block_number', y='initiation', fill=False, showcaps=False, width=.5, hue='block_number', palette='colorblind', legend=False,data=rini_INIvBLOCK_data)
        for iii in range(1,blockcount):
            median_i=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==iii-1])
            median_ii=statistics.median(rini_INIvBLOCK_data['initiation'].loc[rini_INIvBLOCK_data['block_number']==iii])
            plt.plot([iii-0.5,iii-0.5], [median_i,median_ii],'--', color='black')
            plt.text(iii-0.675,median_i+0.001,f'b{iii-1}b{iii} = {median_i-median_ii:.2g}',fontsize=9)
        
        #plt.xticks(np.arange(0, L+2, step=2))
        plt.yticks(np.arange(0, 1.2, step=0.2))
        plt.xlabel('Number of blockable sites')
        plt.ylabel('Initiation efficiency (cooperative model)')
        plt.title(f'Initiation efficiency vs. number of blocks | Sites:{[x+1 for x in B_i]} | Pb = {round(k_on/(k_on+k_off)*100,1)}% | n = {n}')

        plt.tight_layout()
        plt.show();

