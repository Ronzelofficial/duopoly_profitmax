# duopoly_profitmax
A profit maximization calculator for Cournot duopoly, Stackelberg duopoly, symmetric cartel, and folk theorem.

Requires installation of mpmath and sympy 
  follow instructions https://www.sympy.org/en/index.html
  
All functions are oriented around inverse demand and cost functions. Where x = firm1 quantity and y = firm2 quantity. Inverse demand refers to all demand curves being in the form of Price = 

All functions take 3 parameters. Inverse demand, cost of firm 1, cost of firm 2
  
This file contains 4 functions 
  1. Simultaineous Duopoly. 
      This calculates the classic Cournot Duopoly profit maximizing quantity for each firm. Market price. As well       as profit for each firm. This function works with asymmetric costs. 
      
  2. Sequential Duopoly 
      This calculates the classic Stackleberg Duopoly profit maximizing quantity for each firm. Market price. As       well as profit for each firm. It assumes that firm 1 plays 1st and firm 2 plays 2nd. This function works         with asymmetric costs. 
      
  3. Symmetric Cartel 
      This calculates the classic Cartel Collusion profit maximizing quantity for each firm. Market price. As           well as profit for an individual firm. As the name suggests, this requires symmetric cost functions in the       sense that market clearing quantity chosen by each firm must be identical. 
      
  4. Folk theorem calculates the classic discounting requirement that a firm needs in order to maintain the            collusive agreement. The code is based in part on the Symmetric Cartel function and therefore requires            symmetric costs in the form of market clearing quantities. The function is based on the Grim Trigger              punishment criterion. 
  

Note to developers who wish to expand on this. 

Current Limitations 
1. When a firm is facing negative costs or huge costs the software will not coerce output to zero. i.e, a firm      cannot produce negative output. 

2. Functions 3&4 can be expanded to handle asymmetric costs in the form of quantities chosen. 

3. Can be expanded to firms facing different demand functions 

4. Can be expanded to handle capital constraints 
