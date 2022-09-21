-- "UPGRADE CDST v1.2 as Arrow Signal" is creat by "Kittitat Wasati" --  
instrument { name = "UPGRADE CDST", short_name = "UPGRADE CDST", icon = 'https://www.img.in.th/images/53726d263d57e3e1d3eca6984c781a70.gif', overlay = true }

-- color setting -- 
input_group {
   "Color",
   colorBuy = input { default = "#08FE0B", type = input.color },
   colorSell = input { default = "#FF0909", type = input.color },
   width = input { default = 1, type = input.line_width}
}

-- display -- 
fastma = ema (close, 5)
slowma = ema (close, 15)
targetma = ema (close, 30)
trendma = ema (close, 60)
-- end of frist script --

-- B2 Signal --
fastma1 = fastma[1]
targetma1 = targetma[1]
-- B2 Buy --
    plot_shape((
        fastma > targetma and  -- 5 > 30
        fastma1 < targetma1 and -- Before 5 < 30
        targetma > slowma and -- 30 > 15
        trendma > fastma and -- 60 > 5
        trendma > slowma and -- 60 > 15
        trendma > targetma and -- 60 > 30
        close > fastma and -- Candle are closed price more than EMA5
        close > trendma),  -- Candle are closed price more than EMA60
        "B2_Buy",
        shape_style.arrowup,
        shape_size.auto,
        colorBuy,
        shape_location.belowbar,
        0,
        "Buy Next Bar +5 min",
        colorBuy     
    )
-- B2 Sell --
    plot_shape((
        fastma < targetma and  -- 5 < 30
        fastma1 > targetma1 and -- Before 5 > 30
        targetma < slowma and -- 30 < 15
        trendma < fastma and -- 60 < 5
        trendma < slowma and -- 60 < 15
        trendma < targetma and -- 60 < 30
        close < fastma and -- Candle are closed price low than EMA5
        close < trendma), -- Candle are closed price low than EMA60
        "B2_Sell",
        shape_style.arrowdown,
        shape_size.auto,
        colorSell,
        shape_location.abovebar,
        0,
        "Sell Next Bar +5 min",
        colorSell     
    )
-- end of B2 Signal --

-- B3 Signal --
fastma1 = fastma[1]
trendma1 = trendma[1]
-- B3 Buy --
    plot_shape((
        fastma > trendma and  -- 5 > 60
        fastma1 < trendma1 and -- Before 5 < 60
        slowma > targetma and -- 15 > 30
        slowma < trendma and -- 15 < 60
        close > fastma and -- Candle are closed price more than EMA5
        close > trendma),  -- Candle are closed price more than EMA60
        "B3_Buy",
        shape_style.arrowup,
        shape_size.auto,
        colorBuy,
        shape_location.belowbar,
        0,
        "Buy Next Bar +5 min",
        colorBuy     
    )
-- B3 Sell --
    plot_shape((
        fastma < trendma and  -- 5 < 60
        fastma1 > trendma1 and -- Before 5 > 60
        slowma < targetma and -- 15 < 30
        slowma > trendma and -- 15 > 60
        close < fastma and -- Candle are closed price low than EMA5
        close < trendma),  -- Candle are closed price low than EMA60
        "B3_Sell",
        shape_style.arrowdown,
        shape_size.auto,
        colorSell,
        shape_location.abovebar,
        0,
        "Sell Next Bar +5 min",
        colorSell    
    )
    
-- B4 Signal --
fastma1 = fastma[1]
slowma1 = slowma[1]
-- B4 Buy --
    plot_shape((
        fastma > slowma and  -- 5 > 15
        fastma1 < slowma1 and -- Before 5 < 15
        targetma > slowma and -- 30 > 15
        targetma > fastma and -- 30 > 5
        trendma > fastma and -- 60 > 5
        trendma > slowma and -- 60 > 15
        trendma > targetma and -- 60 > 30
        close > targetma and -- Candle are closed price high than EMA30
        close < trendma),  -- Candle are closed price low than EMA60
        "B4_Buy",
        shape_style.arrowup,
        shape_size.auto,
        colorBuy,
        shape_location.belowbar,
        0,
        "Buy Next Bar +5 min",
        colorBuy     
    )
-- B4 Sell --
    plot_shape((
        fastma < slowma and  -- 5 < 15
        fastma1 > slowma1 and -- Before 5 > 15
        targetma < slowma and -- 30 < 15
        targetma < fastma and -- 30 < 5
        trendma < fastma and -- 60 < 5
        trendma < slowma and -- 60 < 15
        trendma < targetma and -- 60 < 30
        close < targetma and -- Candle are closed price low than EMA30
        close > trendma),  -- Candle are closed price high than EMA60
        "B4_Sell",
        shape_style.arrowdown,
        shape_size.auto,
        colorSell,
        shape_location.abovebar,
        0,
        "Sell Next Bar +5 min",
        colorSell     
    )

