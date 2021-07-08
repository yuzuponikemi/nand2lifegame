# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:15:17 2021
   /** Generate random numbers with LCG. */
   method Array randoms() {
      var Array randoms, randomsbin;
	  var int seed,j,a,c,m,axc,temp,tempp;
	  let randoms = Array.new(yw*xw);
	  let randomsbin = Array.new(xw*yw);
	  //let randoms[0] = Keyboard.readInt("Enter a seed number(not 0): ");
	  let randoms[0] = 1;
      let j = 0;
	  let a = 141;
	  let c = 1;
	  let m = 499;
	  while(j<(xw*yw)){
	    //do Output.printInt(j);
		let temp = (a*randoms[j])+c ;
		let tempp = mod(temp,m);
		let j = j + 1;
		let randoms[j] = Math.abs(tempp);
		do Output.printInt(randoms[j]);
		do Output.printChar(a);
		if (mod(tempp,3)=0){ //mod(tempp,2)=0
			let randomsbin[j] = 1;}
		else{let randomsbin[j] = 0;}
		
	  }
	  do randoms.dispose();
      return randomsbin;
   }
        
           /** Calc moduler. */
   method int mod(int i, int m) {
      var int temp, tempp;
	  let temp = (i/m)*m;
	  let tempp = i - temp;
      return tempp;
   }
@author: IKM1YH
"""

import math

a = 17

j = 0
c = 1
m = 2371
out = False
for a in range(5,m):
    randoms = [4]
    for j in range(m):
        ax = a*randoms[j]
        nex = (ax+c)%m
        if nex in randoms:
            #print('over man')
            break
        else:
            randoms.append(nex)
        if j == m-3:
            print('got it')
            print(a)
            out = True
            break
    if out :break
