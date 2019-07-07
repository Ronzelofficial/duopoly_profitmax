from sympy import *
x, y, z, t, q, Q = symbols('x y z t q Q')


def simultaneous_duopoly(demand, cost1, cost2):
    main1 = demand * x - cost1
    profit1 = simplify(main1)
    deriv1 = diff(profit1, x)

    main2 = demand * y - cost2
    profit2 = simplify(main2)
    deriv2 = diff(profit2, y)

    cv_sim = solve((deriv1, deriv2), (x, y))

    firstsub1 = profit1.subs(x, cv_sim[x])
    firm1_profit = firstsub1.subs(y, cv_sim[y])
    firstsub2 = profit2.subs(y, cv_sim[y])
    firm2_profit = firstsub2.subs(x, cv_sim[x])
    price1 = demand.subs(x, cv_sim[x])
    price2 = price1.subs(y, cv_sim[y])

    x1_sim = round(cv_sim[x])
    y1_sim = round(cv_sim[y])
    p_sim = round(price2, 2)
    profit1_sim = round(firm1_profit, 2)
    profit2_sim = round(firm2_profit, 2)

    return (x1_sim, y1_sim, p_sim, profit1_sim, profit2_sim)

def sequential_duopoly(demand, cost1, cost2):
    main1 = demand * x - cost1
    profit1 = simplify(main1)

    main2 = demand * y - cost2
    profit2 = simplify(main2)
    deriv2 = diff(profit2, y)

    br2 = solve(deriv2, y)

    expr2 = profit1.subs(y, br2[0])
    foc = diff(expr2, x)
    firm1quan = solve(foc, x)
    firm2quan = br2[0].subs(x, firm1quan[0])

    firstsub1 = profit1.subs(x, firm1quan[0])
    firm1_profit = firstsub1.subs(y, firm2quan)
    firstsub2 = profit2.subs(y, firm2quan)
    firm2_profit = firstsub2.subs(x, firm1quan[0])

    pricex = demand.subs(x, firm1quan[0])
    price = pricex.subs(y, firm2quan)

    x1_seq = round(firm1quan[0])
    y1_seq = round(firm2quan)
    p_seq = round(price, 2)
    profit1_seq = round(firm1_profit, 2)
    profit2_seq = round(firm2_profit, 2)

    return (x1_seq, y1_seq, p_seq, profit1_seq, profit2_seq)


def symmetric_cartel(demand, cost1, cost2):
    main = demand * x + demand * y - cost1 - cost2
    profit = simplify(main)
    profit1 = demand * x - cost1
    profit2 = demand * y - cost2
    deriv1 = diff(profit, x)
    deriv2 = diff(profit, y)
    foc = deriv1.subs(y, x)
    cv_cart = solve(foc, x)

    profit_x = profit.subs(x, cv_cart[0])
    profit_cart = (profit_x.subs(y, cv_cart[0]))/2

    pricex = demand.subs(x, cv_cart[0])
    price = pricex.subs(y, cv_cart[0])


    quan_cart1 = round(cv_cart[0])
    p_cart = round(price, 2)
    profit_cartel = round(profit_cart, 2)

    return(quan_cart1, p_cart, profit_cartel)

def folk_theorem(demand, cost1, cost2):
  main1_sim = demand*x - cost1
  profit1_sim = simplify(main1_sim)
  deriv1_sim = diff(profit1_sim, x)

  main2_sim = demand*y - cost2
  profit2_sim = simplify(main2_sim)
  deriv2_sim = diff(profit2_sim, y)

  cv_sim = solve((deriv1_sim, deriv2_sim), (x, y))

  firstsub1 = profit1_sim.subs(x, cv_sim[x])
  firm1_profit = firstsub1.subs(y, cv_sim[y])
  firstsub2 = profit2_sim.subs(y, cv_sim[y])
  firm2_profit = firstsub2.subs(x, cv_sim[x])

  profit1_sim = round(firm1_profit, 2)
  profit2_sim = round(firm2_profit, 2)

  main = demand * x + demand * y - cost1 - cost2
  profit = simplify(main)
  profit1 = demand * x - cost1
  profit2 = demand * y - cost2
  deriv1 = diff(profit, x)
  deriv2 = diff(profit, y)
  foc = deriv1.subs(y, x)
  cv_cart = solve(foc, x)

  profit_x = profit.subs(x, cv_cart[0])
  profit_cart = (profit_x.subs(y, cv_cart[0]))/2

  pricex = demand.subs(x, cv_cart[0])
  price = pricex.subs(y, cv_cart[0])


  quan_cart1 = round(cv_cart[0])
  p_cart = round(price, 2)
  profit_cartel = round(profit_cart, 2)

  maind = demand * y - cost2
  profitd = simplify(maind)
  derivd = diff(profitd, y)
  br2 = solve(derivd, y)
  deviation = br2[0].subs(x, quan_cart1)
  profitx_sub = profitd.subs(x, quan_cart1)
  deviation_profit = profitx_sub.subs(y, deviation)

  folk_dirty = (deviation_profit - profit_cartel)/(deviation_profit - profit2_sim)

  folk = round(folk_dirty, 3)
  return(folk)