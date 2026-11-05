import math,itertools
from .common import number,integer,identifier
def run(d):
 half=number(d['backlash'],0,1e6)/2;commands=[number(x,-1e9,1e9)for x in d['commands']]
 if not 1<=len(commands)<=10000:raise ValueError('commands')
 y=number(d.get('initial_output',commands[0]),commands[0]-half,commands[0]+half);out=[];command_travel=0;actual_travel=0
 for i,x in enumerate(commands):
  old=y;y=max(x-half,min(x+half,y));command_travel+=abs(x-commands[i-1])if i else 0;actual_travel+=abs(y-old)
  out.append(dict(command=x,output=y,tracking_error=x-y,movement=y-old))
 return dict(trace=out,command_travel=command_travel,output_travel=actual_travel,dead_travel=command_travel-actual_travel)
