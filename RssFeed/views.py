from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .feedparser import parse

from datetime import date, datetime

today = date.today()


def index(request):
    NewsFeed1 = parse("https://cointelegraph.com/rss")
    NewsFeed2 = parse("https://news.bitcoin.com/feed/")
    NewsFeed3 = parse("https://www.reddit.com/r/CryptoCurrency/top/.rss?format=xml")
    
    cointelegraph,bitcoin,reddit=[],[],[]

    i=NewsFeed1.entries
    for a in i:
        datetime1= a.published[5:25]
        dict = {
            'title': a.title[0:75],
            'img': a.links[1].href,
            'link': a.link,
            'date': a.published[5:16],
            
            'datetime2': datetime.strptime(datetime1, '%d %b %Y %H:%M:%S'),
            'tag': a.tags[0].term,
            'name': "CoinTelegraph"
            }
        cointelegraph.append(dict)
    
    i=NewsFeed2.entries

    for a in i:
        b=a.summary
        c = parse(b)
        img = c.feed.img["src"]
        
        datetime1= a.published[5:25]
        
        dict={
            'title': a.title[0:75],
            'link': a.link,
            'date': a.published[5:16],
                
            'datetime2': datetime.strptime(datetime1, '%d %b %Y %H:%M:%S'),
            'tag': a.tags[0].term,
            'img': img,
            'name': "Bitcoin"
            }
        bitcoin.append(dict)
        

    i=NewsFeed3.entries
    for a in i:

        c= a.content[0].value
        b= parse(c)
        datetime1 = a.updated[0:10] + " " +a.updated[11:19]
        
        if b.feed.has_key('img'):
            img = b.feed.img["src"]
            
            dict = {
                'title': a.title[0:75],
                'link': a.link,
                'date': a.updated[0:10],
                
                'datetime2': datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S'),
                'tag': a.tags[0].term,
                'img': img,
                'name': "Reddit"
                }
            reddit.append(dict)
                
        else:
            pass
        


    
    l= cointelegraph+bitcoin+reddit
    lf = sorted(l, key = lambda i: i['datetime2'], reverse= True)
    l1 = lf[0:9]
    l2 = lf[9:27]

    a= l1[0]
    b= l1[1]
    c=l1[2]
    d=l1[3]
    e=l1[4]
    f=l1[5]
    g=l1[6]
    h=l1[7]
    i=l1[8]
    

    context= {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'l2': l2,
        'today': today
    }
    return render(request,'index.html',context)

def resources(request):
    c_wallets=[
    {'name': "My Ether Wallet",
     'link': "https://www.myetherwallet.com/"},
    {'name': "Blockchani Wallet",
     'link': "https://www.blockchain.com/wallet"},
    {'name': "Cryptonator Online Wallet",
     'link': "https://www.cryptonator.com/"},
    {'name': "Coinbase Wallet",
     'link': "https://wallet.coinbase.com/"},
    {'name': "Btc.com Wallet",
     'link': "https://wallet.btc.com/"}
    
    ]

    h_wallets=[
        {'name': "Ledger",
         'link': "https://www.ledger.com"},
        {'name': "Trezor",
        'link': "https://trezor.io/"},
        {'name': "CoolWallet",
         'link': "https://www.coolwallet.io/"},
        {'name': "BitLox",
         'link': "https://www.bitlox.com/"},
        {'name': "KeepKey",
         'link': "https://shapeshift.com/keepkey"}
        
        ]

    c_exchanges=[
        {'name': "Binance",
         'link': "https://www.binance.com/en?ref=15269217"},
        {'name': "Coinbase",
         'link': "https://www.coinbase.com/"},
        {'name': "BitMEX",
         'link': "https://www.bitmex.com/"},
        {'name': "Huobi Global",
         'link': "https://www.huobi.com/en-us/"},
        {'name': "KuCoin",
         'link': "https://www.kucoin.com/"}
        ]

    
    c_news = [
        {'name': "Cointelegraph",
         'link': "https://cointelegraph.com/"},
        {'name': "Coindesk",
         'link': "https://www.coindesk.com/"},
        {'name': "NewsBitcoin",
         'link': "https://news.bitcoin.com/"},
        {'name': "CCN",
         'link': "https://www.ccn.com/"},
        {'name': "BitcoinMagazine",
         'link': "https://bitcoinmagazine.com/"}
    ]

    c_forums = [
        {'name': "Bitcointalk",
         'link': "https://bitcointalk.org/"},
        {'name': "Bitcoin.com forum",
         'link': "https://forum.bitcoin.com/"},
        {'name': "Beermoneyforum",
         'link': "https://www.beermoneyforum.com/"},
        {'name': "Cryptocurrencytalk",
         'link': "https://cryptocurrencytalk.com/"},
        {'name': "Mastersofcrypto Forum",
         'link': "https://mastersofcrypto.com/forum/"}
        ]

    r_cryptocurrency = [
        {'name': "r/Bitcoin",
         'link': "https://www.reddit.com/r/Bitcoin/"},
        {'name': "r/Cryptocurrency",
         'link': "https://www.reddit.com/r/Cryptocurrency/"},
        {'name': "r/ethereum",
         'link': "https://www.reddit.com/r/ethereum/"},
        {'name': "r/btc",
         'link': "https://www.reddit.com/r/btc/"},
        {'name': "r/litecoin",
         'link': "https://www.reddit.com/r/litecoin/"}
    ]

    

    b_mining_software = [
        {'name': "MinerGate",
         'link': "https://minergate.com/"},
        {'name': "BTCMiner",
         'link': "https://mining.bitcoin.com/"},
        {'name': "RPCminer",
         'link': "https://en.bitcoin.it/wiki/RPC_Miner"},
        {'name': "GUIMiner",
         'link': "https://cnguiminer.com/"},
        {'name': "GroupFabric",
         'link': "https://www.groupfabric.com/"}
        ]

    m_pools = [
        {'name': "F2Pool",
         'link': "https://www.f2pool.com/"},
        {'name': "Antpool",
         'link': "https://antpool.com/"},
        {'name': "SlushPool",
         'link': "https://slushpool.com/home/"},
        {'name': "ViaBTC",
         'link': "https://www.viabtc.com/?lang=en_US"},
        {'name': "Bitminter",
         'link': "https://bitminter.com/"}
        ]

    u_ico = [
        {'name': "Fidelityhouse",
         'link': "https://icobench.com/ico/fidelity-house"},
        {'name': "Membrana",
         'link': "https://icobench.com/ico/membrana"},
        {'name': "Poof Of Toss",
         'link': "https://icobench.com/ico/toss"},
        {'name': "Elrond",
         'link': "https://elrond.com/"},
        {'name': "Aidus",
         'link': "https://aidus.io/"}
    ]

    airdrops = [
        {'name': "ICO Drops",
         'link': "https://icodrops.com/"},
        {'name': "Gift.ONE",
         'link': "https://www.facebook.com/GiftONE2018/"},
        {'name': "Airdrop Alert",
         'link': "https://airdropalert.com/"},
        {'name': "AirdropBob",
         'link': "https://www.airdropbob.com/"},
        {'name': "Coin Airdrops",
         'link': "https://coinairdrops.com/"}
        ]

    c_calender = [
        {'name': "CoinMarketCal",
         'link': "https://coinmarketcal.com/en/"},
        {'name': "ICO Calender",
         'link': "https://tokenmarket.net/ico-calendar"},
        {'name': "Coin Calender",
         'link': "http://www.coincalendar.info/"},
        {'name': "Wiser ICO",
         'link': "https://icobench.com/ico/wise"},
        {'name': "Coins Calender",
         'link': "https://coinscalendar.com/"}
    ]

    charting = [
        {'name': "Coinmarketcap",
         'link': "https://coinmarketcap.com/"},
        {'name': "Investing.com",
         'link': "https://www.investing.com/"},
        {'name': "Tradingview",
         'link': "https://in.tradingview.com/"},
        {'name': "Etherscan.io",
         'link': "https://etherscan.io/"},
        {'name': "Blockchain",
         'link': "https://www.blockchain.com/"}
        ]

    c_gambling = [
        {'name': "Luckygames.io",
         'link': "https://luckygames.io/"},
        {'name': "bitStarz",
         'link': "https://www.bitstarz.com/"},
        {'name': "Nitrogensports",
         'link': "https://nitrogensports.eu/"},
        {'name': "Primedice",
         'link': "https://primedice.com/"},
        {'name': "mBit Casino",
         'link': "https://www.mbitcasino.com/"}
        
        ]


    c_tracking = [
        {'name': "CoinTracking",
         'link': "https://cointracking.info/"},
        {'name': "coin.fyi",
         'link': "https://coin.fyi/"},
        {'name': "Blox",
         'link': "https://www.blox.io/"},
        {'name': "Altpocket",
         'link': "https://altpocket.io/"},
        {'name': "Blockfolio",
         'link': "https://blockfolio.com/"}
        ]

    

    

    context={
        'c_wallets' : c_wallets,
        'h_wallets' : h_wallets,
        'c_exchanges' : c_exchanges,
        'c_news': c_news,
        'c_forums' : c_forums,
        'r_cryptocurrency': r_cryptocurrency,
        'b_mining_software' : b_mining_software,
        'm_pools' : m_pools,
        'u_ico' : u_ico,
        'airdrops' : airdrops,
        'c_calender' : c_calender,
        'charting' : charting,
        'c_gambling' : c_gambling,
        'c_tracking' : c_tracking
        
    }
    return render(request,'resources.html',context)

