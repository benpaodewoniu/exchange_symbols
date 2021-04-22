import glob

txts = glob.glob(r"./platfrom_symbol/*.txt")

symbol_pair = ['KRW', 'JPY', 'BTC', 'EUR', 'USD', 'USDT', 'PERP', 'CQ', 'NW', 'NQ', 'CW', 'NNQ', 'CM', 'NM', "USTF0",
               "BTCF0", 'XBT']


def p(coin):
    print(coin.upper() + "={")

    for t in txts:
        exchange = t.split('/')[2].split('.')[0].upper()
        symbols = []
        with open(t, 'r') as f:
            line = f.readline().strip()
            while line:
                if coin.upper() in line.upper():
                    for pair in symbol_pair:
                        if pair.upper() in line.strip().upper():
                            if line.strip() not in symbols:
                                symbols.append(line.strip())
                line = f.readline()
            tmp = "Exchange." + exchange + ".value" + ":'"
            if len(symbols) > 0:
                ss = ",".join(symbols)
                tmp = tmp + ss + "',"
                print(tmp)
    print("}")
    # for symbol in symbols:
    #     tmp = tmp + str(symbol.strip()) + ','
    # tmp = tmp.


if __name__ == '__main__':

    # coins = [
    #     'CRV',
    #     'DEFI',
    #     'DOGE',
    #     'EGLD',
    #     'ENJ',
    #     'ETC',
    #     'FLM',
    #     'GRT',
    #     'ICX',
    #     'IOST',
    #     'IOTA',
    #     'KAVA',
    #     'KNC',
    #     'KSM',
    #     'LRC',
    #     'MKR',
    #     'NEO',
    #     'OCEAN',
    #     'OMG',
    #     'ONT',
    #     'QTUM',
    #     'REN',
    #     'RLC',
    #     'RSR',
    #     'SOL',
    #     'SRM',
    #     'STORJ',
    #     'SUSHI',
    #     'SXP',
    #     'THETA',
    #     'TOMO',
    #     'TRB',
    #     'TRX',
    #     'VET',
    #     'WAVES',
    #     'XLM',
    #     'XMR',
    #     'XRP',
    #     'XTZ',
    #     'ZEC',
    #     'ZEN',
    #     'ZIL',
    #     'ZRX',
    #     'OKB'
    # ]
    coins = [
        "bch"
    ]
    for coin in coins:
        p(coin)
