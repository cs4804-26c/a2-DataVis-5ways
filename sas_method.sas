
FILENAME REFFILE '/penglings.csv';

PROC IMPORT DATAFILE=REFFILE
    out=penglings
    dbms=csv
    replace;
    getnames=yes;
    guessingrows=max;
RUN;

data penglings_clean;
    set penglings(rename=(flipper_length_mm = _flipper 
                          body_mass_g       = _body 
                          bill_length_mm    = _bill));

    flipper_length_mm = input(_flipper, ?? best.);
    body_mass_g       = input(_body, ?? best.);
    bill_length_mm    = input(_bill, ?? best.);

    drop _flipper _body _bill;
run;

ods graphics / width=8in height=5in;

proc sgplot data=penglings_clean;
    styleattrs backcolor=white wallcolor=lightgray datacolors=("#fe9013" "#018b8b" "#9932cc");

    bubble x=flipper_length_mm y=body_mass_g size=bill_length_mm / 
    	nooutline
        group=species   
        bradiusmin=3px
        bradiusmax=10px
        transparency=0.2;       

    xaxis label="Flipper Length (mm)"  
    	grid gridattrs=(color=white thickness = 1)
    	values=(170 to 239 by 10)
    	minorcount = 1
    	minorgrid
    	minorgridattrs= (color=white thickness = 0.5);
    yaxis label="Body Mass (g)"  
    	grid gridattrs=(color=white thickness = 1)
    	values=(3000 to 6900 by 1000)
    	minorcount = 1
    	minorgrid
    	minorgridattrs= (color=white thickness = 0.5);

    keylegend / title="Species" location=outside position=right;
    
run;