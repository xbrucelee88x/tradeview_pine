#Simple Backtest with Tradingview/Pine script


//https://www.youtube.com/watch?v=P5CCRvEwG4o

strategy("Moving average cross", overlay=true)


ema20 = ta.ema(close, 20)
ema50 = ta.ema(close, 50)

long = ema20 > ema50
short = ema20 > ema50

longcondition = long and long[10] and not long[11]
shortcondition = short and short[10] and not short[11]

closelong = ema20 < ema50 and not long[11]
closeshort = ema20 > ema50 and not short[11]

plot(ema20, title="20", color=#00ffaa, linewidth=3)
plot(ema50, title="50", color=#FFC1CC, linewidth=2)

start = timestamp(2015,6,1,0,0)
end = timestamp(2019,6,1,0,0)

if time >= start and time <= end
    strategy.entry("long", strategy.long, 1000.0, when = longcondition)
    strategy.entry("short", strategy.long, 1000.0, when = shortcondition)
    
strategy.close("long", when = closeshort)
strategy.close("short", when = closelong)




    
    
    





